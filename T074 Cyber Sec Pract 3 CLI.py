#Krishna T074 Cyber Security Pract 3

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

# Function to verify MAC
def verify_mac(message, secret_key, received_mac):
    generated_mac = generate_mac(message, secret_key)
    return hmac.compare_digest(generated_mac, received_mac)

# Main Program
message = input("Enter the message: ")
secret_key = input("Enter the secret key: ")

# Generate MAC
mac = generate_mac(message, secret_key)
print("\nGenerated MAC:", mac)

# Verify MAC
print("\n--- Verification ---")
received_message = input("Enter the received message: ")
received_mac = input("Enter the received MAC: ")

if verify_mac(received_message, secret_key, received_mac):
    print("MAC Verification Successful!")
    print("Message is authentic and has not been modified.")
else:
    print("MAC Verification Failed!")
    print("Message has been altered or the key is incorrect.")    
