"""This program demostrates a function named merge_student_scores that takes two dictionaries:
student_names = {1: 'Anish', 2: 'Priya', 3: 'Sujan'}
student_scores = {1: 88, 2: 92, 3: 79}
and returns a new dictionary combining both, in the format:
{'Anish': 88, 'Priya': 92, 'Sujan': 79}
"""


def merge_student_scores(stu_name, stu_score):
    merged = {}
    for sid, name in stu_name.items():
        if sid in stu_score:
            merged[name] = stu_score[sid]
    return merged


student_names = {1: "Anish", 2: "Priya", 3: "Sujan"}
student_scores = {1: 88, 2: 92, 3: 79}
print("The merged dictionary:")
print(merge_student_scores(student_names, student_scores))
