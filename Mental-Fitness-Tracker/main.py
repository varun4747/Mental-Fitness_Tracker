from models import UserRecord
from analytics import WellnessAnalytics
from storage import DataStorage

def main():
    storage = DataStorage()
    analytics = WellnessAnalytics()

    while True:
        print("\n--- Mental Fitness Tracker ---")
        print("1. Add Record")
        print("2. View Report")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            mood = int(input("Mood (1-10): "))
            stress = int(input("Stress (1-10): "))
            sleep = int(input("Sleep (1-10): "))

            record = UserRecord(name, mood, stress, sleep)
            record.calculate_wellness_score()

            storage.save_record(record)
            print("Record saved successfully!")

        elif choice == "2":
            records = storage.load_records()
            analytics.generate_report(records)

        elif choice == "3":
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()