# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774

#Scope of this part:
# The main app file for handling interactions by the user and the single app components

"""
Main Application Module

This module serves as the entry point for the Command Line Interface (CLI).
It uses the `click` library to define commands and sub-commands that allow
the user to interact with the underlying Tracker logic.
"""

import click
from tracker import Tracker
from analytics import get_habits_by_periodicity, get_longest_streak_all, get_longest_streak_for_habit

tracker = Tracker("Tracker_DB")

@click.group()
def cli():
    """
    Habit Tracker CLI interface.
    Use this tool to add, track, and analyze your habits.
    """
    pass

@cli.command()
@click.argument('name')
@click.option('--description', default="No description", help='A short description of the habit.')
@click.option('--recurrence', type=click.Choice(['daily', 'weekly'], case_sensitive=False), default='daily', help='How often will this habit reocurre? (daily/weekly).')
def add(name, description, recurrence):
    """
    Command to add a new habit to the tracker.
    :param name: The unique name of the habit (e.g., 'exercise').
    :param description: Optional details about the habit.
    :param recurrence: Frequency of the habit ('daily' or 'weekly').
    """
    tracker.save_habits_to_db(name, description, recurrence)
    click.echo("Habit "+name+" was added.")

@cli.command()

@click.argument('name')

def complete(name):
    """
    Command to mark a habit as completed for the current period.
    :param name: The name of the habit to check off.
    """
    tracker.complete_habits(name)
    click.echo("Habit "+name+" was marked as complete.")

@cli.command(name="list")

def list_habits():
    """
    Command to list all currently tracked habits and their current streaks.
    """
    if not tracker.habits:
        click.echo("You have no habits yet.")
        return
    click.echo("--- All habits ---")
    for habit in tracker.habits:
        streak = habit.get_habit_streak()
        click.echo("- "+str(habit.name)+" "+str(habit.recurrence)+" current streak: "+str(streak))

@cli.group()
def analyze():
    """
    Command group for analysis tasks.
    Use 'analyze all', 'analyze habit', or 'analyze period'.
    """
    pass

@analyze.command(name="all")
def analyze_all():
    """
    Calculates and displays the longest streak ever achieved across ALL habits.
    """
    longest_streak = get_longest_streak_all(tracker.habits)
    click.echo("The longest streak of all habits: "+ str(longest_streak))

@analyze.command(name="habit")
@click.argument('name')
def analyze_habit(name):
    """
    Calculates and displays the longest streak for a specific habit.
    :param name: The name of the habit to analyze.
    """
    streak = get_longest_streak_for_habit(tracker.habits, name)
    click.echo("The longest streak for "+ name +" is: "+ str(streak))

@analyze.command(name="period")
@click.argument('period_type', type=click.Choice(['daily', 'weekly'], case_sensitive=False))
def analyze_period(period_type):
    """
    Lists all habits that match a specific periodicity (daily or weekly).
    :param period_type: The type of recurrence to filter by.
    """
    habits = get_habits_by_periodicity(tracker.habits, period_type)
    click.echo("--- All "+period_type+" habits ---")
    for habit in habits:
        click.echo("- "+habit.name)

cli.add_command(analyze)

if __name__ == '__main__':
    cli()

