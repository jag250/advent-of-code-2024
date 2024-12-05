import click
import importlib
from datetime import datetime
from zoneinfo import ZoneInfo

from advent_of_code_2024.get_data import add_data_to_file
import aocd

def dynamic_import_day(day):
    try:
        module = importlib.import_module(f'advent_of_code_2024.day{day}.day{day}')
        return getattr(module, f'day{day}')
    except (ImportError, AttributeError) as e:
        click.echo(f"Error importing day{day} function: {e}")
        return None

@click.command()
@click.argument("part", type=click.IntRange(min=1, max=2))
@click.argument("day", type=click.IntRange(min=1, max=25), default=lambda: datetime.now(ZoneInfo("America/New_York")).day)
@click.option("-s", "--submit", is_flag=True, default=False)
def main(part: int, day: int, submit: bool):
    add_data_to_file(day=day)
    sol = dynamic_import_day(day)(part)
    print(sol)

    part_num_to_string = {1:"a", 2:"b"}
    if sol and submit:
        print("Submitting...")
        aocd.submit(sol, part=part_num_to_string[part], day=day, year=2024)

