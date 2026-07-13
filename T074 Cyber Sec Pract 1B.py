# T074 Krishna Chaudhary Cyber Pract 1B

import math
import tkinter as tk

def encrypt(message, key):
    cipher = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipher[col] += message[pointer]
            pointer += key
    return ''.join(cipher)

def decrypt(cipher, key):
    num_cols = math.ceil(len(cipher) / key)
    num_rows = key
    num_shaded = (num_cols * num_rows) - len(cipher)

    plaintext = [''] * num_cols

    col = 0
    row = 0

    for symbol in cipher:
        plaintext[col] += symbol
        col += 1

        if (col == num_cols) or (col == num_cols - 1 and row >= num_rows - num_shaded):
            col = 0
            row += 1

    return ''.join(plaintext)

def cli():
    print("----- Transposition Cipher CLI -----")
    choice = input("1. Encrypt\n2. Decrypt\nEnter Choice: ")
    text = input("Enter Message: ")
    key = int(input("Enter Key: "))

    if choice == "1":
        print("Encrypted Message:", encrypt(text, key))
    elif choice == "2":
        print("Decrypted Message:", decrypt(text, key))
    else:
        print("Invalid Choice")

def gui():
    root = tk.Tk()
    root.title("Transposition Cipher GUI")
    root.geometry("400x350")

    tk.Label(root, text="Message").pack()
    message = tk.Entry(root, width=40)
    message.pack()

    tk.Label(root, text="Key").pack()
    key = tk.Entry(root)
    key.pack()

    output = tk.Label(root, text="", wraplength=350)
    output.pack(pady=20)

    def enc():
        output.config(text="Encrypted: " + encrypt(message.get(), int(key.get())))

    def dec():
        output.config(text="Decrypted: " + decrypt(message.get(), int(key.get())))

    tk.Button(root, text="Encrypt", command=enc).pack(pady=5)
    tk.Button(root, text="Decrypt", command=dec).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    mode = input("Select Mode:\n1. CLI\n2. GUI\nEnter Choice: ")

    if mode == "1":
        cli()
    elif mode == "2":
        gui()
