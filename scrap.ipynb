import requests
from bs4 import BeautifulSoup
import json
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

event_urls = [
    'https://www.ces.tech']

def scrape_event_data(url):
    try:
        response = requests_retry_session().get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()  # Raise an error for bad status codes
        soup = BeautifulSoup(response.content, 'html.parser')

        event_data = {}
        event_data['Event Name'] = soup.find('title').text.strip() if soup.find('title') else 'N/A'
        event_data['Event Date(s)'] = soup.find('meta', {'name': 'date'})['content'] if soup.find('meta', {'name': 'date'}) else 'N/A'
        event_data['Location'] = soup.find('meta', {'name': 'location'})['content'] if soup.find('meta', {'name': 'location'}) else 'N/A'
        event_data['Website URL'] = url
        event_data['Description'] = soup.find('meta', {'name': 'description'})['content'] if soup.find('meta', {'name': 'description'}) else 'N/A'
        event_data['Key Speakers'] = [speaker.text.strip() for speaker in soup.find_all('div', class_='speaker-name')] if soup.find_all('div', class_='speaker-name') else 'N/A'
        event_data['Agenda/Schedule'] = [schedule.text.strip() for schedule in soup.find_all('div', class_='schedule-item')] if soup.find_all('div', class_='schedule-item') else 'N/A'
        event_data['Registration Details'] = soup.find('div', class_='registration-details').text.strip() if soup.find('div', class_='registration-details') else 'N/A'
        event_data['Pricing'] = soup.find('div', class_='pricing-details').text.strip() if soup.find('div', class_='pricing-details') else 'N/A'
        event_data['Categories'] = [category.text.strip() for category in soup.find_all('div', class_='category-item')] if soup.find_all('div', class_='category-item') else 'N/A'
        event_data['Audience type'] = soup.find('meta', {'name': 'audience'})['content'] if soup.find('meta', {'name': 'audience'}) else 'N/A'

        return event_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

events_data = []

for url in event_urls:
    event_data = scrape_event_data(url)
    if event_data:
        events_data.append(event_data)
    time.sleep(2) 
with open('events_data.json', 'w') as json_file:
    json.dump(events_data, json_file, indent=4)

print("Data scraping completed. Check the events_data.json file for the scraped data.")
