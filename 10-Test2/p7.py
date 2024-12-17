import re

def f(array):
    counter = 0
    for username in array:
        if re.match(r"[a-z0-9_]{4,12}$", username):
            print(username)
            counter += 1

    return counter

print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))      