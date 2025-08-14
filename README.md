# Web-Scraper-For-News-Headlines
    Automate Data collection from a public website

Web Scraper for News Headlines 📰
📌 Objective
      A simple Python script to scrape top news headlines from a public news website and store them in a .txt file.

🛠 Tools Used
    Python 3
    requests → To fetch the HTML content of the webpage.
    BeautifulSoup (bs4) → To parse HTML and extract headlines.

📂 Deliverables
    Python Script → news_scraper.py
    Output File → headlines.txt

💡 Features
    Fetches the latest headlines from a chosen news website.
    Extracts <h2> or <title> tags containing headlines.
    Saves results in headlines.txt for offline access.
    Lightweight and fast.

📋 How It Works
    Fetch HTML → Use requests.get() to retrieve the page.
    Parse HTML → Use BeautifulSoup to extract headlines.
    Store Headlines → Save the extracted headlines to headlines.txt.

🚀 Installation & Usage
    # 1️⃣ Install dependencies
      pip install requests beautifulsoup4

    # 2️⃣ Run the scraper
      python news_scraper.py

📄 Example Output (headlines.txt)
    1. Breaking News: Example headline one
    2. Government announces new policy
    3. Sports: Team wins championship

⚠️ Note
    This project is for educational purposes only.
    Always check a website’s robots.txt before scraping.
    Avoid sending too many requests to prevent server overload.
