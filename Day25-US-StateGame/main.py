import turtle
import pandas as pd
from names import Name_Writter
import os


def get_mouse_cord(x,y):
    """
    Function to get the coordinates from mouse click

    Args:
        x : position x on screen click
        y : position y on screen click
    """
    print(x, y)


#defining the path with the file dir 
path = os.path.dirname(__file__)

writer = Name_Writter()

#defining the screen object
screen = turtle.Screen()
screen.title("U.S State Game")


#loading the image to screen
screen.addshape(os.path.join(path,"blank_states_img.gif"))
turtle.shape(os.path.join(path,"blank_states_img.gif"))

guessed_states = set()
df = pd.read_csv(os.path.join(path, "50_states.csv"))

while len(guessed_states) < 50:
    answer = turtle.textinput(f"U.S State {len(guessed_states)}/50", "Please, insert the state name:").title()
    
    if answer == "Exit":
        break
    
    a = df[df['state'] == answer] 
    if a.empty:
        continue
    else:
        a = a.to_dict()
        index = int(list(a['state'].keys())[0])
        writer.show_state(a['state'][index],a['x'][index], a['y'][index])
        guessed_states.add(answer)

df_states = df['state'].tolist()
dic_to_export = {
    "state":[]
}

for state in df_states:
    if state not in guessed_states:
        dic_to_export["state"].append(state)

df_to_export = pd.DataFrame(dic_to_export)
df_to_export.to_csv(os.path.join(path, 'non-guessed.csv'))


turtle.onclick(get_mouse_cord)

turtle.mainloop()
