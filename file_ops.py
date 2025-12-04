import tkinter as tk
from tkinter import filedialog

# Stores the path of the currently opened file
current_file = None

def new_file(text_widget, window):
    """
    Create a new empty document.
    Clears the text widget and resets the current file path.
    """
    global current_file
    text_widget.delete("1.0", tk.END) # Remove all text from the editor
    current_file = None # No file is associated with this new document
    window.title("Notepad - New File") # Update window title

def open_file(text_widget, window):
    """
    Open an existing text file and load its contents into the editor.
    """

    global current_file
    path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if path:
        current_file = path # Save the selected file path
        text_widget.delete("1.0", tk.END) # Clear the editor

        # Read the selected file and insert its content into the text widget
        with open(path, "r", encoding="utf-8") as f:
            text_widget.insert(tk.END, f.read())
        window.title(f"Notepad - {path}") # Show file path in the window title

def save_file(text_widget, window):
    """
    Save the current document.
    If no file has been saved yet, open the 'Save As' dialog instead.
    """

    global current_file
    if current_file is None:
        # No file name yet -> require user to choose a location
        save_as_file(text_widget, window)
    else:
        # Save the text directly to the existing file
        with open(current_file, "w", encoding="utf-8") as f:
            f.write(text_widget.get("1.0", tk.END))
        window.title(f"Notepad - {current_file}")

def save_as_file(text_widget, window):
    """
    Save the document under a new name chosen by the user.
    """

    global current_file
    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if path:
        current_file = path # Store the new file path

        # Write the content of the editor into the newly chosen file
        with open(path, "w", encoding="utf-8") as f:
            f.write(text_widget.get("1.0", tk.END))
        window.title(f"Notepad - {path}") # Update window title with new file name
