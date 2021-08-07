from tkinter import *
from tkinter import messagebox

# create the main App window
age_app = Tk()

# create title for my App
age_app.title("Calculate your Age")

# set dimensions for my App
age_app.geometry("400x200")

# write the age label
text = Label(age_app, text="Please write your age", height=2, font=("Times", 17)).pack()

# aga Var
age = StringVar()

# set default value for age
age.set("00")

# create input for age
age_input = Entry(age_app, width=2, font=("Times", 17), textvariable=age).pack()


def btn_function():
    age_value = age.get()
    months = int(age_value) * 12
    weeks = int(age_value) * 12*4
    days = int(age_value) * 365

    line_one = f"Your age in months is:{months}"
    line_two = f"Your age in weeks is:{weeks}"
    line_three = f"Your age in days is:{days}"

    all_lines = [line_one, line_two, line_three]

    # import messagebox from tkinter to pop up ur result
    messagebox.showinfo("Your age is", "\n".join(all_lines))


# create button to calculate age
btn = Button(age_app, text="Calculate", width=20, height=2,
             bg="#7952b3", fg="white", borderwidth=0, command=btn_function).pack()

# Run App infinitely
age_app.mainloop()

# then >>  to open it in exe file >> pip install pyinstaller >> pyinstaller.exe --onefile calculate_ur_age.py
