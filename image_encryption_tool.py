import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
import random

# Function to generate a random key (between 1 and 255)
def generate_key():
    return random.randint(1, 255)

# Save key to a text file
def save_key(key, key_file="key.txt"):
    with open(key_file, "w") as f:
        f.write(str(key))

# Load key from a text file
def load_key(key_file="key.txt"):
    try:
        with open(key_file, "r") as f:
            key = int(f.read().strip())
        return key
    except FileNotFoundError:
        messagebox.showerror("Error", "Key file not found. Please encrypt an image first.")
        return None

# Image encryption function
def encrypt_image(image_path, key, output_path):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    img.save(output_path)

# Decryption function (same logic as encryption)
def decrypt_image(image_path, key, output_path):
    encrypt_image(image_path, key, output_path)

# Open file dialog for selecting an image
def open_file():
    filepath = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")]
    )
    if filepath:
        entry_image_path.delete(0, tk.END)
        entry_image_path.insert(0, filepath)
        display_image(filepath)

# Display image in the GUI
def display_image(image_path):
    img = Image.open(image_path)
    img.thumbnail((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    lbl_image.config(image=img_tk)
    lbl_image.image = img_tk

# Encrypt the image and save the key
def encrypt_action():
    image_path = entry_image_path.get()
    if not os.path.exists(image_path):
        messagebox.showerror("Error", "Image file not found.")
        return

    # Generate a random key
    key = generate_key()

    output_path = entry_output.get()

    # Encrypt the image
    encrypt_image(image_path, key, output_path)
    messagebox.showinfo("Success", f"Image encrypted and saved as {output_path}.")

    # Save the key to a file
    save_key(key)
    messagebox.showinfo("Key Saved", f"Key saved to 'key.txt'. You will need this key for decryption.")
    display_image(output_path)

# Decrypt the image using the key from the file
def decrypt_action():
    image_path = entry_image_path.get()
    if not os.path.exists(image_path):
        messagebox.showerror("Error", "Image file not found.")
        return

    # Load the key from the key file
    key = load_key()
    if key is None:
        return

    output_path = entry_output.get()

    # Decrypt the image
    decrypt_image(image_path, key, output_path)
    messagebox.showinfo("Success", f"Image decrypted and saved as {output_path}.")
    display_image(output_path)

# Create the main window
root = tk.Tk()
root.title("Image Encryption Tool with Auto Key")
root.geometry("500x400")

# Image file selection
lbl_image_path = tk.Label(root, text="Select Image:")
lbl_image_path.pack(pady=5)

entry_image_path = tk.Entry(root, width=40)
entry_image_path.pack(pady=5)

btn_browse = tk.Button(root, text="Browse", command=open_file)
btn_browse.pack(pady=5)

# Image preview
lbl_image = tk.Label(root)
lbl_image.pack(pady=10)

# Output file name
lbl_output = tk.Label(root, text="Output File Name (with extension):")
lbl_output.pack(pady=5)

entry_output = tk.Entry(root, width=40)
entry_output.pack(pady=5)

# Buttons for Encrypt and Decrypt
btn_encrypt = tk.Button(root, text="Encrypt Image", command=encrypt_action)
btn_encrypt.pack(pady=10)

btn_decrypt = tk.Button(root, text="Decrypt Image", command=decrypt_action)
btn_decrypt.pack(pady=10)

# Run the GUI
root.mainloop()
