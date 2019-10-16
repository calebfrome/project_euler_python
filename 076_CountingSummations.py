count = 0


def find_addends(n, addends):
    global count

    if n == 0:
        if len(addends) >= 2:
            count += 1
        return

    for i in range(n, 0, -1):
        new_addends = addends.copy()
        if len(new_addends) > 0:
            if i > new_addends[len(new_addends) - 1]:
                continue

        new_addends.append(i)
        find_addends(n - i, new_addends)


a = []
find_addends(100, a)
print(count)
