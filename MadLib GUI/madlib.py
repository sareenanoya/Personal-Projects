from tkinter import*
import random

def madlib():
    'create GUI for generating a customized madlib'
    global name_entry, display
    global place_entry, display
    global food_entry, display

    root=Tk()

    # name box frame
    name_box = Frame(root)
    name_label = Label(name_box, text = "Enter a name: ")
    name_label.pack(side=LEFT)
    name_entry = Entry(name_box, width = 20)
    name_entry.pack(side=RIGHT)
    name_box.pack()
    
    #place box frame
    place_box= Frame(root)
    place_label= Label(place_box, text='Enter a place: ')
    place_label.pack(side= LEFT)
    place_entry= Entry(place_box, width=20)
    place_entry.pack(side= RIGHT)
    place_box.pack()

    #food box frame
    food_box= Frame(root)
    food_label= Label(food_box, text='Enter a food: ')
    food_label.pack(side= LEFT)
    food_entry= Entry(food_box, width=20)
    food_entry.pack(side= RIGHT)
    food_box.pack()


    #create button and text area for presenting response
    show_button = Button(root, text="Show MadLib", command = show)
    show_button.pack()
    display = Text(root)
    display.pack()

    #create button to clear all entries and madlib display
    mybutton= Button(root, text= "Clear", command= clear)
    mybutton.pack()

    root.mainloop()

def show():
    'event handler for pressing show button'
    lst_strings=['snowboarding', 'swimming','skateboarding'] #creates list of string
    random_str= random.choice(lst_strings) #select random string
    first_name=name_entry.get()
    place= place_entry.get()
    food= food_entry.get()
    display.delete(1.0, END)
    display.insert(END, f'{first_name} went to {place} and had a blast eating {food} while {random_str}!')
    #create story and display

def clear():
    'clears all entries and display'
    name_entry.delete(0, END) #clears name, place, food entries
    place_entry.delete(0, END)
    food_entry.delete(0, END)
    display.delete(1.0, END) #clears madlib display

    
madlib()

    

    
