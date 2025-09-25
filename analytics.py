# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774

#Scope of this part:
#Here are all the functions to analyze the habit data.


def get_all_habits(habit_list):
    return habit_list


def get_habits_by_periodicity(habit_list, period):

    found_habits = []
    for habit in habit_list:
        if habit.recurrence == period:
            found_habits.append(habit)

    return found_habits

def get_longest_streak_all(habit_list):
    longest_streak = 0
    for habit in habit_list:
        current_streak = habit.get_habit_streak()
        if current_streak > longest_streak:
            longest_streak = current_streak
    return longest_streak

def get_longest_streak_for_habit(habit_list, habit_name):
    longest_streak = 0
    for habit in habit_list:
        if habit.name == habit_name:
            longest_streak = habit.get_habit_streak()
    return longest_streak

