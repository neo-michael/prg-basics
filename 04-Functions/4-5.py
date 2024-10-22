def final_grade(points):
    if points < 10:
        return 'Fail'
    elif points >= 18:
        return 'Excellent'
    elif points >= 14:
        return 'Good'
    elif points >= 10:
        return 'Satisfactory'

points = float(input("Enter the number of points obtained: "))
grade = final_grade(points)
print('The final grade is:', grade)
