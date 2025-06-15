def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))   # In Python, strip() is used for removing whitespace or characters from the beginning and end of a string.
    return n



l = ["harry", "rohan", "shubham", "an"]
print(rem(l, "an"))