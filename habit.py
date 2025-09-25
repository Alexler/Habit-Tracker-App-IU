# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774

#Scope of this part:
#This is the Habit class that will be trackable by the user


import datetime

class Habit:
    def __init__(self, name: str, description: str, recurrence: str):
        # initialization of a new habit // construtcor
        self.name = name
        self.description = description
        self.recurrence = recurrence

        self.create_time = datetime.datetime.now()
        self.completed = []

    def complete_habits(self):
        #a habit will be marked as completed here
        self.completed.append(datetime.datetime.now())

    def get_habit_streak(self):
        # calculates the streak based on the habit's recurrence
        streaks_sorted = sorted(self.completed, reverse=True)

        streak = 0
        today = datetime.datetime.now().date()
        recent_streak = streaks_sorted[0].date()

        if self.recurrence == "daily":
            if (today - recent_streak).days > 1:
                return 0
        elif self.recurrence == "weekly":
            if (today - recent_streak).days > 7:
                return 0
        streak = 1

        for i in range(len(streaks_sorted) - 1):
            current_date = streaks_sorted[i].date()
            previous_date = streaks_sorted[i + 1].date()
            day_difference = (current_date - previous_date).days

            if self.recurrence == "daily":
                if day_difference == 1:
                    streak += 1
                elif day_difference == 0:
                    continue
                else:
                    break

            elif self.recurrence == "weekly":
                if day_difference <= 7:
                    streak += 1
                else:
                    break
        return streak



