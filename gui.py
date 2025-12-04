import tkinter as tk

def create_gui():
    # Create the main application window
    window = tk.Tk()
    window.title("Notepad") # Set the window title
    window.geometry("600x500") # Set the initial window size

    # Create the main text editing area
    text_widget = tk.Text(window)

    # Make the text widget fill the entire window and resize with it
    text_widget.pack(fill="both", expand=True)

    # Return the window and text widget so other modules can use them
    return window, text_widget