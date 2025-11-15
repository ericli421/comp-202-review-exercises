import random

def shuffle(input_list):
    """
    Shuffles the list that it's given

    Args:
        input_list : list

    Returns:
        None
    """

    for i in range(len(input_list)):
        n = random.randint(0, len(input_list)-1)
        input_list[i], input_list[n] = input_list[n], input_list[i]

a = [1,2,3,4,5,6,7]
shuffle(a)
print(a)