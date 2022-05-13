# main.py
from tkinter import *
from tkinter import ttk
import sqlite3

'''
c.execute("""CREATE TABLE Contact (
		ID PRIMARY KEY,
		first_name text,
		last_name text,
		age integer,
		phone_number text,
		address text
		)""")
'''

GUI = Tk()
GUI.geometry('575x425')
GUI.minsize(width=575, height=425)
GUI.maxsize(width=575, height=425)
GUI.title("Contact Books")

conn = sqlite3.connect("contact.db")
c = conn.cursor()

def Submit():
	conn = sqlite3.connect("contact.db")
	c = conn.cursor()

	c.execute("INSERT INTO Contact VALUES (:ID, :f_name, :l_name, :ages, :phone_num, :Add)",
			{
			'ID': Id.get(),
			'f_name': F_name.get(),
			'l_name': L_name.get(),
			'ages': AGE.get(),
			'phone_num': P_num.get(),
			'Add': Add.get()
			})

	F_name.delete(0, END)
	L_name.delete(0, END)
	AGE.delete(0, END)
	P_num.delete(0, END)
	Add.delete(0, END)
	Id.delete(0,END)
	
	conn.commit()
	conn.close()

def Cancel():
	F_name.delete(0, END)
	L_name.delete(0, END)
	AGE.delete(0, END)
	P_num.delete(0, END)
	Add.delete(0, END)
	Id.delete(0,END)

def Show():
	conn = sqlite3.connect("contact.db")
	c = conn.cursor()

	c.execute("SELECT * FROM Contact")
	Record = c.fetchall()

	Name_list.delete(0, END)

	for  Rec in Record:
		print_Record = ""
		print_Record += str(Rec[1]) + " " + str(Rec[2]) + "\t" + str(Rec[0]) + "\n"

		Name_list.insert(END, print_Record)

	conn.commit()
	conn.close()

def Enter():
	conn = sqlite3.connect("contact.db")
	c = conn.cursor()

	c.execute("SELECT * FROM Contact WHERE first_name='%s' " % Search_box.get() )

	Record = c.fetchall()
	Name_list.delete(0, END)

	for  Rec in Record:
		print_Record = ""
		print_Record += str(Rec[1]) + " " + str(Rec[2]) + "\t" + str(Rec[0]) + "\n"

		Name_list.insert(END, print_Record)

	conn.commit()
	conn.close()

def cancel():
	Search_box.delete(0, END)

	Show()

def Del_contact():
	conn = sqlite3.connect("contact.db")
	c = conn.cursor()
	c.execute("DELETE from Contact WHERE ID='%s' " % ID_Delete.get() )

	Name_list.delete(0, END)
	ID_Delete.delete(0, END)

	conn.commit()
	conn.close()

def Contact_Data():
	conn = sqlite3.connect("contact.db")
	c = conn.cursor()
	c.execute("SELECT * FROM Contact WHERE ID='%s' " % Contact_ID_Entry.get() )
	Record = c.fetchall()
	print_Record = ""

	for  Rec in Record:
		print_Record += "ID :" + " " + Rec[0] + "\n"
		print_Record += "First name :" + " " + Rec[1] + "\n"
		print_Record += "Last name :" + " " + Rec[2] + "\n"
		print_Record += "Age :" + " " + str(Rec[3]) + "\n"
		print_Record += "Phone number :" + " " + Rec[4] + "\n"
		print_Record += "Address :" + " " + Rec[5] + "\n"

	Info_Window = Toplevel(GUI)
	Info_Window.geometry("185x115")
	Info_Window.title("Contact information")

	Window_Frame = ttk.LabelFrame(Info_Window)
	Window_Frame.place(x=0, y=0)
	Window_label = ttk.Label(Info_Window, text=print_Record, justify=CENTER)
	Window_label.pack()

	Contact_ID_Entry.delete(0, END)
	
	conn.commit()
	conn.close()

Add_Frame = ttk.LabelFrame(GUI)
Add_Frame.place(x=0, y=0)

