from tkinter import *
import random
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbol = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_number = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_number + password_symbol + password_letter
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    pyperclip.paste()

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(website_entry.get()) == 0 or len(email_user_name_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo("Empty boxes", "Please do not left any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(),
                                       message=f"There are the details entered:\n"
                                               f" Email: {email_user_name_entry.get()}\n"
                                               f" Password: {password_entry.get()}\n"
                                               f"Is it ok to save?")
        if is_ok:
            try:
                with open("data.txt", "a") as data:
                    data.write(f"{website_entry.get()} | {email_user_name_entry.get()} | {password_entry.get()}\n")
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)
                    messagebox.showinfo("Saving Data", "Data saved successfully")
            except FileNotFoundError:
                messagebox.showerror("Saving Data Error", "File not found")
        else:
            messagebox.showinfo("Cancel saving data", "Data does not saved.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="black")

canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website: ", bg="black", fg="white")
website_label.grid(column=0, row=1)
email_user_name_label = Label(text="Email/Username: ", bg="black", fg="white")
email_user_name_label.grid(column=0, row=2)
password_label = Label(text="Password: ", bg="black", fg="white")
password_label.grid(column=0, row=3)

# entries
website_entry = Entry(width=34)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_user_name_entry = Entry(width=34)
email_user_name_entry.grid(column=1, row=2, columnspan=2)
email_user_name_entry.insert(0, "mustafatima67@gmail.com")
password_entry = Entry(width=34)
password_entry.grid(column=1, row=3, columnspan=2)

# buttons
password_gen_button = Button(text="Generate password", width=20, command=generate_password)
password_gen_button.grid(column=1, row=4, columnspan=2)
add_button = Button(text="Add", width=20, command=save)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()


