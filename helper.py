from icecream import ic

def print_animals(animals):
    for animal in animals:
        ic(animal)
        # print(f'animal name{animal["name"]}age:{animal["age"]}')   
def search_animal(animals):
    search_name = input("Enter the animal name to search: ")
    search_age = input("Enter the animal age to search: ")

    found_animals = [animal for animal in animals if animal['name'] == search_name and str(animal['age']) == search_age]

    if found_animals:
        print("Found animals:")
        for animal in found_animals:
            print(animal)
    else:
        print("No animals found with that name and age.")
        # search by name and age

def delete_animal(animals):
    del_name = input("Enter the name of the animal to delete: ")
    del_age = input("Enter the age of the animal to delete: ")

    # Attempt to find and delete the animal with matching name and age
    for animal in animals:
        if animal['name'] == del_name and str(animal['age']) == del_age:
            animals.remove(animal)
            print(f"Animal with name '{del_name}' and age '{del_age}' has been deleted.")
            return

    print("No animal found with that name and age.")



        