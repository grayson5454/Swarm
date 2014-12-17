'''
Introduction by the Author, Grayson Perez  grayson5454  (at)  Gmail

game purpose

custom classes I've define

external classses I use....

external libraries and modules
https://docs.python.org/2/library/tkinter.html?highlight=tkinter




'''


from Tkinter import * #Importing module " Tkinter" which contains many window and color functions for user interface, the pygame did not support arrays
from nathan_maze import * #Imports code from a fellow student in my high school, my list of arrays

while True: #Intiates my game engine

    #Variable Declarations
    current_map = maze_11 #Sets the map where the "Hero" will be generated
    current_map_immutable = maze_11_immutable #Sets the "Landscape" of the map
    root = Tk() #Generates window TK defines that there will be a window  
    root.wm_title("Swarm")  #Window title
    gamemap= Canvas(root, width = 700, height = 700) #Creates game map canvas using class defined in tkinter
    pos = True #Sets whether or not gamemap_update_positive() or gamemap_update_negative() will be used
    pos_switch_conditional = True #Sets whether ot not pos's value can be changed

    #End of Variable Declarations

    #Class Declarations
    
    class Unit(object): #Defines all objects that may move in our "map" arrays
        
        def __init__(self,sprite,x_cord,y_cord): #Defines what parameters Unit objects need
            
            self.sprite = sprite #This defines the spirite of any instanced object of Unit
            self.x_cord = x_cord #Sets the y coordinate of instanced object
            self.y_cord = y_cord #Sets the x_cord coordinate of instanced object
            
            current_map[self.y_cord][self.x_cord] = self.sprite #Places the instanced object into the array, replacing the array position with the instanced object spirite

    #End of Class Declarations

    #Function Declarations
            
    def gamemap_update_positive(a):#Defines how to update game map canvas
        gamemap.delete('all') #Clears old game map canvas
        
        for row in range(len(a)): #Iterates through each row
            for column in range(len(a[row])):#Iterates through each column in each row
                color = "white" #Sets the default color of any value
                if( a[row][column] == 1 ): #Defines color for all squares whose value is 1
                    color = "black" #Assigns each "1" with the color black
                elif ( a[row][column]  == 8):
                    color = "blue"
                elif ( a[row][column]  in [3,4,5]): #Defines the color for all sqaures with values 3,4, or 5
                    color = "green"
                elif ( a[row][column] == 6 ):
                    color = "orange"
                    
                gamemap.create_rectangle(100 * row, 100 * column, 100 * row + 100, 100 * column + 100,
                    outline = color, fill = color) #Here we generate the the rectangles, search through tkinter documentation for the create_rectangle() function for more info

        gamemap.pack(fill=BOTH, expand=1)#This actually fills in the canvas generating it to the window
        

        
    def gamemap_update_negative(a):#Defines how to update game map canvas, does the opposite colors as gamemap_update_positive
        gamemap.delete('all')
        
        for row in range(len(a)):
            for column in range(len(a[row])):
                color = "black"
                if ( a[row][column] == 1 ):
                    color = "white"
                elif ( a[row][column] == 8 ):
                    color = "red"
                elif ( a[row][column] == 2 ):
                    color = "blue"
                elif ( a[row][column] in [3,4,5] ):
                    color = "green"
                elif ( a[row][column] == 6 ):
                    color = "yellow"
                    
                gamemap.create_rectangle(100 * row, 100 *  column, 100 * row + 100, 100 * column + 100,
                    outline = color, fill = color)

        gamemap.pack(fill=BOTH, expand=1)
        


    def endscreen(): #This function is used when the game is beat
        
        root.destroy() #Destroys the window
        print("YOU WIN!") #Prints "You Win"  to the console
        sys.exit() #Terminates the program
        

        
    def title_define(): #Re-defines the title of the window based on the current map
        
        if current_map == maze_11:
            root.wm_title("Maze_11")
        elif current_map == maze_12:
            root.wm_title("Maze_12")
        elif current_map == maze_13:
            root.wm_title("Maze_13")
        else:
            root.wm_title("Swarm")

            

    def map_change(z,y): #Changes the map currently on screen
        
        global current_map
        global current_map_immutable
        
        current_map[Hero.y_cord][Hero.x_cord] = current_map_immutable[Hero.y_cord][Hero.x_cord] # takes the Hero's current position on the map and replaces it with the 'Landscape value' from the immutable map
        current_map = z #Sets new current map
        current_map_immutable = y #Sets new current map immutable
        
        Hero.x_cord = 3 #Sets new x_cord coordinate for Hero
        Hero.y_cord = 3 #Sets new y_cord cooridnate for Hero
        
        title_define() # Re-defines title of window
        current_map[Hero.y_cord][Hero.x_cord] = Hero.sprite #Places Hero to map
        
        if pos == True: #Checks value of pos and determines which update function to use
            gamemap_update_positive(current_map)
        else:
            gamemap_update_negative(current_map)


            
    def move(a,b,move_value):#Where a is any Unit, c is an integer, and b is x_cord or y
        current_map[a.y_cord][a.x_cord] = current_map_immutable[a.y_cord][a.x_cord] #Takes the current unit position and returns it to its originial state

        if b == 'x': #Checks if we are using the x-axis
            a.x_cord = a.x_cord + move_value #Takes any instanced object's x cooridnate and adds the integer c to it
            current_map[a.y_cord][a.x_cord] = a.sprite #Places the Unit at the new x location
            if pos == False:
                gamemap_update_negative(current_map)
            else:
                gamemap_update_positive(current_map)
        elif b == 'y': #Checks if we are using the y-axis
            a.y_cord = a.y_cord + move_value #Takes any instanced object's y cooridnate and adds the integer c to it
            current_map[a.y_cord][a.x_cord] = a.sprite #Places the Unit at the new y location
            if pos == False:
                gamemap_update_negative(current_map)
            else:
                gamemap_update_positive(current_map)
    def direction_key(axis,move_value):
        global pos
        global pos_switch_conditional
        if axis == 'y':
            new_position = Hero.y_cord + move_value
            if current_map[new_position][Hero.x_cord] == 1:
                pass
            elif current_map[new_position][Hero.x_cord] == 2:
                pos_switch_conditional = True
                if pos == True:
                    move(Hero,axis,move_value)
                    pos_switch_conditional
                else:
                    move(Hero,axis,move_value)
            elif current_map[new_position][Hero.x_cord] in [3,4,5]:
                if current_map[new_position][Hero.x_cord] == 3:
                    map_change(maze_11,maze_11_immutable)
                elif current_map[new_position][Hero.x_cord] == 4:
                    map_change(maze_12,maze_12_immutable)
                elif current_map[new_position][Hero.x_cord] == 5:
                    map_change(maze_13,maze_13_immutable)
            elif current_map[new_position][Hero.x_cord] == 6:
                endscreen()
            else:
                move(Hero,axis,move_value)
        elif axis == 'x':
            new_position = Hero.x_cord + move_value
            if current_map[Hero.y_cord][new_position] == 1:
                pass
            elif current_map[Hero.y_cord][new_position] == 2:
                if pos == True:
                    move(Hero,axis,move_value)
                    pos_switch_conditional = True
                else:
                    pos = True
                    move(Hero,axis,move_value)
                    pos_switch_conditional = True
            elif current_map[Hero.y_cord][new_position] in [3,4,5]:
                if current_map[Hero.y_cord][new_position] == 3:
                    map_change(maze_11,maze_11_immutable)
                elif current_map[Hero.y_cord][new_position] == 4:
                    map_change(maze_12,maze_12_immutable)
                elif current_map[Hero.y_cord][new_position] == 5:
                    map_change(maze_13,maze_13_immutable)
            elif current_map[Hero.y_cord][new_position] == 6:
                endscreen()
            else:
                move(Hero,axis,move_value)
                
    def LeftKey(event):  
        direction_key('y',-1)

            
    def RightKey(event):
        direction_key('y',1)
    def UpKey(event):
        direction_key('x',-1)

            
    def DownKey(event):
        direction_key('x',1)

            
    def Quit(event):
        root.destroy()
        sys.exit()

        
    def pos_switch(event):
        global pos
        global pos_switch_conditional
        
        if pos_switch_conditional == True:
            if pos == True:
                pos = False
                gamemap_update_negative(current_map)
            else:
                pos = True
                gamemap_update_positive(current_map)
            pos_switch_conditional = False
        else:
            pass

    #End of Function Delcarations
        
    Hero = Unit(8,3,3) #generates Hero using my own class


    
    # setting rot and root.wm are pre-requisites to calling main loop window function

    
    gamemap_update_positive(current_map) #this runs our function
    
    title_define()

    root.bind('<Left>',LeftKey) 
    root.bind('<Right>',RightKey)
    root.bind('<Up>',UpKey)
    root.bind('<Down>',DownKey)
    root.bind('<Escape>',Quit)
    root.bind('<p>', pos_switch)

    root.mainloop()
    # mainloop is a tkinter function, by this time we have setup assigned root to a window, window size, and what the canvas will look like
    
