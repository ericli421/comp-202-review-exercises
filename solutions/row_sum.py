def row_sum(input_list):

    output_list = []

    for row in input_list:

        sum = 0

        for num in row:
            sum += num
        
        output_list.append(sum)

    return output_list