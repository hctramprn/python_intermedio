def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Héctor", "lastname": "Amparán"}

    super_list = [
    {"firstname": "Pepe", "lastname": "Pecas"},
    {"firstname": "Fulano", "lastname": "Pérez"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(f"The value of the key {key} is {value}")


if __name__ == '__main__':
    run()