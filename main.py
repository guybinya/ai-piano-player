from piano.ui import setup_ui


def create_gui():
    root = setup_ui()
    # Start the GUI event loop
    root.mainloop()


create_gui()
