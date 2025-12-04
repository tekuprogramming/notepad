import tkinter as tk
import file_ops

def create_menu(window, text_widget):
    """
    Create the main menu bar and attach file-related menu options.
    """
    # Create the main menu bar for the application window
    main_menu = tk.Menu(window)
    window.config(menu=main_menu)

    # Create the "File" menu
    file_menu = tk.Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="File", menu=file_menu)

    # "New" - create a new blank document
    file_menu.add_command(
        label="New",
        command=lambda: file_ops.new_file(text_widget, window)
    )

    # "Open" - open an existing file
    file_menu.add_command(
        label="Open",
        command=lambda: file_ops.open_file(text_widget, window)
    )

    # "Save" - save the current file
    file_menu.add_command(
        label="Save",
        command=lambda: file_ops.save_file(text_widget, window)
    )

    # "Save As" - save the file under a new name
    file_menu.add_command(
        label="Save As",
        command=lambda: file_ops.save_as_file(text_widget, window)
    )