# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774

#Scope of this part:
# The main app file for handling interactions by the user and the single app components

import click
from tracker import Tracker
from analytics import get_habits_by_periodicity, get_longest_streak_all, get_longest_streak_for_habit

tracker = Tracker("Tracker_DB")

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
@click.option('--description', default="No description", help='A short description of the habit.')
@click.option('--recurrence', type=click.Choice(['daily', 'weekly'], case_sensitive=False), default='daily', help='How often will this habit reocurre? (daily/weekly).')
def add(name, description, recurrence):
    tracker.save_habits_to_db(name, description, recurrence)
    click.echo("Habit "+{name}+" was added.")

@cli.command()
@click.argument('name')
def complete(name):
    tracker.complete_habits(name)
    click.echo("Habit "+{name}+" was marked as complete.")


@cli.command(name="list")
def list_habits():
    if not tracker.habits:
        click.echo("You have no habits yet.")
        return

    click.echo("--- All habits ---")
    for habit in tracker.habits:
        streak = habit.get_habit_streak()
        click.echo("- "+{habit.name}+" "+({habit.recurrence}), "current streak: "+{streak})

cli()