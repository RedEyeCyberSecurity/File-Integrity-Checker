import hashlib
import os


# Function to calculate hash
def calculate_file_hash(filepath):
    with open(filepath, "rb") as f:
        file_hash = hashlib.sha256()
        while chunk := f.read(4096):
            file_hash.update(chunk)
    return file_hash.hexdigest()


# Main integrity check logic
if __name__ == "__main__":
    file_path = input("Enter the file path to monitor: ")
    original_hash = calculate_file_hash(file_path)
    print(f"Original file hash: {original_hash}")

    while True:
        input("Press Enter to recheck the file integrity...")
        current_hash = calculate_file_hash(file_path)
        if current_hash == original_hash:
            print("[+] File is intact.")
        else:
            print("[!] File tampered with!")