Frame = ttk.LabelFrame(Add_Frame, text="Add Contact")
Frame.grid(row=0,rowspan=2, ipady=100, column=1)

ID = ttk.Label(Frame, text="ID number")
First_name = ttk.Label(Frame, text="First name")
Last_name = ttk.Label(Frame, text="Last name")
Age = ttk.Label(Frame, text="Age")
Phone_number = ttk.Label(Frame, text="Phone number")
Address = ttk.Label(Frame, text="Address")
ID.grid(row=5, column=0)
First_name.grid(row=0, column=0)
Last_name.grid(row=1, column=0)
Age.grid(row=2, column=0)
Phone_number.grid(row=3, column=0)
Address.grid(row=4, column=0)

Id = ttk.Entry(Frame)
F_name = ttk.Entry(Frame)
L_name = ttk.Entry(Frame)
AGE = ttk.Entry(Frame)
P_num = ttk.Entry(Frame)
Add = ttk.Entry(Frame)
Id.grid(row=5, column=1)
F_name.grid(row=0, column=1)
L_name.grid(row=1, column=1)
AGE.grid(row=2, column=1)
P_num.grid(row=3, column=1)
Add.grid(row=4, column=1)

Cancel_button = ttk.Button(Frame, text='Cancel', command=Cancel)
Cancel_button.grid(row=6, column=0, ipadx=4)
Submit_button = ttk.Button(Frame, text='Add', command=Submit)
Submit_button.grid(row=6, column=1, ipadx=45)
Show_button = ttk.Button(Frame, text='Update', command=Show)
Show_button.grid(row=7, column=0, columnspan=2, ipadx=90)

Frame1 = ttk.LabelFrame(Add_Frame)
Frame1.grid(row=0, rowspan=2, ipady=100, column=0)

Frame_search = ttk.LabelFrame(Frame1, text='Contact list')
Frame_search.grid(row=0, column=0)
Search_name = ttk.Label(Frame_search, text='Search')
Search_name.grid(row=0, column=0)
Search_box = ttk.Entry(Frame_search)
Search_box.grid(row=0, column=1)
Enter_button = ttk.Button(Frame_search, text='Enter', command=Enter)
Enter_button.grid(row=0, column=2)
cancel_button = ttk.Button(Frame_search, text='Cancel', command=cancel)
cancel_button.grid(row=1, column=1, columnspan=2, ipadx=85)

Frame_list = ttk.LabelFrame(Frame1)
Frame_list.grid(row=1, column=0)
List_scrollbar = Scrollbar(Frame_list, orient=VERTICAL)
Name_list = Listbox(Frame_list, yscrollcommand=List_scrollbar.set)
List_scrollbar.config(command=Name_list.yview)
List_scrollbar.pack(side=RIGHT, fill=Y)
Name_list.pack()

Frame2 = ttk.LabelFrame(Add_Frame, text='Delete Contact')
Frame2.grid(row=1, column=0)
id_Delete = ttk.Label(Frame2, text='Delete ID')
ID_Delete = ttk.Entry(Frame2)
id_Delete.grid(row=0, column=0)
ID_Delete.grid(row=0, column=1)
Del_Button = ttk.Button(Frame2, text='Delete contact', command=Del_contact)
Del_Button.grid(row=2, column=0, columnspan=2, ipadx=54)

Contact_Info_Frame = ttk.LabelFrame(Add_Frame, text='Show information')
Contact_Info_Frame.grid(row=1, column=1)
Label_Contact_ID = ttk.Label(Contact_Info_Frame, text='Contact ID')
Label_Contact_ID.grid(row=0, column=0)
Contact_ID_Entry = ttk.Entry(Contact_Info_Frame)
Contact_ID_Entry.grid(row=0, column=1)
Data_button = ttk.Button(Contact_Info_Frame, text='Show data', command=Contact_Data)
Data_button.grid(row=1, column=0, columnspan=2, ipadx=71)

conn.commit()
conn.close()
GUI.mainloop()