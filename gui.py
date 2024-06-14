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

searchResults = None

def getManualBarcode():
     ManualBarcode = enterBarcode.get()
     Barcode = ManualBarcode

     print(database.getItemName(ManualBarcode))
     
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



def clickdbbtn():
     dbWindow = Toplevel(root)
     dbWindow.title("Database")
     dbWindow.geometry("1000x562")

     greeting2 = Label(dbWindow, text="Database")
     greeting2.config(font=('TkDefaultFont', 20))
     greeting2.pack()

     blankLabel = Label(dbWindow, text=' ') # for space purposes
     blankLabel.pack()

     scanText2 = Label(dbWindow, text="Enter product's barcode: ")
     scanText2.config(font=('TkDefaultFont', 20))
     #scanText2.place(x=350, y=250)
     scanText2.pack()
     enterBarcode2 = Entry(dbWindow, fg="black", bg="gray85", width=40)
     #enterBarcode2.place(x=350, y=290)
     enterBarcode2.pack()

     anotherBlankLabel = Label(dbWindow, text=' ')
     anotherBlankLabel.pack()


     searchbtn = Button(dbWindow, text="Search", width=15, height = 3, fg="black", bg="gray85", command= lambda: clicksearchbtn(dbWindow, enterBarcode2.get()))
     searchbtn.place(x=15, y=490)

     insertbtn = Button(dbWindow, text="Insert", width=15, height = 3, fg="black", bg="gray85", command = lambda: clickinsertbtn(dbWindow, enterBarcode2.get()))
     insertbtn.place(x=145, y=490)
     
     removebtn = Button(dbWindow, text="Remove", width=15, height = 3, fg="black", bg="gray85", command = lambda: clickrmvbtn(dbWindow, enterBarcode2.get()))
     removebtn.place(x=275, y=490)

     updatePricebtn = Button(dbWindow, text="Update Price", width=15, height = 3, fg="black", bg="gray85", command = lambda: clickupdatepricebtn(dbWindow, enterBarcode2.get()))
     updatePricebtn.place(x=405, y=490)
     
     updateStockbtn = Button(dbWindow, text="Update Stock", width=15, height = 3, fg="black", bg="gray85", command = lambda: clickupdatestockbtn(dbWindow, enterBarcode2.get()))
     updateStockbtn.place(x=535, y=490)

def clicksearchbtn(dbWindow, barcode):
     global searchResults
     if searchResults is not None:
          searchResults.config(text='Name: ' + database.searchItem(barcode)[0]['name'] + '  |  Price: ' + database.searchItem(barcode)[0]['price'] + '  |  Stock: ' + database.searchItem(barcode)[0]['stock'])
     else:
          searchResults = Label(dbWindow, text='Name: ' + database.searchItem(barcode)[0]['name'] + '  |  Price: ' + database.searchItem(barcode)[0]['price'] + '  |  Stock: ' + database.searchItem(barcode)[0]['stock'])
          searchResults.config(font=('TkDefaultFont', 20))
          searchResults.pack()

def clickinsertbtn(dbWindow, barcode):
     dbWindow2 = Toplevel(root)
     dbWindow2.title("Insert item")
     dbWindow2.geometry("500x231")

     greeting3 = Label(dbWindow2, text="Insert item")
     greeting3.config(font=('TkDefaultFont', 20))
     greeting3.pack()

     blankLabel = Label(dbWindow2, text=' ') # for space purposes
     blankLabel.pack()

     nameLabel = Label(dbWindow2, text="Name: ")
     nameLabel.place(x=15, y=60)

     enterName = Entry(dbWindow2, fg="black", bg="gray85", width=40)
     enterName.place(x=120, y=60)

     priceLabel = Label(dbWindow2, text="Price: ")
     priceLabel.place(x=15, y=100)

     enterPrice = Entry(dbWindow2, fg="black", bg="gray85", width=40)
     enterPrice.place(x=120, y=100)

     stockLabel = Label(dbWindow2, text="Stock: ")
     stockLabel.place(x=15, y=140)

     enterStock = Entry(dbWindow2, fg="black", bg="gray85", width=40)
     enterStock.place(x=120, y=140)

     submitbtn = Button(dbWindow2, text="Submit", bg="gray85", fg="black", width=20, command=lambda: clicksubmitbtn(dbWindow, dbWindow2, barcode, enterName.get(), enterPrice.get(), enterStock.get()))
     submitbtn.place(x=165, y=180)

