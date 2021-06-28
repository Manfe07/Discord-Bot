
def remove_first_space(input : str):
    while input[0] == ' ':
        input = input[1:]
    return input