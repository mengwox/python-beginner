# Write a function called chop that takes a list and modifies it,
# removing the first and last elements, and returns None.
def chop(cols: list):
    cols.pop(len(cols) - 1)
    cols.pop(0)


# Then write a function called middle that takes a list
# and returns a new list that contains all but the first and last elements.
def middle(cols: list):
    size = len(cols)
    return cols[1:size - 1]


temp = [1, 2, 3, 4]
print(middle(temp))
print(temp)
print(chop(temp))
print(temp)
