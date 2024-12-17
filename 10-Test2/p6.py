import json

def f(years, course, average_grade):
    with open("data/data.json", 'r', encoding="utf-8") as file:
        students = json.load(file)

    counter = 0
    for student in students:
        if student["age"] < years:
            continue

        for course_obj in student["studies"]["courses"]:
            if not course_obj["name"] == course:
                continue
            avg = sum(course_obj["grades"]) / len(course_obj["grades"])
            if not avg >= average_grade:
                continue
            print(avg, student["name"], course_obj["name"])
            counter += 1

    return counter
print(f(21, "statistics", 4))