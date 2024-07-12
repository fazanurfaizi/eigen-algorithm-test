def reverse_alpha(input: str):    
    alpha_pos = []
    number_pos = []
    
    for i in range(len(input)):
        if input[i].isalpha():
            alpha_pos.append((i, input[i]))
        elif input[i].isdigit():
            number_pos.append((i, input[i]))
    
    reversed_alphabets = [alpha_pos[i][1] for i in range(len(alpha_pos) - 1, -1, -1)]
    
    result = list(input)
    
    for i in range(len(alpha_pos)):
        result[alpha_pos[i][0]] = reversed_alphabets[i]
    
    result_str = ''.join(result)

    return result_str

test_string = 'NEGIE1'
reversed_string = reverse_alpha(test_string)
print(reversed_string)