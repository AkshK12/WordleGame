with open("./words_alpha.txt") as f:
    lines = f.readlines()
filtered_lines = filter(
    lambda x:  len(x.strip()) == 5,
    lines
)
filtered_lines = list(filtered_lines)
with open("./5words_alpha.txt","w+") as f:
    for line in filtered_lines:
        f.write(line)
