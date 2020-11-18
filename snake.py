#! python3

# imports
import tkinter
import random

# initialisation
window = tkinter.Tk()
window.resizable(width = False, height = False)
window.title("Snake")
window.geometry("500x500")

background = tkinter.Canvas(window, width = 500, height = 500, background="#000", bd=0, highlightthickness=0)
background.pack()

direction = [10, 0]
coords = {'head':[0, 0], 'body':[None], 'food':[200, 200], 'end':[-10, 0]}
snake_head = background.create_rectangle(0, 0, 10, 10, fill="#F00", outline="#F00")
snake_body = [None]
snake_dirs = [[10, 0]] # move for each rectangle
food = background.create_oval(200, 200, 210, 210, fill="#0F0", outline="#0F0")

def motion():
    global snake_body, snake_dirs, food
    if (coords['head'] == coords['food']):
        coords['body'].append(coords['end'][:]) # a = b[:] to copy (instead of reference a = b)
        temp = background.create_rectangle(coords['end'][0], coords['end'][1], coords['end'][0]+10, coords['end'][1]+10, fill="#FF0", outline="#FF0")
        snake_body.append(temp)
        snake_dirs.append(snake_dirs[-1])
        while (coords['food'] == coords['head'] or coords['food'] in coords['body']):
            temp = [random.randint(0, 49)*10, random.randint(0, 49)*10]
            coords['food'][0] = temp[0]
            coords['food'][1] = temp[1]
        background.coords(food, temp[0], temp[1], temp[0]+10, temp[1]+10)
    else:
        coords['end'][0] += snake_dirs[-1][0]
        coords['end'][1] += snake_dirs[-1][1]
    coords['head'][0] += direction[0]
    coords['head'][1] += direction[1]
    snake_dirs = snake_dirs[:-1]
    snake_dirs.insert(0, direction)
    background.move(snake_head, direction[0], direction[1])
    for i in range(1, len(snake_dirs)):
        coords['body'][i][0] += snake_dirs[i][0]
        coords['body'][i][1] += snake_dirs[i][1]
        background.move(snake_body[i], snake_dirs[i][0], snake_dirs[i][1])
    print(coords)
    if ((coords['head'] in coords['body']) or (-10 in coords['head'])):
        return False
    window.after(100, motion)

def changeDirections(event):
    global direction
    if (event.keysym == 'Down' and direction != [0, -10]):
        direction = [0, 10]
    elif (event.keysym == 'Up' and direction != [0, 10]):
        direction = [0, -10]
    elif (event.keysym == 'Right' and direction != [-10, 0]):
        direction = [10, 0]
    elif (event.keysym == 'Left' and direction != [10, 0]):
        direction = [-10, 0]

# run
window.after(100, motion)
window.bind("<Down>", changeDirections)
window.bind("<Up>", changeDirections)
window.bind("<Right>", changeDirections)
window.bind("<Left>", changeDirections)
window.mainloop()