def clicksubmitbtn(dbWindow, dbWindow2, barcode, name, price, stock):
     database.insertItem(barcode, name, price, stock)
     dbWindow2.destroy()

     global searchResults
     if searchResults is not None:
          searchResults.config(text="Item has been added successfully.")
     else:
          searchResults = Label(dbWindow, text="Item has been added successfully.")
          searchResults.config(font=('TkDefaultFont', 20))
          searchResults.pack()

def clickrmvbtn(dbWindow, barcode):
     database.removeItem(barcode)
     global searchResults
     if searchResults is not None:
          searchResults.config(text="Item removed successfully.")
     else:
          searchResults = Label(dbWindow, text="Item removed successfully.")
          searchResults.config(font=('TkDefaultFont', 20))
          searchResults.pack()

def clickupdatepricebtn(dbWindow, barcode):
     dbWindow3 = Toplevel(root)
     dbWindow3.title("Update price")
     dbWindow3.geometry("400x200")

     greeting = Label(dbWindow3, text="Update price")
     greeting.config(font=('TkDefaultFont', 20))
     greeting.pack()

     blankLabel = Label(dbWindow3, text=' ') # for space purposes
     blankLabel.pack()

     priceLabel = Label(dbWindow3, text="Price: ")
     priceLabel.place(x=35, y=88)

     enterPrice = Entry(dbWindow3, fg="black", bg="gray85", width=40)
     enterPrice.place(x=90, y=90)

     submitbtn = Button(dbWindow3, text="Submit", bg="gray85", fg="black", width=10, command=lambda: clicksubmitbtn2(dbWindow, dbWindow3, barcode, enterPrice.get()))
     submitbtn.place(x=160, y=160)

def clicksubmitbtn2(dbWindow, dbWindow3, barcode, price):
     database.updatePrice(barcode, price)
     dbWindow3.destroy()

     global searchResults
     if searchResults is not None:
          searchResults.config(text="Price has been updated successfully.")
     else:
          searchResults = Label(dbWindow, text="Price has been updated successfully.")
          searchResults.config(font=('TkDefaultFont', 20))
          searchResults.pack()

def clickupdatestockbtn(dbWindow, barcode):
     dbWindow4 = Toplevel(root)
     dbWindow4.title("Add more stock")
     dbWindow4.geometry("400x200")

     greeting = Label(dbWindow4, text="Add more stock")
     greeting.config(font=('TkDefaultFont', 20))
     greeting.pack()

     blankLabel = Label(dbWindow4, text=' ') # for space purposes
     blankLabel.pack()

     stockLabel = Label(dbWindow4, text="Additional stock: ")
     stockLabel.place(x=15, y=88)

     enterStock = Entry(dbWindow4, fg="black", bg="gray85", width=40)
     enterStock.place(x=130, y=90)

     submitbtn = Button(dbWindow4, text="Submit", bg="gray85", fg="black", width=10, command=lambda: clicksubmitbtn3(dbWindow, dbWindow4, barcode, enterStock.get()))
     submitbtn.place(x=160, y=160)

def clicksubmitbtn3(dbWindow, dbWindow4, barcode, stock):
     database.updateStock(barcode, stock)
     dbWindow4.destroy()

     global searchResults
     if searchResults is not None:
          searchResults.config(text="Stock has been updated successfully.")
     else:
          searchResults = Label(dbWindow, text="Stock has been updated successfully.")
          searchResults.config(font=('TkDefaultFont', 20))
          searchResults.pack()

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
databasebtn = Button(text="Database", width=8, height=3, fg="black", bg="gray85", command=clickdbbtn)
databasebtn.place(x=315, y=480)


root.mainloop()