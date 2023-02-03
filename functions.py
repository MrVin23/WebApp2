import time
import streamlit as st

def print_date():
    print("\tToday is:\t" + time.strftime("%c"))


def get_todos(filepath='todos.txt'):
    """This method returns lines of text that are read from a text file"""
    # This is called a "Doc string which describe the function"
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='todos.txt'):
    with open(filepath, 'w') as file:
        todos = file.writelines(todos_arg)


