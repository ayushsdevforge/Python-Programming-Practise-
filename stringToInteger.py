def my_atoi(s):
    s = s.strip()
    sign, num = 1, 0
    i = 0

    if i < len(s) and s[i] in "+-":
        sign = -1 if s[i] == '-' else 1
        i += 1

    while i < len(s) and s[i].isdigit():
        num = num * 10 + int(s[i])
        i += 1

    return max(-2**31, min(sign * num, 2**31 - 1))
