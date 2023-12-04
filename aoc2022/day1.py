with open("2022_1.txt") as f:
    input_lines = f.readlines()

calories_by_elf = []
running_total = 0

for line in input_lines:
    line = line.strip()
    if line:
        running_total += int(line)
    else:
        calories_by_elf.append(running_total)
        running_total = 0

if running_total:
    calories_by_elf.append(running_total)

top_3 = sorted(calories_by_elf, reverse=True)[:3]

print(f"{sum(top_3)=}")
