# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774

#Scope of this part:
#This is the Habit class that will be trackable by the user


import datetime

class Habit:
    """
    Represents a single user habit with tracking capabilities.
    Stores metadata (name, description) and a history of completion events.
    """
    def __init__(self, name: str, description: str, recurrence: str):
        """
        Initializes a new habit instance.
        :param name: The unique name of the habit.
        :param description: A brief description of the task.
        :param recurrence: The frequency of the habit ('daily' or 'weekly').
        """
        self.name = name
        self.description = description
        self.recurrence = recurrence

        self.create_time = datetime.datetime.now()
        self.completed = []

    def complete_habits(self):
        """
        Marks the habit as completed by appending the current timestamp to the log.
        """
        self.completed.append(datetime.datetime.now())

    def get_habit_streak(self):
        """
        Calculates the current streak based on the habit's recurrence policy.
        Checks if the chain of completion is unbroken based on the specific
        rules for 'daily' (gap > 1 day) or 'weekly' (gap > 7 days).
        :return: Integer representing the count of consecutive periods.
        """

        if not self.completed:
            return 0

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