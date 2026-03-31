# main.py
import pandas as pd
from analysis import run_analysis
from recommender import recommend_trip

df = pd.read_csv("india_travel_dataset.csv")

# Run analysis
run_analysis(df)

# Test recommendation
result = recommend_trip(df, 8000, "October")
print(result.head())