import json

class DataStorage:
    def __init__(self):
        self.file = "data.json"

    def save_record(self, record):
        try:
            with open(self.file, "r") as f:
                data = json.load(f)
        except:
            data = []

        data.append({
            "name": record.name,
            "mood": record.mood,
            "stress": record.stress,
            "sleep": record.sleep,
            "wellness_score": record.wellness_score,
            "category": record.category
        })

        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def load_records(self):
        try:
            with open(self.file, "r") as f:
                return json.load(f)
        except:
            return []