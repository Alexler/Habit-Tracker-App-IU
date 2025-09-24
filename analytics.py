# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774

#Scope of this part:
#Here are all the functions to analyze the habit data.


def get_all_habits(habit_list):
    return habit_list


def get_habits_by_periodicity(habit_list, period):

    gefundene_habits = []
    for habit in habit_list:
        if habit.recurrence == period:
            gefundene_habits.append(habit)

    return gefundene_habits