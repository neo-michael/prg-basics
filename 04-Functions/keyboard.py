def input_string(message):
    value = input(message)
    return value

def input_integer(message):
    value = int(input(message))
    return value

def input_real(message):
    value = float(input(message))
    return value

def input_boolean(message):
    value = input(message).strip().lower()
    return value in ['y', 'yes']
