"""This program prompts for the number of students and group size, then displays how many groups will be needed and
how many will be left over in a smaller group.
This program also changes the grammar of the output meaning if there is a single student the output prints student instead of students and similarly for group.
"""


def grammar(num, word):
    if num == 1:
        return word
    else:
        return word + "s"


n = input("Enter the number of students:")
s = input("Enter the size of the group:")
n = int(n)
s = int(s)
g = n // s
r = n % s
group_grammar = grammar(g, "group")
student_grammar = grammar(r, "student")
print(f"There will be {g} {group_grammar} with {r} {student_grammar} remaining.")
