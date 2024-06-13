from tkinter import *
import database
item_price_list =[]
item_name_list = []
item_price_total=0.0

 
root = Tk()

root.title("Scanner")
root.geometry("1000x562")
 
greeting = Label(text="Scanner")
greeting.config(font=('TkDefaultFont', 44))
greeting.pack()
scanText = Label(text="Enter product's barcode:")
scanText.config(font=('TkDefaultFont', 20))
scanText.place(x=15, y=80)
enterBarcode = Entry(fg="black", bg="gray85", width=40)
enterBarcode.place(x=15, y=120, height=25)
def getManualBarcode():
     ManualBarcode = enterBarcode.get()
     Barcode = int(ManualBarcode)
     
     item_name = database.getItemName(Barcode)
     item_price = database.getItemPrice(Barcode)
     if item_name != 0:
          item_price_list.append(item_price)
          item_name_list.append(item_name)
          database.itemSold(Barcode)

          print(item_name_list)
          print(item_price_list)
     enterBarcode.delete(0,END)
enterbtn = Button(text="Enter", width=10, fg="black", bg="gray85",
                  command= getManualBarcode)
enterbtn.place(x=122, y=150)
scanbtn = Button(text="Scan", width=8, height=3, fg="black", bg="gray85")
scanbtn.place(x=15, y=480)
def edit():
     
     editBox = Toplevel(root)

     editBox.title("edit")
     editBox.geometry("500x281")
 
     Editgreeting = Label(editBox, text="which item would you like to edit")
     Editgreeting.config(font=('TkDefaultFont', 20))
     Editgreeting.pack()
     enteritemtoedit = Entry(editBox, fg="black", bg="gray85", width=40)
     enteritemtoedit.place(x=120, y=50, height=15)
     


    
     AmountText = Label(editBox, text="enter the desired amount")
     AmountText.config(font=('TkDefaultFont', 20))
     AmountText.place(x=120,y=80)
     Amount = Entry(editBox, fg="black", bg="gray85", width=40)
     Amount.place(x=120, y=135, height=15)
     desired_amount=Amount.get()
     itemtoedit = enteritemtoedit.get()
     itemtoedit_name = item_name_list[itemtoedit-1]
     itemtoedit_price = item_price_list[itemtoedit-1]
     if desired_amount == 0:
          item_price_list.pop(int(itemtoedit)-1)
          item_name_list.pop(int(itemtoedit)-1)

editbtn = Button(text="Edit", width=8, height=3, fg="black", bg="gray85",
                 command= edit)
editbtn.place(x=115, y=480)
endbtn = Button(text="End", width=8, height=3, fg="black", bg="gray85")
endbtn.place(x=215, y=480)
databasebtn = Button(text="Database", width=8, height=3, fg="black", bg="gray85")
databasebtn.place(x=315, y=480)

root.mainloop()