from Tkinter import * #Importing module " Tkinter" which contains many window and color functions for user interface, the pygane did not support arrays
from nathan_maze import * #Imports code from a fellow student in my high school, my list of arrays

while True: #Intiates engine
    current_map = maze_11 #Sets the map where the "Hero" will be generated
    current_map_immutable = maze_11_immutable #Sets the "Landscape" of the map
    class Unit(object): # defines class
        def __init__(self,sprite,x,y): #defines what parameters Unit objects need
            self.sprite = sprite #This says that whatever instance of the object
            self.x = x
            self.y = y
            current_map[self.y][self.x] = self.sprite #what our Unit will look like
    Hero = Unit(8,3,3) #generates Hero
    root = Tk() # generates window
    root.wm_title("Swarm")  #window title
    # setting rot and root.wm are pre-requisites to calling main loop window function
    gm = Canvas(root, width = 700, height = 700) #Creates game map canvas
    def gm_update_positive(a):#Defines how to update game map canvas
        gm.delete('all') #Clears old game map canvas
        for row in range(len(a)): #Iterates through each row
            for column in range(len(a[row])):#Iterates through each column in each row
                color = "white" #This is the default color of the canvas
                if a[row][column] == 1:
                    color = "black"
                elif a[row][column] == 8:
                    color = "blue"
                elif a[row][column] == 2:
                    color = "red"
                elif a[row][column] in [3,4,5]:
                    color = "green"
                elif a[row][column] == 6:
                    color = "orange"
                gm.create_rectangle(100 * row, 100 * column, 100 * row + 100, 100 * column + 100,
                    outline = color, fill = color) #Here we generate the the rectangles, search through tkinter documentation for the create_rectangle() function for more info
        gm.pack(fill=BOTH, expand=1)#This actual fills in the canvas
    def gm_update_negative(a):
        gm.delete('all')
        for row in range(len(a)):
            for column in range(len(a[row])):
                color = "black"
                if a[row][column] == 1:
                    color = "white"
                elif a[row][column] == 8:
                    color = "red"
                elif a[row][column] == 2:
                    color = "blue"
                elif a[row][column] in [3,4,5]:
                    color = "green"
                elif a[row][column] == 6:
                    color = "yellow"
                gm.create_rectangle(100 * row, 100 *  column, 100 * row + 100, 100 * column + 100,
                    outline = color, fill = color)
        gm.pack(fill=BOTH, expand=1)
    gm_update_positive(current_map) #this runs our function
    pos = True
    pos_switch_conditional = True
    def endscreen():
        root.destroy()
        print("YOU WIN!")
        sys.exit()
    def title_define():
        if current_map == maze_11:
            root.wm_title("Maze_11")
        elif current_map == maze_12:
            root.wm_title("Maze_12")
        elif current_map == maze_13:
            root.wm_title("Maze_13")
        else:
            root.wm_title("Swarm")
    title_define()
    def n2p0(z,y):
        global current_map
        global current_map_immutable
        current_map[Hero.y][Hero.x] = current_map_immutable[Hero.y][Hero.x]
        current_map = z
        current_map_immutable = y
        current_map[Hero.y][Hero.x] = current_map_immutable[Hero.y][Hero.x]
        Hero.x = 3
        Hero.y = 3
        title_define()
        current_map[Hero.y][Hero.x] = Hero.sprite
        if pos == True:
            gm_update_positive(current_map)
        else:
            gm_update_negative(current_map)
    def move(a,b,c):#Where a is a Unit, c is an integer, and b is x or y
        current_map[a.y][a.x] = current_map_immutable[a.y][a.x] #Takes the current unit position and returns it to its originial state
        if b == 'x':
            a.x = a.x + c
            current_map[a.y][a.x] = a.sprite #Places the Unit at the new x location
            if pos == False:
                gm_update_negative(current_map)
            else:
                gm_update_positive(current_map)
        elif b == 'y':
            a.y = a.y + c
            current_map[a.y][a.x] = a.sprite #Places the Unit at the new y location
            if pos == False:
                gm_update_negative(current_map)
            else:
                gm_update_positive(current_map)
    def LeftKey(event):  #This tell the program what to do when the the 'Left Key' is pushed
        a = Hero.y - 1
        if current_map[a][Hero.x] == 1:
            pass
        elif current_map[a][Hero.x] == 2:
            global pos
            if pos == True:
                pos = False
                move(Hero,'y',-1)
                global pos_switch_conditional
                pos_switch_conditional = True
            else:
                pos = True
                move(Hero,'y',-1)
                pos_switch_conditional = True
        elif current_map[a][Hero.x] in [3,4,5]:
            if current_map[a][Hero.x] == 3:
                n2p0(maze_11,maze_11_immutable)
            elif current_map[a][Hero.x] == 4:
                n2p0(maze_12,maze_12_immutable)
            elif current_map[a][Hero.x] == 5:
                n2p0(maze_13,maze_13_immutable)
        elif current_map[a][Hero.x] == 6:
            endscreen()
        else:
            move(Hero,'y',-1)
    def RightKey(event):
        a = Hero.y + 1
        if current_map[a][Hero.x] == 1:
            pass
        elif current_map[a][Hero.x] == 2:
            global pos
            if pos == True:
                pos = False
                move(Hero,'y',1)
                global pos_switch_conditional
                pos_switch_conditional = True
            else:
                pos = True
                move(Hero,'y',1)
                pos_switch_conditional = True
        elif current_map[a][Hero.x] in [3,4,5]:
            if current_map[a][Hero.x] == 3:
                n2p0(maze_11,maze_11_immutable)
            elif current_map[a][Hero.x] == 4:
                n2p0(maze_12,maze_12_immutable)
            elif current_map[a][Hero.x] == 5:
                n2p0(maze_13,maze_13_immutable)
        elif current_map[a][Hero.x] == 6:
            endscreen()
        else:
            move(Hero,'y',1)
    def UpKey(event):
        a = Hero.x - 1
        if current_map[Hero.y][a] == 1:
            pass
        elif current_map[Hero.y][a] == 2:
            global pos
            if pos == True:
                pos = False
                move(Hero,'x',-1)
                global pos_switch_conditional
                pos_switch_conditional = True
            else:
                pos = True
                move(Hero,'x',-1)
                pos_switch_conditional = True
        elif current_map[Hero.y][a] in [3,4,5]:
            if current_map[Hero.y][a] == 3:
                n2p0(maze_11,maze_11_immutable)
            elif current_map[Hero.y][a] == 4:
                n2p0(maze_12,maze_12_immutable)
            elif current_map[Hero.y][a] == 5:
                n2p0(maze_13,maze_13_immutable)
        elif current_map[Hero.y][a] == 6:
            endscreen()
        else:
            move(Hero,'x',-1)
    def DownKey(event):
        a = Hero.x + 1
        if current_map[Hero.y][a] == 1:
            pass
        elif current_map[Hero.y][a] == 2:
            global pos
            if pos == True:
                pos = False
                move(Hero,'x',1)
                global pos_switch_conditional
                pos_switch_conditional = True
            else:
                pos = True
                move(Hero,'x',1)
                pos_switch_conditional = True
        elif current_map[Hero.y][a] in [3,4,5]:
            if current_map[Hero.y][a] == 3:
                n2p0(maze_11,maze_11_immutable)
            elif current_map[Hero.y][a] == 4:
                n2p0(maze_12,maze_12_immutable)
            elif current_map[Hero.y][a] == 5:
                n2p0(maze_13,maze_13_immutable)
        elif current_map[Hero.y][a] == 6:
            endscreen()
        else:
            move(Hero,'x',1)
    def Quit(event):
        root.destroy()
        sys.exit()
    def pos_switch(event):
        global pos
        global pos_switch_conditional
        if pos_switch_conditional == True:
            if pos == True:
                pos = False
                gm_update_negative(current_map)
            else:
                pos = True
                gm_update_positive(current_map)
            pos_switch_conditional = False
        else:
            pass
    root.bind('<Left>',LeftKey) 
    root.bind('<Right>',RightKey)
    root.bind('<Up>',UpKey)
    root.bind('<Down>',DownKey)
    root.bind('<Escape>',Quit)
    root.bind('<p>', pos_switch)

    root.mainloop()
    # mainloop is a tkinter function, by this time we have setup assigned root to a window, window size, and what the canvas will look like
    
