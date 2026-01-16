"""This program consists of three function that each take two strings as parameters and return sorted lists according to these requirements:
Lists of letters that appear in at least one of the two strings.
List of letters that appear in both strings.
List of letters that appear in either strings but not in both.
"""


def str_union(s1, s2):
    return sorted(set(s1) | set(s2))


def str_intersection(s1, s2):
    return sorted(set(s1) & set(s2))


def str_sym_diff(s1, s2):
    return sorted(set(s1) ^ set(s2))


print(str_union("cheese", "cake"))
print(str_intersection("cheese", "cake"))
print(str_sym_diff("cheese", "cake"))
