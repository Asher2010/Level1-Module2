"""
Create a simple calculator app
"""
import tkinter as tk

# TODO Make a calculator app like the one shown in the calculator.png image
#  located in this folder.
#  HINT: you'll need: 2 text fields, 4 buttons, and 1 label

class Calculator(tk.Tk):
    def __init__(self):

        super().__init__()
        self.button = tk.Button(self, text='Add', fg='black',
                                font=('courier new', 16, 'bold'), command=self.on_button_press)
        self.button.place(relx=0.0, rely=0.3, relwidth=0.2, relheight=0.1)

        self.button2 = tk.Button(self, text='Subtract', fg='black',
                                font=('courier new', 16, 'bold'), command=self.on_button_press)
        self.button2.place(relx=0.2, rely=0.3, relwidth=0.3, relheight=0.1)

        self.button3 = tk.Button(self, text='Multiply', fg='black',
                                font=('courier new', 16, 'bold'), command=self.on_button_press)
        self.button3.place(relx=0.5, rely=0.3, relwidth=0.3, relheight=0.1)

        self.button4 = tk.Button(self, text='Divide', fg='black',
                                font=('courier new', 16, 'bold'), command=self.on_button_press)
        self.button4.place(relx=0.8, rely=0.3, relwidth=0.2, relheight=0.1)

    def on_button_press(self):
        pass


        #self.text_field = tk.Entry(self)
        #self.text_field.place(relx=0.1, rely=0.8, relwidth=0.8, height=18)

if __name__ == '__main__':
    app = Calculator()
    app.title('Calculator')
    app.geometry('300x300')
    app.mainloop()
