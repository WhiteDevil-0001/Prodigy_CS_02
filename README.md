# Image Encryption Tool 

This Python tool allows you to encrypt and decrypt images using pixel manipulation and a graphical user interface (GUI) built with Tkinter. The user provides an image and a key to encrypt or decrypt the image. It supports common image formats like PNG and JPG.

## Features
- Encrypt an image by manipulating its pixels using a user-provided key.
- Decrypt the image using the same key.
- GUI for selecting images and inputting keys.

## Requirements
- Python 3.x
- Pillow library (`pip install pillow`)
- Tkinter (comes pre-installed with most Python installations)

## How to Run
1. Clone the repository:
   git clone https://github.com/WhiteDevil-0001/Prodigy_CS_02.git

2. Install required libraries:
    pip install pillow

3. Navigate to the directory:
    cd Prodigy_CS_02

4. Run the Python script:
    python image_encryption_tool.py

## Usage
Browse for an image file (PNG, JPG, etc.).
Enter an encryption/decryption key (between 1 and 255).
Provide a name for the output file.
Click "Encrypt Image" to encrypt, or "Decrypt Image" to decrypt the file.