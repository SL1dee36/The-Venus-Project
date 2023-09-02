import tkinter as tk
from tkinter import font
import customtkinter as ctk
from PIL import Image

root = ctk.CTk()

# Window Display
root.geometry("1200x600")
root.resizable(False,False)
root.title('The Venus')
root.iconbitmap('icons/venus.ico')

#Themes: Light and Night

#Light: Main: #C70039, hover: #900C3F
#Night: Main: #C70039, hover: #900C3F


#(LeftFrame)

MainLabel =ctk.CTkLabel(root, text="VENUS",font=('Cosomos-normal',140),width=300,height=40)
MainLabel.place(x=65, y=40)



button1 = ctk.CTkButton(root, text="New Game",
                        font=('Courier New',20),
                        width=300,height=70,
                        corner_radius=10,
                        hover=True)

button1.place(x=65, y=260)


button2 = ctk.CTkButton(root, text="Settings",
                        font=('Courier New',20),
                        width=300,height=70,
                        corner_radius=10,
                        hover=True)

button2.place(x=65, y=340)

button3 = ctk.CTkButton(root, text="Exit",
                        font=('Courier New',20),
                        width=300,height=70,
                        corner_radius=10,
                        hover=True)

button3.place(x=65, y=420)



# Image (RightFrame)
Image_load = ctk.CTkImage(Image.open(("textures/Venus.png")), size=(512, 512))

image_field = ctk.CTkLabel(root,image=Image_load,text='')
image_field.place(x=600, y=44)

root.mainloop()
