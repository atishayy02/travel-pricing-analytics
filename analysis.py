# analysis.py
import matplotlib.pyplot as plt

def run_analysis(df):
    # Monthly cost
    monthly_cost = df.groupby('month')['total_cost'].mean()
    print("\nMonthly Cost:\n", monthly_cost)

    monthly_cost.plot(kind='line', marker='o', title="Monthly Cost Trend")
    plt.show()

    # Destination cost
    dest_cost = df.groupby('destination')['total_cost'].mean()
    print("\nDestination Cost:\n", dest_cost)

    # Cost breakdown
    cost_breakdown = df[['stay_cost','transport_cost','food_cost','activity_cost']].mean()
    print("\nCost Breakdown:\n", cost_breakdown)