# T074 Krishna Chaudhary Cyber Pract 1A

import tkinter as tk

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def cli():
    print("----- Caesar Cipher CLI -----")
    choice = input("1. Encrypt\n2. Decrypt\nEnter Choice: ")
    text = input("Enter Message: ")
    shift = int(input("Enter Shift Value: "))
    if choice == "1":
        print("Encrypted Message:", encrypt(text, shift))
    elif choice == "2":
        print("Decrypted Message:", decrypt(text, shift))
    else:
        print("Invalid Choice")

def gui():
    root = tk.Tk()
    root.title("Caesar Cipher GUI")
    root.geometry("400x350")

    tk.Label(root, text="Message").pack()
    message = tk.Entry(root, width=40)
    message.pack()

    tk.Label(root, text="Shift").pack()
    shift = tk.Entry(root)
    shift.pack()

    output = tk.Label(root, text="", wraplength=350)
    output.pack(pady=20)

    def enc():
        output.config(text="Encrypted: " + encrypt(message.get(), int(shift.get())))

    def dec():
        output.config(text="Decrypted: " + decrypt(message.get(), int(shift.get())))

    tk.Button(root, text="Encrypt", command=enc).pack(pady=5)
    tk.Button(root, text="Decrypt", command=dec).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    mode = input("Select Mode:\n1. CLI\n2. GUI\nEnter Choice: ")
    if mode == "1":
        cli()
    elif mode == "2":
        gui()
