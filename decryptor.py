from cryptography.fernet import Fernet
import os

# Load encryption key
def load_key():
    return open("encryption_key.key", "rb").read()

# Decrypt files in a folder
def decrypt_files(folder_path, key):
    fernet = Fernet(key)
    
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path) and file != "decryptor.py" and file != "encryption_key.key":
            with open(file_path, "rb") as f:
                encrypted_data = f.read()
            
            decrypted_data = fernet.decrypt(encrypted_data)
            
            with open(file_path, "wb") as f:
                f.write(decrypted_data)

# Run decryption
if __name__ == "__main__":
    key = load_key()
    decrypt_files("test_folder", key)
    print("🟢 Files Successfully Decrypted!")
