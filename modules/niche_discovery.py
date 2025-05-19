import random
import requests

def get_niche(seed_keywords):
    keyword = random.choice(seed_keywords)
    suggestions = fetch_youtube_autocomplete(keyword)
    return random.choice(suggestions) if suggestions else keyword

def fetch_youtube_autocomplete(keyword):
    try:
        url = f"https://suggestqueries.google.com/complete/search?client=firefox&ds=yt&q={keyword}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data[1]
    except Exception as e:
        print("Autocomplete error:", e)
    return []
