from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import os
import random

app = FastAPI(
    title="Public APIs Directory",
    description="A free, searchable JSON API wrapping the famous github.com/public-apis repository.",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
)

# Load data into memory on startup
DATA_FILE = os.path.join(os.path.dirname(__file__), "../public_apis.json")
try:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        API_DATA = json.load(f)
except FileNotFoundError:
    API_DATA = []

@app.get("/", tags=["General"])
def root():
    return {
        "status": "online",
        "total_apis": len(API_DATA),
        "endpoints": ["/entries", "/random", "/categories"]
    }

@app.get("/entries", tags=["Search"])
def get_entries(
    category: str = Query(None, description="Filter by category (e.g., 'Animals')"),
    title: str = Query(None, description="Filter by API name/title"),
    auth: str = Query(None, description="Filter by auth type (e.g., 'apiKey', 'OAuth', 'null')"),
    https: bool = Query(None, description="Filter by HTTPS support"),
    cors: str = Query(None, description="Filter by CORS support ('yes', 'no', 'unknown')")
):
    results = API_DATA

    if category:
        results = [api for api in results if category.lower() in api.get("Category", "").lower()]
    if title:
        results = [api for api in results if title.lower() in api.get("API", "").lower()]
    if auth is not None:
        if auth.lower() in ["null", "no", "none"]:
            results = [api for api in results if api.get("Auth", "No").lower() in ["no", ""]]
        else:
            results = [api for api in results if auth.lower() in api.get("Auth", "").lower()]
    if https is not None:
        results = [api for api in results if api.get("HTTPS") is https]
    if cors:
        results = [api for api in results if cors.lower() in api.get("Cors", "").lower()]

    return {
        "count": len(results),
        "entries": results
    }

@app.get("/random", tags=["Search"])
def get_random(
    category: str = Query(None, description="Filter by category before picking random")
):
    results = API_DATA
    if category:
        results = [api for api in results if category.lower() in api.get("Category", "").lower()]
    
    if not results:
        raise HTTPException(status_code=404, detail="No APIs found matching criteria.")
        
    return {
        "count": 1,
        "entries": [random.choice(results)]
    }

@app.get("/categories", tags=["Metadata"])
def get_categories():
    categories = sorted(list(set([api.get("Category") for api in API_DATA if api.get("Category")])))
    return {
        "count": len(categories),
        "categories": categories
    }
