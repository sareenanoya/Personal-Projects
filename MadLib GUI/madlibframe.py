from tkinter import*
import random

class MadLibFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self)

        # name box frame
        name_box = Frame(self)
        name_label = Label(name_box, text = "Enter a name: ")
        name_label.pack(side=LEFT)
        self.name_entry = Entry(name_box, width = 20)
        self.name_entry.pack(side=RIGHT)
        name_box.pack()
    
        #place box frame
        place_box= Frame(self)
        place_label= Label(place_box, text='Enter a place: ')
        place_label.pack(side= LEFT)
        self.place_entry= Entry(place_box, width=20)
        self.place_entry.pack(side= RIGHT)
        place_box.pack()

        #food box frame
        food_box= Frame(self)
        food_label= Label(food_box, text='Enter a food: ')
        food_label.pack(side= LEFT)
        self.food_entry= Entry(food_box, width=20)
        self.food_entry.pack(side= RIGHT)
        food_box.pack()


        #create button and text area for presenting response
        show_button = Button(self, text="Show MadLib", command = self.show)
        show_button.pack()
        self.display = Text(self)
        self.display.pack()

        #create button to clear all entries and madlib display
        mybutton= Button(self, text= "Clear", command= self.clear)
        mybutton.pack()
    

    def show(self):
        'event handler for pressing show button'
        lst_strings=['snowboarding', 'swimming','skateboarding'] #creates list of string
        random_str= random.choice(lst_strings) #select random string
        first_name=self.name_entry.get()
        place= self.place_entry.get()
        food= self.food_entry.get()
        self.display.delete(1.0, END)
        self.display.insert(END, f'{first_name} went to {place} and had a blast eating {food} while {random_str}!')
        #create story and display

    def clear(self):
        'clears all entries and display'
        self.name_entry.delete(0, END) #clears name, place, food entries
        self.place_entry.delete(0, END)
        self.food_entry.delete(0, END)
        self.display.delete(1.0, END) #clears madlib display

    
