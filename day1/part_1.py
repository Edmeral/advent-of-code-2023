import re

sum = 0
with open("input_1", "r") as f:
    for line in f.readlines():
        s = re.sub(r"[a-zA-Z]+", "", line)
        s = s.strip()
        if len(s) == 1:
            s = f"{s}{s}"
        if len(s) > 2:
            s = f"{s[0]}{s[-1]}"
        print(int(s))
        sum = sum + int(s)
print(sum)
