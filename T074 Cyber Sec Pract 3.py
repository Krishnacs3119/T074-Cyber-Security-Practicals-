# Krishna T074 Cyber Security Pract 3 (GUI)

import tkinter as tk
from tkinter import messagebox
import hmac
import hashlib

# Function to generate MAC
def generate_mac(message, secret_key):
    mac = hmac.new(
        secret_key.encode(),
        message.encode(),
        hashlib.sha256
    )
    return mac.hexdigest()

# Generate MAC Button
def generate():
    message = message_entry.get()
    secret_key = key_entry.get()

    if message == "" or secret_key == "":
        messagebox.showerror("Error", "Please enter Message and Secret Key.")
        return

    mac = generate_mac(message, secret_key)
    mac_entry.delete(0, tk.END)
    mac_entry.insert(0, mac)

# Verify MAC Button
def verify():
    received_message = received_message_entry.get()
    secret_key = key_entry.get()
    received_mac = received_mac_entry.get()

    if received_message == "" or received_mac == "":
        messagebox.showerror("Error", "Please fill all verification fields.")
        return

    generated_mac = generate_mac(received_message, secret_key)

    if hmac.compare_digest(generated_mac, received_mac):
        messagebox.showinfo("Success", "MAC Verification Successful!\n\nMessage is authentic and has not been modified.")
    else:
        messagebox.showerror("Failed", "MAC Verification Failed!\n\nMessage has been altered or the key is incorrect.")

# GUI Window
root = tk.Tk()
root.title("Message Authentication Code (MAC)")
root.geometry("700x450")
root.resizable(False, False)

# Labels and Entries
tk.Label(root, text="Message:", font=("Arial", 11)).pack(pady=5)
message_entry = tk.Entry(root, width=70)
message_entry.pack()

tk.Label(root, text="Secret Key:", font=("Arial", 11)).pack(pady=5)
key_entry = tk.Entry(root, width=70, show="*")
key_entry.pack()

tk.Button(root, text="Generate MAC", command=generate, bg="green", fg="white").pack(pady=10)

tk.Label(root, text="Generated MAC:", font=("Arial", 11)).pack()
mac_entry = tk.Entry(root, width=70)
mac_entry.pack()

tk.Label(root, text="Received Message:", font=("Arial", 11)).pack(pady=10)
received_message_entry = tk.Entry(root, width=70)
received_message_entry.pack()

tk.Label(root, text="Received MAC:", font=("Arial", 11)).pack(pady=5)
received_mac_entry = tk.Entry(root, width=70)
received_mac_entry.pack()

tk.Button(root, text="Verify MAC", command=verify, bg="blue", fg="white").pack(pady=15)

root.mainloop()
