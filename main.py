import string
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
from cryptography.fernet import Fernet
import os
# ---------------------------- GENERATE KEY ------------------------------- #

def generate_and_save_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists("key.key"):
        generate_and_save_key()
    with open("key.key", "rb") as key_file:
        return key_file.read()
key = load_key()
cipher = Fernet(key)

def encrypt_password(password):
    return cipher.encrypt(password.encode())

def decrypt_password(encrypted_password):
    return cipher.decrypt(encrypted_password).decode()

def retrieve_password():
    website_name = website.get()
    if len(website_name) == 0:
        messagebox.showerror("Error", "Please enter a website to retrieve a password.")
    else:
        with open("data.txt", "r") as file:
            for line in file:
                web, user, enc_pass = line.strip().split(" | ")
                if web == website_name:
                    dec_pass = decrypt_password(enc_pass.encode())
                    messagebox.showinfo(
                        title="Password Retrieved",
                        message=f"Website{web}\nEmail: {user}\nPassword: {dec_pass}"
                    )
                    pyperclip.copy(dec_pass)

                    return
            messagebox.showerror("Error", "No details for the website found.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pass_gen():
    length = 13
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    generated_pass = ''.join(random.choices(chars, k=length))
    password_entry.delete(0, END)
    password_entry.insert(0, generated_pass)
    pyperclip.copy(generated_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    user_info = user_entry.get()
    web_info = website.get()
    pass_info = password_entry.get()

    if len(user_info) == 0 or len(web_info) == 0 or len(pass_info) == 0:
        messagebox.showerror("Error", "Entry is empty.")
    else:
        encrypted_pass = encrypt_password(pass_info)
        is_ok = messagebox.askokcancel(title=web_info,
                                       message=f"These are the details entered:\nEmail {user_info} \nPassword: {pass_info} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{web_info} | {user_info} | {encrypted_pass.decode()}\n" )
                website.delete(0, END)
                password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
pic_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100,  image=pic_png)
canvas.grid(column= 2, row=1)



website_text = Label(text="Website", font=("Arial", 13, "normal"))
website_text.grid(column=1, row=3)
website = Entry(width=50)
website.focus()
website.grid(column=2, row=3)


user = Label(text="Email/Username:", font=("Arial", 13, "normal"))
user.grid(column=1, row=4)
user_entry = Entry(width=50)
user_entry.grid(column=2, row=4)
user_entry.insert(0, "Youremail@gmail.com")

password = Label(text="Password:", font=("Arial", 13, "normal"))
password.grid(column=1, row=5)
password_entry = Entry(width=50)
password_entry.grid(column=2, row=5)


gen_pass_button = Button(text="Generate Password", width=20, height=1, command=pass_gen)
gen_pass_button.grid(column= 3, row=5)

add_pass = Button(text="Add", width=43, height=1, command=save_password)
add_pass.grid(column=2, row=6)



retrieve_pass = Button(text="Retrieve Password", width=20, height=1, command=retrieve_password)
retrieve_pass.grid(column=3, row=6)





window.mainloop()
