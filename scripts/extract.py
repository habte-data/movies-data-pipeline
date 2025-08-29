import requests
import json
import os

API_KEY = "5031fd6"  # Replace with your OMDb API key
MOVIES = ["Inception", "Titanic", "Avatar", "Interstellar", "The Dark Knight"]

def extract_movies():
    results = []
    for movie in MOVIES:
        url = f"http://www.omdbapi.com/?t={movie}&apikey={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            results.append(response.json())
    os.makedirs("../data", exist_ok=True)
    with open("../data/movies_raw.json", "w") as f:
        json.dump(results, f, indent=4)
    print("✅ Extracted and saved to data/movies_raw.json")

if __name__ == "__main__":
    extract_movies()