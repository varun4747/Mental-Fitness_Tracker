class WellnessAnalytics:

    def generate_report(self, records):
        if not records:
            print("No data available.")
            return

        total_score = 0
        high_stress_days = 0

        for record in records:
            print(f"\nName: {record['name']}")
            print(f"Mood: {record['mood']}")
            print(f"Stress: {record['stress']}")
            print(f"Sleep: {record['sleep']}")
            print(f"Wellness Score: {record['wellness_score']}")
            print(f"Category: {record['category']}")

            total_score += record['wellness_score']
            if record['stress'] >= 7:
                high_stress_days += 1

        avg_score = total_score / len(records)

        print("\n--- Analytical Summary ---")
        print(f"Average Wellness Score: {round(avg_score, 2)}")
        print(f"High Stress Days: {high_stress_days}")

        if avg_score < 5:
            print("Insight: Overall wellness needs improvement.")
        else:
            print("Insight: Overall wellness is stable.")