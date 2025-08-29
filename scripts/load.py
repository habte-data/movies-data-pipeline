import pandas as pd
from sqlalchemy import create_engine

def load_movies():
    df = pd.read_csv("../data/movies_clean.csv")
    engine = create_engine("sqlite:///../data/movies.db")
    df.to_sql("movies", engine, if_exists="replace", index=False)
    print("✅ Loaded into SQLite database (data/movies.db)")

if __name__ == "__main__":
    load_movies()