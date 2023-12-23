import requests
from bs4 import BeautifulSoup
def web_scraper(URL):
    # Send a GET request to the specified URL
    response = requests.get(URL)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract specific data based on HTML structure
        # Replace the following lines with your own logic
        title = soup.title.text.strip()
        paragraphs = soup.find_all('p')
        paragraph_texts = [p.text.strip() for p in paragraphs]
        # Print or process the extracted data
        print(f'Title: {title}')
        print('Paragraphs:')
        for idx, text in enumerate(paragraph_texts, 1):
            print(f'{idx}. {text}')
        else:
            print(f'Error: Unable to fetch the page. Status code: {response.status_code}')
# Example usage
url_to_scrape = 'https://www.bioexplorer.net/animals/birds/'
web_scraper(url_to_scrape)
