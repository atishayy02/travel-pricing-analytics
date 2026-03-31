import pandas as pd
import random

columns = [
    "destination", "month", "trip_duration",
    "stay_cost", "transport_cost", "food_cost", "activity_cost",
    "availability", "rating", "total_cost"
]

destinations = {
    "Coorg": "Hill",
    "Ooty": "Hill",
    "Manali": "Hill",
    "Goa": "Beach",
    "Gokarna": "Beach",
    "Rishikesh": "Adventure"
}


months = ["January", "March", "May", "June", "July", "October", "December"]

data = []

for _ in range(120):  # number of rows
    dest = random.choice(list(destinations.keys()))
    month = random.choice(months)
    
    # Trip duration
    trip_duration = random.choice([2, 3, 4, 5])
    
    # Stay cost (India realistic)
    if dest in ["Coorg", "Ooty", "Gokarna"]:
        stay_cost = random.randint(1000, 2500)
    elif dest == "Goa":
        stay_cost = random.randint(2000, 4000)
    else:  # Manali, Rishikesh
        stay_cost = random.randint(1500, 3500)
    
    # Transport cost (assuming Bangalore origin)
    if dest in ["Coorg", "Ooty"]:
        transport_cost = random.randint(800, 2000)
    elif dest in ["Goa", "Gokarna"]:
        transport_cost = random.randint(1500, 3000)
    else:
        transport_cost = random.randint(3000, 6000)
    
    # Food cost
    food_cost = trip_duration * random.randint(500, 900)
    
    # Activity cost
    if dest == "Rishikesh":
        activity_cost = random.randint(1000, 2500)  # rafting
    elif dest == "Manali":
        activity_cost = random.randint(800, 2000)  # skiing/paragliding
    else:
        activity_cost = random.randint(500, 1500)
    
    # Availability logic (India-specific)
    availability = 1
    if dest == "Manali" and month in ["July"]:
        availability = 0
    if dest == "Goa" and month in ["July"]:
        availability = 0
    
    # Rating logic
    if dest == "Manali" and month in ["December", "January"]:
        rating = round(random.uniform(4.5, 5.0), 1)
    elif dest == "Coorg" and month in ["July"]:
        rating = round(random.uniform(4.3, 4.8), 1)
    else:
        rating = round(random.uniform(3.8, 4.5), 1)
    
    # Total cost
    total_cost = (
        stay_cost * trip_duration +
        transport_cost +
        food_cost +
        activity_cost
    )
    
    data.append([
        dest, month, trip_duration,
        stay_cost, transport_cost, food_cost, activity_cost,
        availability, rating, total_cost
    ])

df = pd.DataFrame(data, columns=[
    "destination", "month", "trip_duration",
    "stay_cost", "transport_cost", "food_cost", "activity_cost",
    "availability", "rating", "total_cost"
])

df.to_csv("india_travel_dataset.csv", index=False)

df.head()