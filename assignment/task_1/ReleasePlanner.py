from dataclasses import dataclass
from typing import List, Tuple
import os


@dataclass
class Release:
    start_day: int
    end_day: int


def parse_input_file(input_file: str) -> List[Tuple[int, int]]:
    pairs = []
    with open(input_file, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) != 2:
                raise ValueError(f"Invalid format: '{line.strip()}'")
            try:
                start_day = int(parts[0])
                duration = int(parts[1])
            except ValueError:
                raise ValueError(f"Non-integer value found: '{line.strip()}'")
            pairs.append((start_day, duration))
    return pairs


def select_max_releases(pairs: List[Tuple[int, int]]) -> List[Release]:
    releases = [
        Release(start_day=start_day, end_day=start_day + duration - 1)
        for start_day, duration in pairs
        if start_day + duration - 1 <= 10
    ]

    sorted_releases = sorted(releases, key=lambda r: r.end_day)

    selected_releases = []
    last_end_day = 0
    for release in sorted_releases:
        if release.start_day > last_end_day:
            selected_releases.append(release)
            last_end_day = release.end_day

    return selected_releases


def write_output_file(output_file: str, selected_releases: List[Release]) -> None:
    with open(output_file, 'w') as file:
        file.write(f"{len(selected_releases)}\n")
        for release in selected_releases:
            file.write(f"{release.start_day} {release.end_day}\n")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, '../resources', 'releases.txt')
    output_file = os.path.join(script_dir, '../resources', 'solution.txt')

    pairs = parse_input_file(input_file)
    selected_releases = select_max_releases(pairs)
    write_output_file(output_file, selected_releases)


if __name__ == "__main__":
    main()