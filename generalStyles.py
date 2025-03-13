from tkinter import ttk

#This is supposed to be a static class with static instance of "Style" object.
#Equivalent to a CSS file.

#staticStyles must be placed within module function and exported. Can't be put in file by itself or creates another window.

#How to write: style.configure(firstArg = tag OR className.widgetType, styling)
def getStyle():

    style = ttk.Style()

    #Theme for the root. Themes: ("clam", "alt", "default", "classic")
    #https://wiki.tcl-lang.org/page/List+of+ttk+Themes
    style.theme_use("clam")


    style.configure("TButton", font=("Arial", 14), foreground="white", background="blue")
    style.configure("TFrame", background = "#939478")
    return style

