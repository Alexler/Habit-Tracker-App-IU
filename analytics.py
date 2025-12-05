# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774


"""
Analytics Module
This module contains functional programming logic to analyze habit data.
It calculates streaks and filters habits based on user criteria.
"""


def get_all_habits(habit_list):
    """
    Returns a list of all currently tracked habits.
    """
    return habit_list


def get_habits_by_periodicity(habit_list, period):
    """
    Returns a list of habits filtered by their recurrence period.
    :param period: String, either 'daily' or 'weekly'
    """
    found_habits = []
    for habit in habit_list:
        if habit.recurrence == period:
            found_habits.append(habit)

    return found_habits

def get_longest_streak_all(habit_list):
    """
    Iterates through all habits and returns the single highest streak count found.
    """
    longest_streak = 0
    for habit in habit_list:
        current_streak = habit.get_habit_streak()
        if current_streak > longest_streak:
            longest_streak = current_streak
    return longest_streak

def get_longest_streak_for_habit(habit_list, habit_name):
    """
    Returns the longest streak for a specific habit identified by its name.
    """
    longest_streak = 0
    for habit in habit_list:
        if habit.name == habit_name:
            longest_streak = habit.get_habit_streak()
    return longest_streak