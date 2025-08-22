from tkinter import *
from tkinter.ttk import Progressbar
import tkinter
import tkinter.messagebox
import pyperclip
import secrets, string

no_of_options = 0
length_value = 7


def get_slider_value(value):
    global length_value
    length_value = int(value)
    progress_status()


def progress_status():
    global no_of_options, length_value
    no_of_options = upper_case.get() * 5 + small_case.get() * 5 + special_Chars.get() * 5 + num.get() * 5 + length_value * 5
    length_progress['value'] = no_of_options


def generate_pass():
    global no_of_options, length_value
    password = ""

    switchCode = str(upper_case.get()) + str(small_case.get()) + str(special_Chars.get()) + str(num.get())

    switcher = {
        '1100': generate1,
        '1101': generate2,
        '0001': generate3,
        '1111': generate4,
        '0100': generate5,
        '1000': generate6,
        '0010': generate7,
        '1001': generate8,
        '0101': generate9,
        '1010': generate10,
        '0110': generate11,
        '1110': generate12,
        '0011': generate13,
        '0111': generate14
    }

    password = switcher.get(switchCode, lambda: "Please select atleast one checkbox ")()

    password_entry.delete(0, END)
    password_entry.insert(0, password)


def generate1():
    "Upper and Lower letters"
    try:
        n = int(length_value)
        chars = string.ascii_uppercase + string.ascii_lowercase
        return "".join(secrets.choice(chars) for _ in range(n))
    except:
        return "Invalid length_value"

def generate2():
    "Upper, Lower letters and Numbers"
    try:
        n = int(length_value)
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return "".join(secrets.choice(chars) for _ in range(n))
    except:
        return "Invalid length_value"

def generate3():
    "Numbers only"
    try:
        n = int(length_value)
        chars = string.digits
        return "".join(secrets.choice(chars) for _ in range(n))
    except:
        return "Invalid length_value"

def generate4():
    "Upper, Lower, Numbers and Special characters"
    try:
        n = int(length_value)
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
        return "".join(secrets.choice(chars) for _ in range(n))
    except:
        return "Invalid length_value"

def generate5():
    "Lowercase letters only"
    try:
        n = int(length_value)
        chars = string.ascii_lowercase
        return "".join(secrets.choice(chars) for _ in range(n))
    except:
        return "Invalid length_value"

def generate6():
    "Uppercase letters only"
    try:
        n = int(length_value)
        chars = string.ascii_uppercase
        return "".join(secrets.choice(chars) for _ in range(n))
    except:
        return "Invalid length_value"

def generate7():
    "Special characters only"
    try:
        n = int(length_value)
        chars = string.punctuation
        return "".join(secrets.choice(chars) for _ in range(n))
    except:
        return "Invalid length_value"

def generate8():
    "Uppercase letters and Numbers"
    try:
        n = int(length_value)
        chars = string.ascii_uppercase + string.digits
        return "".join(secrets.choice(chars) for _ in range(n))
    except:
        return "Invalid length_value"

def generate9():
    "Lowercase letters and Numbers"
    try:
        n = int(length_value)
        chars = string.ascii_lowercase + string.digits
        return "".join(secrets.choice(chars) for _ in range(n))
    except:
        return "Invalid length_value"

def generate10():
    "Uppercase letters and Special characters"
    try:
        n = int(length_value)
        chars = string.ascii_uppercase + string.punctuation
        return "".join(secrets.choice(chars) for _ in range(n))
    except:
        return "Invalid length_value"

def generate11():
    "Lowercase letters and Special characters"
    try:
        n = int(length_value)
        chars = string.ascii_lowercase + string.punctuation
        return "".join(secrets.choice(chars) for _ in range(n))
    except:
        return "Invalid length_value"

def generate12():
    "Upper, Lower letters and Special characters"
    try:
        n = int(length_value)
        chars = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
        return "".join(secrets.choice(chars) for _ in range(n))
    except:
        return "Invalid length_value"

def generate13():
    "Numbers and Special characters"
    try:
        n = int(length_value)
        chars = string.digits + string.punctuation
        return "".join(secrets.choice(chars) for _ in range(n))
    except:
        return "Invalid length_value"

def generate14():
    "Lowercase letters, Numbers and Special characters"
    try:
        n = int(length_value)
        chars = string.ascii_lowercase + string.digits + string.punctuation
        return "".join(secrets.choice(chars) for _ in range(n))
    except:
        return "Invalid length_value"



def copyclip():
    passwordcopy = password_entry["text"]
    pyperclip.copy(passwordcopy)


root = Tk()
root.title("TryCatch Password Generator")
root.geometry("700x300")

title = Label(root, text="TryCatch-Password Generator",
              fg="Blue", font=("Arial", 15, 'bold')).place(x=200, y=10)

num = IntVar()
small_case = IntVar()
upper_case = IntVar()
special_Chars = IntVar()
length = IntVar()
password_str = StringVar()

# Checkboxes
C1 = Checkbutton(root, text="A-Z", variable=upper_case, onvalue=1, offvalue=0, command=progress_status)
C1.place(x=100, y=40)
C2 = Checkbutton(root, text="a-z", variable=small_case, onvalue=1, offvalue=0, command=progress_status)
C2.place(x=180, y=40)
C3 = Checkbutton(root, text="0-9", variable=num, onvalue=1, offvalue=0, command=progress_status)
C3.place(x=250, y=40)
C4 = Checkbutton(root, text="special characters", variable=special_Chars, onvalue=1, offvalue=0,
                 command=progress_status)
C4.place(x=320, y=40)

# Length scale
s1 = Scale(root, variable=length,
           from_=7, to=16,
           orient=HORIZONTAL, command=get_slider_value
           )
s1.place(x=550, y=40)
scale_lable = Label(root, text="Length",
                    font=("Arial", 11)).place(x=500, y=40)

strength_lable = Label(root, text="Password Strength",
                       font=("Arial", 12, "bold")).place(x=280, y=80)

# Progressbar to show strength
length_progress = Progressbar(root, orient=HORIZONTAL,
                              length=400, mode='determinate')
length_progress.place(x=150, y=120)

btn = Button(master=root, text="calculate", fg="green",
             font=("Arial", 10, 'bold'), command=generate_pass).place(x=300, y=150)

password_entry = Entry(root, width=30)
password_entry.place(x=220, y=200)

copy_btn = Button(master=root, text="Copy", fg="green",
                  font=("Arial", 10, 'bold'), command=copyclip).place(x=320, y=230)

photo = PhotoImage(file="password.png")
root.iconphoto(False, photo)


root.mainloop()
