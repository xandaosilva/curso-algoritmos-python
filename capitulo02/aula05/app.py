school_grades = [8, 4, 10, 10, 10, 7, 5, 3, 7, 6]
average = round(sum(school_grades)/len(school_grades),1)

def check_avg(school_grade, average):
    return True if (school_grade >= average) else False


print(f"Average: {average}")
for school_grade in school_grades:
    res = check_avg(school_grade, average)
    print(f"Student grade: {school_grade} - Approved: {res}")

