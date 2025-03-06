#Imports tkinter library as "tk"
import tkinter as tk
import mainGUI

#root.geometry("") sets dimensions
#Use layout to get widgets into GUI
#principle is objects (widgets) inside of master objects (root)




#This allows to only trigger this file if called directly.

if __name__ == "__main__":
    root = tk.Tk()
                #root.resizable(False, False)
    application = mainGUI.mainGUI(root)



