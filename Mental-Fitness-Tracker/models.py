class UserRecord:
    def __init__(self, name, mood, stress, sleep):
        self.name = name
        self.mood = mood
        self.stress = stress
        self.sleep = sleep
        self.wellness_score = 0
        self.category = ""

    def calculate_wellness_score(self):
        self.wellness_score = round((self.mood * 0.4) +
                                    (self.sleep * 0.4) -
                                    (self.stress * 0.2), 2)

        if self.wellness_score >= 7:
            self.category = "Good"
        elif self.wellness_score >= 4:
            self.category = "Moderate"
        else:
            self.category = "Needs Attention"