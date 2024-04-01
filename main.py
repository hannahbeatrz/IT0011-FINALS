import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import database

''' open and run database.py first to create the database and table 
    before running this file
    
    (optional) install the following packages if not yet installed:
    pip install customtkinter
    pip install matplotlib
'''

# INITIALIZATION OF TKINTER WINDOW, SETTING ATTRIBUTES, AND ADDING BACKGROUND IMAGE
app = customtkinter.CTk()
app.title('Liquor Inventory System')
app.geometry('1000x550')
app.config(bg='#0A0B0C')
app.resizable(False, False)

font1 = ('Arial', 25, 'bold')
font2 = ('Arial', 18, 'bold')
font3 = ('Arial', 13, 'bold')

background_image = Image.open('Images/bg-img.jpg')
background_image = ImageTk.PhotoImage(background_image)

background_label = Label(app, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# BUTTON FUNCTIONS/COMMANDS
def display_data(event):
    selected_item = tree.focus()
    if selected_item:
        row = tree.item(selected_item)['values']
        clear()
        id_entry.insert(0, row[0])
        name_entry.insert(0, row[1])
        stock_entry.insert(0, row[2])
    else:
        pass

def add_to_treeview():
    products = database.fetch_products()
    tree.delete(*tree.get_children())
    for product in products:
        tree.insert('', END, values=product)

def clear(*clicked):
    if clicked:
        tree.selection_remove(tree.focus())
        tree.focus('')
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    stock_entry.delete(0, END)
    
def delete():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error', 'Please select a product to delete')
    else:
        id = id_entry.get()
        database.delete_product(id)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success', 'Product deleted successfully')
        
def update():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showerror('Error', 'Please select a product to update')
    else:
        id = id_entry.get()
        name = name_entry.get()
        stock = stock_entry.get()    
        database.update_product(name, stock, id)
        add_to_treeview()
        clear()
        messagebox.showinfo('Success', 'Product updated successfully') 

def insert():
    id = id_entry.get()
    name = name_entry.get()
    stock = stock_entry.get()
    
    if not (id and name and stock):
        messagebox.showerror('Error', 'Please fill in all fields')
        return
    elif database.id_exists(id):
        messagebox.showerror('Error', 'ID already exists')
        return
    else:
        try:
            stock_value = int(stock)
            database.insert_product(id, name, stock_value)
            add_to_treeview()
            clear()
            messagebox.showinfo('Success', 'Product added successfully')
        except ValueError:
            messagebox.showerror('Error', 'Stock must be an integer')
            return

# START OF PRODUCT DETAILS FRAME
title_label = customtkinter.CTkLabel(app, font=font2, text='Product Details', text_color='white', bg_color='#0A0B0C')
title_label.place(x=190, y=30)

frame = customtkinter.CTkFrame(app, bg_color='#0A0B0C', fg_color='#1B1B21', corner_radius=10, border_width=2, border_color='white', width=300, height=310)
frame.place(x=100, y=70)

original_image = Image.open('Images/liquor.png')
image_width, image_height = original_image.size
max_width = 150
max_height = 300 
if image_width > max_width or image_height > max_height:
    original_image.thumbnail((max_width, max_height))
image = ImageTk.PhotoImage(original_image)

image_label = Label(frame, image=image, bg='#1B1B21')
image_label.image = image 
image_label.place(x=75, y=5)

id_label = customtkinter.CTkLabel(frame, font=font2, text='Liquor ID:', text_color='white', bg_color='#1B1B21')
id_label.place(x=110, y=85)

id_entry = customtkinter.CTkEntry(frame, font=font2, text_color='black', fg_color='white', border_color='#B2016C', border_width=2, width=260)
id_entry.place(x=20, y=110)

name_label = customtkinter.CTkLabel(frame, font=font2, text='Liquor Name:', text_color='white', bg_color='#1B1B21')
name_label.place(x=90, y=158)

name_entry = customtkinter.CTkEntry(frame, font=font2, text_color='black', fg_color='white', border_color='#B2016C', border_width=2,  width=260)
name_entry.place(x=20, y=185)

stock_label = customtkinter.CTkLabel(frame, font=font2, text='In Stock:', text_color='white', bg_color='#1B1B21')
stock_label.place(x=110, y=223)

stock_entry = customtkinter.CTkEntry(frame, font=font2, text_color='black', fg_color='white', border_color='#B2016C', border_width=2,  width=260)
stock_entry.place(x=20, y=250)

# START OF BUTTON CONTAINER
button_container = customtkinter.CTkFrame(app, bg_color='#0A0B0C', fg_color='#1B1B21', corner_radius=10, border_width=2, border_color='white', width=300, height=120)
button_container.place(x=100, y=400)

add_button = customtkinter.CTkButton(button_container, command=insert, font=font2, text='Add', text_color='white', fg_color='#047E43', hover_color='#025B30', bg_color='#1B1B21', cursor='hand2', corner_radius=8, width=120)
add_button.place(x=20, y=20)

clear_button = customtkinter.CTkButton(button_container, command=lambda:clear(True), font=font2, text='Clear', text_color='white', fg_color='#E93E05', hover_color='#A82A00', bg_color='#1B1B21', cursor='hand2', corner_radius=8, width=120)
clear_button.place(x=160, y=20)

update_button = customtkinter.CTkButton(button_container, command=update, font=font2, text='Update', text_color='white', fg_color='#E93E05', hover_color='#A82A00', bg_color='#1B1B21', cursor='hand2', corner_radius=8, width=120)
update_button.place(x=20, y=70)

delete_button = customtkinter.CTkButton(button_container, command=delete, font=font2, text='Delete', text_color='white', fg_color='#D20B02', hover_color='#8F0600', bg_color='#1B1B21', cursor='hand2', corner_radius=8, width=120)
delete_button.place(x=160, y=70)
# END OF BUTTON CONTAINER
# END OF PRODUCT DETAILS FRAME


# START OF DISPLAY INVENTORY FRAME
style = ttk.Style(app)
style.theme_use('clam')
style.configure('Treeview', font=font3, foreground='white', background='#0A0B0C', fieldbackground='#1B1B21',corner_radius='8')
style.map('Treeview', background=[('selected', '#AA04A7')])

# Add border-radius to the Treeview
style.configure('Treeview', relief='solid', borderwidth=2,)

tree = ttk.Treeview(app, height=21, style='Treeview')
tree['columns'] = ('ID', 'Name', 'In Stock')
tree.column('#0', width=0, stretch=tk.NO)
tree.column('ID', anchor=tk.CENTER, width=100)
tree.column('Name', anchor=tk.CENTER, width=300)
tree.column('In Stock', anchor=tk.CENTER, width=100)

tree.heading('ID', text='ID')
tree.heading('Name', text='Name')
tree.heading('In Stock', text='In Stock')

tree.place(x=420, y=70)
tree.bind('<ButtonRelease>', display_data)
# END OF DISPLAY INVENTORY FRAME


add_to_treeview()
app.mainloop()
