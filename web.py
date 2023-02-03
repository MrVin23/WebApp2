import streamlit as st
import functions
import colorama
from colorama import Fore


# ======================================================================
#   Instantiating Functions
# ====================================================================== 
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    # print(Fore.RED + todo + Fore.WHITE)
    
# ======================================================================
#   Instantiating Variabls and lists
# ======================================================================     
todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my Sub Header")
st.write("This is to increase your productivity")

# ======================================================================
#   Check Box
# ====================================================================== 
for index, todo in enumerate (todos):
    checkbox = st.checkbox(todo, key =todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
        
st.text_input(label="",
              placeholder="Enter a todo",
              on_change=add_todo,
              key= 'new_todo')

print("Hello")
st.session_state