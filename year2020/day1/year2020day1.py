"""
--- Day 1: Report Repair ---

After saving Christmas five years in a row, you've decided to take a vacation at a nice
resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used
there have a little picture of a starfish; the locals just call them stars. None of the
currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of
these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the
Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle
grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense report (your
puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to year2020 and then multiply those
two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456

In this list, the two entries that sum to year2020 are 1721 and 299. Multiplying them together
produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to year2020; what
do you get if you multiply them together?

--- Part Two ---

The Elves in accounting are thankful for your help; one of them even offers you a starfish
coin they had left over from a past vacation. They offer you a second one if you can find
three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to year2020 are 979, 366, and 675.
Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to year2020?
"""
from itertools import permutations
from os.path import dirname, relpath, join
from typing import List

from common import read_input, time_it


def solve_via_brute_force(list_of_numbers: List[int]) -> int:
    """Tries every combination of numbers, the first that adds up to year2020 will be returned."""
    for a in list_of_numbers:
        for b in list_of_numbers:
            if a + b == 2020:
                return a * b


def solve_via_brute_force2(list_of_numbers: List[int]) -> int:
    """Tries every combination of numbers, the first that adds up to year2020 will be returned."""
    for a in list_of_numbers:
        for b in list_of_numbers:
            for c in list_of_numbers:
                if a + b + c == 2020:
                    return a * b * c


def solve_via_early_break_loops(list_of_numbers: List[int]) -> int:
    """Tries every combination of numbers, the first that adds up to year2020 will be returned."""

    sorted_list_of_numbers = sorted(list_of_numbers)

    for a in sorted_list_of_numbers:
        for b in sorted_list_of_numbers:
            if a + b == 2020:
                return a * b
            elif a + b > 2020:
                break


def solve_via_dict(list_of_numbers: List[int]) -> int:
    """Puts the values into a dict and then loop over the list only once trying to access
    the missing number directly. If the missing number is not a key simply continue."""

    choices = {val: val for val in list_of_numbers}

    for val in list_of_numbers:
        try:
            return choices[2020 - val] * val
        except KeyError:
            continue


def solve_via_dict2(list_of_numbers: List[int]) -> int:
    """Puts the values into a dict and then loop over the list only once trying to access
    the missing number directly. If the missing number is not a key simply continue."""

    choices = {val: val for val in list_of_numbers}

    for val in list_of_numbers:
        if 2020 - val in choices:
            return choices[2020 - val] * val


def solve_via_dict3(list_of_numbers: List[int]) -> int:
    """Puts the values into a dict and then loop over the list only once trying to access
    the missing number directly. If the missing number is not a key simply continue."""

    choices = {val: val for val in list_of_numbers}

    for val in list_of_numbers:
        a = choices.get(2020 - val)
        if a:
            return a * val


def solve_via_dict3_walrus(list_of_numbers: List[int]) -> int:
    """Puts the values into a dict and then loop over the list only once trying to access
    the missing number directly. If the missing number is not a key simply continue."""

    choices = {val: val for val in list_of_numbers}

    for val in list_of_numbers:
        if a := choices.get(2020 - val):
            return a * val


def solve_via_itertools_permutations(list_of_numbers: List[int]) -> int:
    """Uses the itertools to create all permutations."""

    all_permutations = permutations(list_of_numbers, 2)

    for a, b in all_permutations:
        if a + b == 2020:
            return a * b


if __name__ == "__main__":
    """
    Execution of solve_via_brute_force() took 0.7853507995605469ms
    Execution of solve_via_early_break_loops() took 0.10275840759277344ms
    Execution of solve_via_dict() took 0.051021575927734375ms
    Execution of solve_via_dict2() took 0.024080276489257812ms
    Execution of solve_via_dict3() took 0.029087066650390625ms
    Execution of solve_via_dict3_walrus() took 0.025987625122070312ms
    Execution of solve_via_itertools_permutations() took 1.035928726196289ms

    Note that some results are quite sensitive to the order of the list. Nevertheless solve_via_dict2()
    is the fasted solution i could find for any random order of the input list.
    """

    day1_input = read_input(join(relpath(dirname(__file__)), "input.txt"), int)

    with time_it("solve_via_brute_force()"):
        solution_brute_force = solve_via_brute_force(day1_input)

    # this is about 8x times faster than brute force
    with time_it("solve_via_early_break_loops()"):
        solution_early_break_loops = solve_via_early_break_loops(day1_input)

    # this is about 16x faster than the brute for attempt
    with time_it("solve_via_dict()"):
        solution_dict = solve_via_dict(day1_input)

    # this is about 23x faster than the brute for attempt
    with time_it("solve_via_dict2()"):
        solution_dict2 = solve_via_dict2(day1_input)

    # this is about 23x faster than the brute for attempt
    with time_it("solve_via_dict3()"):
        solution_dict3 = solve_via_dict3(day1_input)

    # this is about 23x faster than the brute for attempt
    with time_it("solve_via_dict3_walrus()"):
        solution_dict3_walrus = solve_via_dict3_walrus(day1_input)

    # this is about 1.3x slower than the brute for attempt
    with time_it("solve_via_itertools_permutations()"):
        solution_permutation = solve_via_itertools_permutations(day1_input)

    assert solution_early_break_loops == solution_brute_force
    assert solution_dict == solution_brute_force
    assert solution_dict2 == solution_brute_force
    assert solution_dict3 == solution_brute_force
    assert solution_dict3_walrus == solution_brute_force
    assert solution_permutation == solution_brute_force

    print(f"Solution of Day 1 - Part 1 is " f"'{solution_brute_force}'")
    print(f"Solution of Day 1 - Part 2 is " f"'{solve_via_brute_force2(day1_input)}'")
