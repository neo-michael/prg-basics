###
# A program that displays your height both in cm and in feet and inches.
#
import math
cm = 170
inches = cm / 2.54
feet = inches / 12
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {int(feet)} feet and {math.ceil((feet % 1) * 10)} inches')