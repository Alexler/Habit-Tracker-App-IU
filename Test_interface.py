# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774

#Scope of this part:
#this application part is for development purpose, for testing of single functions and the whole app

from habit import Habit
import datetime

def test_daily_streak():
    habit = Habit("Test Daily", "A test habit", "daily")

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    day_before_yesterday = today - datetime.timedelta(days=2)

    habit.completed.append(day_before_yesterday)
    habit.completed.append(yesterday)
    habit.completed.append(today)

    streak = habit.get_habit_streak()

    assert streak == 3


def test_broken_daily_streak():
    habit = Habit("Test Broken Daily", "A test habit", "daily")

    today = datetime.datetime.now()
    day_before_yesterday = today - datetime.timedelta(days=2)

    habit.completed.append(day_before_yesterday)
    habit.completed.append(today)

    streak = habit.get_habit_streak()

    assert streak == 1

def test_weekly_streak():
    habit = Habit("Test Weekly", "A weekly habit", "weekly")

    today = datetime.datetime.now()
    six_days_ago = today - datetime.timedelta(days=6)

    habit.completed.append(six_days_ago)
    habit.completed.append(today)

    streak = habit.get_habit_streak()

    assert streak == 2

def test_broken_weekly_streak():
    habit = Habit("Test Broken Weekly", "A weekly habit", "weekly")

    today = datetime.datetime.now()
    eight_days_ago = today - datetime.timedelta(days=8)

    habit.completed.append(eight_days_ago)
    habit.completed.append(today)

    streak = habit.get_habit_streak()

    assert streak == 1