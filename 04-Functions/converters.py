def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_i(cm):
    return cm / 2.54

def fi_to_cm(feet, inches):
    total_inches = (feet * 12) + inches
    return total_inches * 2.54


if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'10cm = {cm_to_i(10)}i')
    print(f'5feet 10inches = {fi_to_cm(5, 10)}cm')