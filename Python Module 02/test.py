def atoi(temp_str : str)->int:
    res = 0
    for c in temp_str:
        res *= 10
        res += int(c)
    return res

i = atoi("8434")
print(i // 2)