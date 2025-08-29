import pandas as pd
import json
import os

def transform_movies():
    with open("../data/movies_raw.json", "r") as f:
        movies = json.load(f)

    df = pd.DataFrame(movies)
    df = df[["Title", "Year", "Genre", "imdbRating", "Director"]]
    df["imdbRating"] = pd.to_numeric(df["imdbRating"], errors="coerce")

    os.makedirs("../data", exist_ok=True)
    df.to_csv("../data/movies_clean.csv", index=False)
    print("✅ Transformed and saved to data/movies_clean.csv")

if __name__ == "__main__":
    transform_movies()
