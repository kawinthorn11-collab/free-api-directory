# Asset #2 Research: Free API Directory (Web App & JSON Endpoint)

## The Opportunity
- **Target Asset**: `public-apis` (https://github.com/public-apis/public-apis)
- **Description**: The most famous curated list of free APIs for software and web development (over 400,000+ stars).
- **Why it matters**: Currently, it is just a massive Markdown file (`README.md`). Developers have to manually scroll through thousands of lines to find a weather API or a sports API. 
- **The Gap**: The official JSON API that used to power this repository went offline years ago.
- **License**: MIT License (Commercial use permitted).

## The Execution Path (Zero-Cost)
1. Write a Python script to parse the `README.md` from the `public-apis` repo and convert the Markdown tables into a clean, searchable SQLite database or JSON file.
2. Wrap this data in a fast FastAPI backend.
3. Add search endpoints: `/search?category=weather` or `/random`.
4. Deploy the backend to Vercel for free.
5. Monetize: Offer the JSON API on RapidAPI (Freemium model, just like Asset #1).

## Legal & Risk Check
- **Legality**: The dataset is explicitly licensed under MIT. Repackaging a Markdown file into a searchable JSON API is fully permitted.
- **Risk**: Very low. It requires zero authentication, zero web scraping, and zero external rate limits. 

## Next Step Verification
I will write the parser script locally to prove I can extract the structured data from the Markdown file and convert it to JSON.