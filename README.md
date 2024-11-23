# Password-Manager-with-Cryptography
A simple and secure password manager built with Python and the cryptography library. This application allows you to generate, store, and retrieve passwords securely using encryption.

## Feautures
Password Generation: Automatically generate strong passwords.
Password Storage: Securely store passwords using AES encryption (Fernet).
Password Retrieval: Retrieve saved passwords by entering the website name.
Encryption: Passwords are encrypted before being saved to ensure security.
Clipboard Integration: Generated passwords can be copied to the clipboard for convenience.

## Installation
Prerequisites
To use this project, you need to have Python installed on your system. If you don't have Python, you can download it from python.org.

Dependencies
This project uses the following libraries:
cryptography
pyperclip
tkinter (comes pre-installed with Python)
To install the necessary libraries, run the following commands:

pip install cryptography pyperclip

## Usage
Save a Password
Open the app.
Enter the website name, email/username, and password.
Click Add to save the details. The password will be encrypted before being stored.
Retrieve a Password:
Enter the website name for which you want to retrieve the password.
Click Retrieve Password. The decrypted password will be displayed and copied ready to be pasted.
Generate a Random Password
Click Generate Password to create a strong, random password.
The password will be copied to your clipboard for easy use.
Security Notice
Encryption: This project uses Fernet encryption from the cryptography library to securely store passwords.
Key Management: The encryption key (key.key) is stored in the same directory. Make sure to keep this key safe; if it’s lost, the passwords cannot be decrypted.

## SCREENSHOTS
![Starting_screen](https://raw.githubusercontent.com/Kasperk-sudo/Password-Manager-with-Cryptography/refs/heads/main/Screenshots/Screenshot%202024-11-22%20200330.png)
1[Info_screen](https://raw.githubusercontent.com/Kasperk-sudo/Password-Manager-with-Cryptography/refs/heads/main/Screenshots/Screenshot%202024-11-22%20200401.png)
![saved_info_screen](https://raw.githubusercontent.com/Kasperk-sudo/Password-Manager-with-Cryptography/refs/heads/main/Screenshots/Screenshot%202024-11-22%20200418.png)
![data.txt_screen](https://raw.githubusercontent.com/Kasperk-sudo/Password-Manager-with-Cryptography/refs/heads/main/Screenshots/Screenshot%202024-11-22%20200436.png)
![Retrieved_password_screen](https://raw.githubusercontent.com/Kasperk-sudo/Password-Manager-with-Cryptography/refs/heads/main/Screenshots/Screenshot%202024-11-22%20200459.png)
