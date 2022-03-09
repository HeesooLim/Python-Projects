from tkinter import *

window = Tk()
window.title('Unit Converter')
window.minsize(width=200, height=100)
window.config(padx=10, pady=10)

cm_entry = Entry(width=10)
cm_entry.grid(row=0, column=0)

cm_label = Label(text="cm =")
cm_label.grid(row=0, column=1)

feet_entry = Entry(width=10)
feet_entry.grid(row=0, column=2)

feet_label = Label(text="ft")
feet_label.grid(row=0, column=3)

error_label = Label(text="")
error_label.grid(row=2, columnspan=4)


def to_feet():
    cm_value = cm_entry.get()
    try:
        cm_value = float(cm_value)
        feet_entry.delete(0, END)
        feet_entry.insert(0, string=f"{cm_value * 0.032808}")
    except ValueError:
        error_label["text"] = f"Please enter valid input"


def to_cm():
    feet_value = feet_entry.get()
    try:
        feet_value = float(feet_value)
        cm_entry.delete(0, END)
        cm_entry.insert(0, string=f"{feet_value * 30.48}")
    except ValueError:
        error_label["text"] = f"Please enter valid input"


to_feet_button = Button(text="To feet", command=to_feet)
to_feet_button.grid(row=1, column=0)

to_cm_button = Button(text="To cm", command=to_cm)
to_cm_button.grid(row=1, column=2)
window.mainloop()
