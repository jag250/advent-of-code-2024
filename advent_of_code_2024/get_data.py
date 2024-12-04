import os
from pathlib import Path

from aocd import get_data
from aocd.exceptions import PuzzleLockedError

BASE_PATH = Path("advent_of_code_2024")

def add_data_to_file(day: int, year: int = 2024):
    day_directory = BASE_PATH / Path(f"day{day}")
    if not day_directory.exists():
        os.mkdir(day_directory)

    path_to_file = day_directory / Path(f"day{day}.txt")
    if not path_to_file.exists() or os.stat(path=path_to_file).st_size == 0:
        with open(path_to_file, "w") as f:
            try:
                f.write(get_data(day=day, year=year))

            except PuzzleLockedError as e:
                print(e)