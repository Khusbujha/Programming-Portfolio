"""This program demonstrates a function called common_letters that takes two words and returns a sorted list of all unique letters that appear in both words."""


def common_letters(word1, word2):
    set1 = set(word1.lower())
    set2 = set(word2.lower())
    common = set1.intersection(set2)
    return sorted(common)


print(common_letters("Kathmandu", "Pokhara"))
print(common_letters("Python", "JavaScript"))
