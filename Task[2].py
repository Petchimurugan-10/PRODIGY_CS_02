from tkinter import *            # Import all the classes and functions from the tkinter module
from tkinter import filedialog   # Import the filedialog module for opening file dialogs

# Create the main window (root) and set its size
root = Tk()
root.geometry("600x400")

def encrypt_decrypt_img(action):
    """
    This function handles both encryption and decryption of an image file.
    It takes the action parameter to determine whether to encrypt ('e') or decrypt ('d').
    """
    # Open a file dialog to select a .jpg file
    file1 = filedialog.askopenfile(mode='r', filetypes=[('jpg file', '*.jpg')])
    if file1 is not None:  # Check if a file was selected
        file_name = file1.name  # Get the file name of the selected file
        key = en1.get(1.0, END).strip()  # Get the key entered by the user from the Text widget
        print(file_name, key)

        try:
            key = int(key)  # Attempt to convert the key to an integer
        except ValueError:
            print("Invalid key. Please enter a numeric key.")  # Handle the case where the key is not numeric
            return

        # Open the image file in binary read mode
        with open(file_name, 'rb') as fi:
            img = fi.read()  # Read the entire file content

        img = bytearray(img)  # Convert the image data into a mutable bytearray
        # Perform XOR operation on each byte of the image using the key
        for index, value in enumerate(img):
            img[index] = value ^ key

        # Save the modified image data back to the file in binary write mode
        with open(file_name, 'wb') as fi1:
            fi1.write(img)

        # Print a success message based on the action performed
        if action == "e":
            print("Image encrypted successfully!")
        elif action == "d":
            print("Image decrypted successfully!")

# Create an "Encrypt" button and place it in the window
b1 = Button(root, text="Encrypt", command=lambda: encrypt_decrypt_img("e"))
b1.place(x=50, y=10)

# Create a "Decrypt" button and place it in the window
b2 = Button(root, text="Decrypt", command=lambda: encrypt_decrypt_img("d"))
b2.place(x=150, y=10)

# Create a Text widget for entering the encryption/decryption key and place it in the window
en1 = Text(root, height=1, width=10)
en1.place(x=100, y=50)

# Start the Tkinter event loop
root.mainloop()
