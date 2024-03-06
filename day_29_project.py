##Day 30 upgraded code##
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json 
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password_button():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    
    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    
    sym_list = [random.choice(symbols) for _ in range(nr_symbols)]
    
    number_list = [random.choice(numbers) for _ in range(nr_numbers)]
    
    password_list = number_list + sym_list + letter_list
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button():
    global new_data
    
    website_info = website_entry.get()
    email_info =email_entry.get()
    password_info = password_entry.get()
    new_data = {
        website_info: {
            "email": email_info,
            "password": password_info,
        }
    }
    
    if len(website_info) == 0 or len(password_info) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                
        except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
        else:            
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:        
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def search_button():
    website_info = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:            
        if website_info in data:
            email = data[website_info]["email"]
            password = data[website_info]["password"]  
            messagebox.showinfo(title=website_info, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website_info} exists.")
            
    
        
        
    


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)



canvas = Canvas(width=200, height=200,highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image= logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2)
email_entry.insert(0, "exmple@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password",width=14, command= generate_password_button)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add",width=46, command= add_button)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command=search_button)
search_button.grid(column=2, row=1)






window.mainloop()