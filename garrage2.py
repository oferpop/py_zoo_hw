import os
import json
from enum import (Enum)


class Actions(Enum):
   PRINT =1
   ADD=2
   SEARCH=3
   DELETE =4
   EXIT=5

cars=[]
my_data_file='contact.json'

def menu():
    for x in Actions:
         print(f'{x.value} - {x.name}')

    return Actions(int(input("Enter your selection:")))     


def load_data():# load a list from a file
    global cars
  
with open(my_data_file, 'r') as file:
            json_string = file.read()
            cars = json.loads(json_string)
   

def main():
    os.system('cls'if os.name=='nt' else 'clear')#clean screan
    load_data()#load data from a file

    while(True):
        userSelection=menu() #display a menu and get user selection and  implements menu
        if userSelection == Actions.EXIT: exit_func()
        if userSelection ==  Actions.PRINT: print(cars)
        if userSelection ==  Actions.SEARCH: search_car()
        if userSelection ==  Actions.ADD: add_contact()
    

def add_contact():
    cars.append({"model":input("Enter car model:"),"color":input("Enter car color:")})

def search_car():
    search_model = input("Enter model to search for: ")
    search_color = input("Enter color to search for: ")

    found = False
    for car in cars:
        if car['model'].lower() == search_model.lower() and car['color'].lower() == search_color.lower():
            print(f"Found car: {car}")
            found = True
    if not found:
        print("No car found with the specified model and color.")

def exit_func():
    json_string = json.dumps(cars)
    # save the list in a file
    with open(my_data_file, 'w') as file:
        file.write(json_string)
    print("by by") 
    exit()      
if __name__ == "__main__":
    main()