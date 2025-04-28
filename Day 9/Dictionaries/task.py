# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#                           "Function": "A piece of code that you can easily call over and over again.",2
# }
# programming_dictionary["Loop"] = "The action of doing things over and over again."
# for key in programming_dictionary:
#     print(key)

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for name in student_scores:
    score = student_scores[name]

    if score >= 91:
        student_grades[name] = "Outstanding"
    elif score >= 81:
        student_grades[name] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"

print(student_grades)



