"""This program demonstrates a function that accepts a list of numbers and returns a new list containing only the even numbers, sorted in ascending order."""


def even_list(n):
    a = [i for i in n if i % 2 == 0]
    print(sorted(a))


new = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_list(new)
