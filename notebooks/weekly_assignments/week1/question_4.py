"""This program tells the teacher how many sweets to give each people and how many she has left,
based on number of sweets and number of total students present that day."""


def grammar(num, word):
    """This function fixes the grammar in the output."""
    if num == 1:
        return word
    else:
        return word + "s"


s = input("Enter the number of sweets:")
n = input("Enter the number of pupils:")
s = int(s)
n = int(n)
a = s // n
r = s % n
sweet_grammar = grammar(a, "sweet")
print(f"Each pupil gets {a} {sweet_grammar} with {r} remaining.")
