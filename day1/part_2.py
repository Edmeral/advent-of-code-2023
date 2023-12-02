import re

sum = 0
mapping = {
    "one": "one1e",
    "two": "tw2o",
    "three": "thre3e",
    "four": "fou4r",
    "five": "fiv5e",
    "six": "si6x",
    "seven": "seve7n",
    "eight": "eigh8t",
    "nine": "nin9e",
}
with open("input_2", "r") as f:
    for line in f.readlines():
        s = line.strip()
        digits = []
        for letters, digit in mapping.items():
            s = s.replace(letters, digit)
        print(s)
        s = re.sub(r"[a-zA-Z]+", "", s)
        if len(s) == 1:
            s = f"{s}{s}"
        if len(s) > 2:
            s = f"{s[0]}{s[-1]}"
        sum = sum + int(s)
print(sum)
