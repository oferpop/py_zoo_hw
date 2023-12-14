"""
this program mentto manage a zoo

"""

from enum import Enum
import json


class Actions (Enum):
    ADD = 1
    PRINT = 2
    EXIT = 3

animals=[]
DATA_FILES='my_list.json'

def menue():
  
        for act in Actions:
            print (f"{act.value} - {act.name}")
   
        return Actions(int (input("selection?")))
        
def print_animals():
    for animal in animals:
            print(f'animal name{animal["name"]}age:{animal["age"]}')   

def exit_program():
    with open(DATA_FILES, 'w') as json_file:
        json.dump(animals, json_file)
    exit()  
def save_data():
    global animals
   
    with open(DATA_FILES, 'r') as json_file:
        animals = json.load(json_file)
  
        print("make")
def main():
    save_data()

    while(True):
        userselection=menue()
        if userselection== Actions.ADD:
            animals.append({"name":input("animal name"),"age":input("age")})
        elif userselection== Actions.EXIT:
            exit_program() 
        elif userselection== Actions.PRINT:
             print_animals() 
        else:
            print(" shut up") 





if __name__ == '__main__':
    main()