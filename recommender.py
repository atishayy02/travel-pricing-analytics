# recommender.py

def recommend_trip(df, budget, month):
    filtered = df[
        (df['total_cost'] <= budget) &
        (df['month'] == month) &
        (df['availability'] == 1)
    ]
    
    return filtered.sort_values(by='rating', ascending=False)