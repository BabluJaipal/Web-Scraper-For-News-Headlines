# news_scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_headlines(url, output_file):
    try:
        # Fetch the HTML content
        response = requests.get(url)
        response.raise_for_status()  # Raise error if request fails

        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract headlines (you can change the tag/class based on website structure)
        headlines = soup.find_all('h2')  # Example: many news sites use <h2> for headlines

        # Save to file
        with open(output_file, 'w', encoding='utf-8') as file:
            for i, headline in enumerate(headlines, start=1):
                text = headline.get_text(strip=True)
                if text:  # Avoid empty headlines
                    file.write(f"{i}. {text}\n")

        print(f"✅ Headlines scraped and saved to '{output_file}'")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Example: BBC News (you can replace with another news site)
    news_url = "https://www.bbc.com/news"
    # news_url = "https://timesofindia.indiatimes.com/"
    output_filename = "headlines.txt"

    scrape_headlines(news_url, output_filename)
