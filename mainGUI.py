from tkinter import ttk
from generalStyles import getStyle

#Holds the actual UI where everything will go and place inside of here.

#Think React-Webdev coding.

class mainGUI:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="#2c3e50")
        self.root.title("SR-16 Graphs")
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()

        #This makes it actually fullsized.
            #self.root.attributes('-fullscreen', True)
        self.root.geometry("%dx%d" % (width, height))

        #Styling for individual widgets found in the styles.py
        style = getStyle()

        button = ttk.Button(root, text="Styled Button")
        button.pack(pady=10)

        self.root.mainloop()
