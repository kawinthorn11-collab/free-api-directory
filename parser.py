import json
import re
import os

def parse_markdown(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    apis = []
    current_category = None

    # Match markdown headers for categories (### Category Name)
    header_pattern = re.compile(r'^###\s+(.+)$')
    
    # Match markdown table rows: | API | Description | Auth | HTTPS | CORS |
    row_pattern = re.compile(r'^\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|')

    lines = content.split('\n')
    for line in lines:
        header_match = header_pattern.match(line.strip())
        if header_match:
            current_category = header_match.group(1).strip()
            continue

        row_match = row_pattern.match(line.strip())
        if row_match and current_category:
            api_name = row_match.group(1).strip()
            api_link = row_match.group(2).strip()
            api_desc = row_match.group(3).strip()
            api_auth = row_match.group(4).strip()
            api_https = row_match.group(5).strip()
            api_cors = row_match.group(6).strip()

            if api_name.lower() != 'api': # Skip table headers
                apis.append({
                    "API": api_name,
                    "Description": api_desc,
                    "Auth": api_auth if api_auth else "No",
                    "HTTPS": True if api_https.lower() == 'yes' else False,
                    "Cors": api_cors,
                    "Link": api_link,
                    "Category": current_category
                })

    return apis

if __name__ == "__main__":
    if os.path.exists("README.md"):
        data = parse_markdown("README.md")
        with open("public_apis.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"Successfully extracted {len(data)} APIs into public_apis.json")
    else:
        print("README.md not found.")
