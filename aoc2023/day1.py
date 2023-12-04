with open("day1_input.txt") as f:
    lines = f.readlines()

replacements = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_calibration_value(line: str) -> int:
    line = line.strip()

    first_digit = ""
    last_digit = ""

    for i in range(len(line)):
        the_line_so_far = line[: i + 1]
        digit = None

        for key, value in replacements.items():
            if the_line_so_far.endswith(key):
                digit = value
                break

        if digit:
            first_digit = first_digit or digit
            last_digit = digit

    return int(first_digit + last_digit)


the_answer = sum(get_calibration_value(line) for line in lines)
print(the_answer)
