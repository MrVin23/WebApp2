# Make list
import colorama
import time
from colorama import Fore
# from functions import get_todos, write_todos
import Modules.functions as functions

functions.print_date()

while True:
    user_action = input("\nType add, show, edit, complete or exit: \n").lower()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo)
        functions.write_todos(todos, 'todos.txt')

    elif user_action.strip().startswith('show'):
        todos = functions.get_todos()
        print("\n" + Fore.CYAN)

        for index, thing in enumerate(todos):
            thing = thing.title().strip()
            print(f"{index+1}) {thing}")

        print("\n" + Fore.WHITE)

    elif user_action.strip().startswith('complete'):
        try:
            todos = functions.get_todos()
            number = int(user_action[9:])
            todos.pop(number-1)

            print("\n" + Fore.CYAN)
            for index, thing in enumerate(todos):
                thing = thing.title().strip()
                print(f"{index+1}) {thing}")

            functions.write_todos(todos)

            print("\n" + Fore.WHITE)
        except IndexError:
            print(Fore.RED + "\nThere is no item with that index number" + Fore.WHITE)
            continue

    elif user_action.strip().startswith('exit'):
        break

    elif user_action.strip().startswith('edit'):
        try:

            number = int(user_action[5:])
            new_todo = input("Enter new to do: ")
            todos = functions.get_todos()
            todos[number-1] = new_todo + "\n"

            print("\n" + Fore.CYAN)
            for index, thing in enumerate(todos):
                thing = thing.title().strip()
                print(f"{index+1}) {thing}")

            print("\n" + Fore.WHITE)

            functions.write_todos(todos, 'todos.txt')

        except ValueError:
            print(Fore.RED + "\nYour command is not valid you numbskull" + Fore.WHITE)
            continue
    else:
        print(Fore.RED + "\nCommand is not valid you idiot" + Fore.WHITE)

print(Fore.BLUE + "     THE PROGRAM HAS CLOSED\n        BYE!" + Fore.WHITE)
