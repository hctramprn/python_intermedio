def run():
    #a function that appends to a dictionary the cube of the numbers from 1 to 100
    # my_dict = {}

    # for i in range(1, 101):
    #     my_dict[i] = i**3
    # print(my_dict)

    #Prints the cube of the numbers from 1 to 100 that are not divisible by 3
    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(my_dict)

    #Alternate version printing the roots from 1 to 1000
    # my_dict_sq = {i: round(i**(0.5), 3) for i in range(1, 1001)}
    # print(my_dict_sq)

if __name__ == '__main__':
    run()