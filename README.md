# Public APIs Directory

This is a fast, searchable REST API wrapped around the famous open-source [public-apis](https://github.com/public-apis/public-apis) repository.

The original official JSON API for that repository went offline. This project restores that functionality using a fully automated Python parser and a FastAPI backend.

## Live API

This project is available on RapidAPI with a free tier:

[Use the Public Free APIs Directory on RapidAPI](https://rapidapi.com/kawinthorn11collab/api/free-api-directory-api)

Live backend:

```text
https://free-api-directory-nxmezfwbj-kawinthorn11-7692s-projects.vercel.app
```

Core endpoints:

```text
GET /categories
GET /entries
GET /entries?category=Weather&cors=yes
GET /entries?auth=No&https=true
GET /random
GET /random?category=Weather
```

## Features
- **1,400+ Free APIs Indexed**: Constantly up-to-date with the master Markdown file.
- **Search & Filter**: Find APIs by category, title, auth type, HTTPS support, and CORS capability.
- **Randomizer**: Pull a random free API to spark your next project idea.
- **Serverless Ready**: Instantly deployable to Vercel's free tier.

## Endpoints

### 1. `GET /categories`
Returns a list of all 51 available categories (e.g., Animals, Weather, Games & Comics).

### 2. `GET /entries`
Returns the full directory of APIs.
**Query Parameters (All Optional):**
- `category` (string): e.g., `Weather`
- `title` (string): Search by API name
- `auth` (string): e.g., `apiKey`, `OAuth`, `No`
- `https` (boolean): `true` or `false`
- `cors` (string): e.g., `yes`, `no`

*Example:* `/entries?category=Weather&cors=yes&auth=No`

### 3. `GET /random`
Returns a single random API.
**Query Parameters:**
- `category` (string): Restrict the random pick to a specific category.

## Local Execution
1. Parse the latest markdown: `python parser.py`
2. Start the server: `uvicorn api.index:app --reload`
3. View Docs: `http://127.0.0.1:8000/docs`