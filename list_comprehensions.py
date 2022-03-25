
def run():

#A list of the squared numbers from 1 to 100 excluding those that are divisible by 3

#     squares = []
#     for i in range(1, 101):
#         if i % 3 != 0:
#             squares.append(i**2)
#     print(squares)


#A comprehension list of all the numbers from 1 to 99999 that are divisible by 4, 6 and 9
    squares = [i for i in range(1, 100000) if i % 36 == 0]
    print(squares)



if __name__ == '__main__':
    run()