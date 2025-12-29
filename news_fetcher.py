import requests

API_KEY = "YOUR_NEWSAPI_KEY"
BASE_URL = "https://newsapi.org/v2/top-headlines"

def get_news(country="us", category=None, page_size=5):
    params = {"apiKey": API_KEY, "country": country, "pageSize": page_size}
    if category:
        params["category"] = category
    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        if response.status_code == 200:
            articles = response.json().get("articles", [])
            return [f"{a['title']} ({a['source']['name']})" for a in articles]
        else:
            return [f"Error fetching news: {response.status_code}"]
    except Exception as e:
        return [f"Exception occurred: {str(e)}"]
