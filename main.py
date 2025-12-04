from gui import create_gui
from menu_bar import create_menu

# Create the main application window and the text editing widget
window, text_widget = create_gui()
# Create and attach the menu bar to the window
create_menu(window, text_widget)

# Start the Tkinter event loop
window.mainloop()
