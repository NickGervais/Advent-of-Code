def read_input_to_list(day_path):
    return_list = []
    with open(f'/{day_path}/input.txt', 'r') as input:
        for i, line in enumerate(input):
            return_list.append(line)
    return return_list