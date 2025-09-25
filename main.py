# App = Habit Tracker App
# Name = Alexander Lerch
# Matrikelnr. = IU14130774

#Scope of this part:
# The main app file for handling interactions by the user and the single app components

import click
from tracker import Tracker
from analytics import get_habits_by_periodicity, get_longest_streak_all, get_longest_streak_for_habit


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count, name):
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()