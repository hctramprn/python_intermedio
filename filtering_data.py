from ast import For


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
#Filter and Map lists
    #Creates a list of all the python developers in DATA
    all_python_devs = list(filter(lambda worker: worker['language'] == 'python', DATA))
    all_python_devs = list(map(lambda worker: worker['name'], all_python_devs))
    print(f'The python devs are: {all_python_devs}')

    #Creates a list of all the workers at Platzi in Data
    all_platzi_workers = list(filter(lambda worker: worker['organization'].lower() == 'platzi', DATA))
    all_platzi_workers = list(map(lambda worker: worker['name'], all_platzi_workers))
    print(f'The people that work at Platzi are: {all_platzi_workers}')

#List comprehensions
    #Creates a list of workers above 70 years old
    old_people = [worker | {'old': (worker['age'] > 70)} for worker in DATA]
    old_people = [worker['name'] for worker in old_people if worker['old']]
    print(f'A list of old people: {old_people}')

    #Creates a 
    adults = [worker['name'] for worker in DATA if worker['age'] > 18]
    print(f'The adults are: {adults}')


    # for workers in DATA:
    #     if workers['age'] > 30:
    #         workers['old'] = workers['age'] > 30
    #         print(workers)


if __name__ == '__main__':
    run()