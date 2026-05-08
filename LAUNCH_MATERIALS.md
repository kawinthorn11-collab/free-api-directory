# Launch Materials: Free API Directory

## Platform 1: Reddit
### r/webdev, r/reactjs, r/nextjs, r/javascript

**Title:** I got tired of scrolling the "Public APIs" repo, so I turned all 1,460+ free APIs into a searchable JSON REST API.

**Body:**
Hey guys, 

The `public-apis` repo on GitHub is amazing (it has over 400k stars), but manually scrolling through a giant Markdown file to find a weather API or a sports API with CORS support is a pain. The official JSON API they used to run went offline years ago.

So I wrote a parser to extract all 1,460+ APIs across 51 categories and wrapped it in a fast REST API.

You can query `/categories`, search via `/entries?category=Weather&cors=yes&auth=No` (perfect for frontend-only React/Next.js projects where you don't want to mess with API keys), or just hit `/random` if you need an idea for a weekend project or hackathon.

It's completely free to use (1,000 req/mo limit to prevent abuse). You can grab the endpoint here:
https://rapidapi.com/kawinthorn11collab/api/free-api-directory-api

Let me know what you think or if you build anything cool with it!

---

## Platform 2: Indie Hackers & Dev.to

**Title:** Launching a REST wrapper for the famous 400k+ star "Public APIs" GitHub repo.

**Body:**
Hi everyone,

One of the biggest hurdles when spinning up a quick weekend project or testing a new frontend framework is finding dummy data or a quick API to consume without signing up for 10 different developer accounts.

The `public-apis` GitHub repository is the gold standard for this, but their official JSON API died a long time ago, leaving only a massive Markdown file to parse.

I built a wrapper that pulls all 1,460+ APIs into a searchable, filterable REST API. You can filter by:
*   Category (e.g., Finance, Weather, Sports, Machine Learning)
*   Auth type (OAuth, apiKey, or "No" auth required)
*   HTTPS support
*   CORS support (Yes/No/Unknown)

You can check it out and use the free tier here: https://rapidapi.com/kawinthorn11collab/api/free-api-directory-api

I'm hoping this makes building hackathon projects and tutorials just a little bit faster. Cheers!

---

## Platform 3: Twitter / X
**Thread:**

1/ 🚀 I just launched a searchable JSON REST API for the famous 400k+ star "Public APIs" GitHub repo.

Instead of scrolling a giant markdown file, you can now search 1,460+ free APIs programmatically. 

Link below 👇

2/ Features:
🔍 51 Categories (Weather, Sports, Crypto, AI, etc.)
🛡️ Filter by Auth (`apiKey`, `OAuth`, `No`)
🌐 Filter by HTTPS & CORS (`yes`, `no`)
🎲 A `/random` endpoint for hackathon ideas!

3/ It's perfect for frontend developers (React, Vue, Next.js) looking for quick dummy data or `No Auth` APIs that support CORS right out of the box.

Get your free endpoint access here: https://rapidapi.com/kawinthorn11collab/api/free-api-directory-api #buildinpublic #webdev #100DaysOfCode #javascript