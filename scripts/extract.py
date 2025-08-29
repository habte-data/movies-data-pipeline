import requests
import os
import json

# ✅ Your OMDb API key
API_KEY = "5031fd6"

# Example movie list
movies = ["Inception", "The Matrix", "Interstellar"]

# Make sure we save inside the project folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

OUTPUT_FILE = os.path.join(DATA_DIR, "movies_raw.json")

results = []

for movie in movies:
    url = f"http://www.omdbapi.com/?t={movie}&apikey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        results.append(response.json())
    else:
        print(f"Failed to fetch {movie}")

# Save JSON
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4)

print(f"✅ Extracted and saved to {OUTPUT_FILE}")
