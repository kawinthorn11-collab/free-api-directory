# RapidAPI Publishing Package: Free API Directory

---

## 1. General Details
*   **API Name:** `Public Free APIs Directory`
*   **Short Description:** `Search, filter, and discover over 1,400+ free public APIs for your next software project.`
*   **Category:** `Data`
*   **Tags:** `free api, directory, tools, developer tools, public apis, json, search`

## 2. Long Description (Paste into "About" section)
```markdown
Stop hunting through massive markdown files for free APIs. 

This API provides a fully searchable, programmatic REST interface to the famous "Public APIs" repository. We have indexed over 1,400+ free APIs across 51 categories (Weather, Animals, Machine Learning, Games, etc.).

### Features
- **Categorized**: Instantly pull APIs for a specific niche.
- **Filterable**: Search by Auth type (e.g., `OAuth`, `apiKey`, `No`), CORS support, or HTTPS availability.
- **Randomizer**: Stuck on what to build next? Hit the `/random` endpoint to get a random free API to spark your imagination.
```

## 3. Base URL Configuration
*   **Base URL:** `https://free-api-directory-nxmezfwbj-kawinthorn11-7692s-projects.vercel.app`

## 4. Endpoints & Responses (Add to "Endpoints" tab)

### Endpoint 1: Get Categories
*   **Name:** `Get Categories`
*   **Method:** `GET`
*   **Path:** `/categories`
*   **Description:** `Returns a list of all 51 available API categories.`
*   **Example Response:**
    ```json
    {
      "count": 51,
      "categories": [
        "Animals",
        "Anime",
        "Anti-Malware",
        "Art & Design",
        "Weather"
      ]
    }
    ```

### Endpoint 2: Search Entries
*   **Name:** `Search Entries`
*   **Method:** `GET`
*   **Path:** `/entries`
*   **Query Parameters (All Optional):** 
    - `category` (String) - e.g., `Weather`
    - `title` (String)
    - `auth` (String) - e.g., `No`
    - `cors` (String) - e.g., `yes`
    - `https` (Boolean)
*   **Example Response:**
    ```json
    {
      "count": 1,
      "entries": [
        {
          "API": "Open-Meteo",
          "Description": "Global weather forecast API for non-commercial use",
          "Auth": "No",
          "HTTPS": true,
          "Cors": "Yes",
          "Link": "https://open-meteo.com/",
          "Category": "Weather"
        }
      ]
    }
    ```

### Endpoint 3: Random API
*   **Name:** `Get Random API`
*   **Method:** `GET`
*   **Path:** `/random`
*   **Query Parameters:** `category` (String, Optional)
*   **Example Response:**
    ```json
    {
      "count": 1,
      "entries": [
        {
          "API": "Cat Facts",
          "Description": "Daily cat facts",
          "Auth": "No",
          "HTTPS": true,
          "Cors": "No",
          "Link": "https://alexwohlbruck.github.io/cat-facts/",
          "Category": "Animals"
        }
      ]
    }
    ```

## 5. Pricing Strategy (Add to "Monetize" tab)
Since this targets developers looking for *free* tools, we will use a highly generous freemium model to capture massive volume, while charging a premium to data-aggregators or AI agents.

1. **BASIC (Free)**
   *   **Monthly Quota:** 1,000 requests
   *   **Hard Limit:** Yes 

2. **PRO ($5.00 / month)**
   *   **Monthly Quota:** 50,000 requests
   *   **Hard Limit:** No
   *   **Overage:** $0.001 per additional request

## 6. Step-by-Step RapidAPI Setup
1. Go to RapidAPI Studio.
2. Click **Add New API**. Fill in details from Section 1.
3. Paste Section 2 into the **About** tab.
4. Paste the Base URL (`https://free-api-directory-nxmezfwbj-kawinthorn11-7692s-projects.vercel.app`) into the **Base URL** tab.
5. Create the 3 endpoints from Section 4.
6. Set the Free/Pro pricing tiers in the **Monetize** tab.
7. Click **Make API Public**.

---

# Launch Materials

## Reddit / Indie Hackers
**Title:** I turned the massive "Public APIs" GitHub repo into a searchable JSON API.

**Body:**
Hey guys, the `public-apis` repo on GitHub is great (400k+ stars), but manually scrolling through a giant Markdown file to find a weather API or a sports API with CORS support is a pain. The official JSON API they used to run went offline years ago.

So I wrote a parser to extract all 1,400+ APIs and wrapped it in a fast REST API.

You can query `/categories`, search via `/entries?category=Weather&cors=yes&auth=No`, or just hit `/random` if you need an idea for a weekend project.

It's completely free to use (1,000 req/mo limit to prevent abuse). You can grab the endpoint here:
[Link to your RapidAPI listing once published]