# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774

"""
Test Module

This module contains unit tests for the core logic of the Habit Tracker.
It uses the `pytest` framework to verify that streak calculations
work correctly for both daily and weekly habits, including edge cases.
"""

from habit import Habit
import datetime

def test_daily_streak():
    """
    Verifies that a daily habit correctly calculates a streak of 3
    when completed on 3 consecutive days (today, yesterday, day before).
    """
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
    """
    Verifies that a daily streak is reset if a day is skipped.
    Scenario: Completed today and 2 days ago.
    Expected Result: Streak should be 1 (only today counts).
    """

    habit = Habit("Test Broken Daily", "A test habit", "daily")

    today = datetime.datetime.now()
    day_before_yesterday = today - datetime.timedelta(days=2)

    habit.completed.append(day_before_yesterday)
    habit.completed.append(today)

    streak = habit.get_habit_streak()

    assert streak == 1

def test_weekly_streak():
    """
    Verifies that a weekly habit correctly calculates a streak of 2
    when completed in two consecutive weeks (today and 6 days ago).
    """

    habit = Habit("Test Weekly", "A weekly habit", "weekly")

    today = datetime.datetime.now()
    six_days_ago = today - datetime.timedelta(days=6)

    habit.completed.append(six_days_ago)
    habit.completed.append(today)

    streak = habit.get_habit_streak()

    assert streak == 2

def test_broken_weekly_streak():
    """
    Verifies that a weekly streak is reset if more than 7 days pass.
    Scenario: Completed today and 8 days ago (gap > 7 days).
    Expected Result: Streak should be 1.
    """
    habit = Habit("Test Broken Weekly", "A weekly habit", "weekly")

    today = datetime.datetime.now()
    eight_days_ago = today - datetime.timedelta(days=8)

    habit.completed.append(eight_days_ago)
    habit.completed.append(today)

    streak = habit.get_habit_streak()

    assert streak == 1