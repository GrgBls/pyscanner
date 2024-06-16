from tkinter import *
import database
import time
import cv2
flag = 0;
from pyzbar.pyzbar import decode
cap=cv2.VideoCapture(0)
bd = cv2.barcode.BarcodeDetector()
item_price_list =[]
item_name_list = []
item_price_total=0.0
roundedTotal = None
depth = 100
receipt_name = None
receipt_price=None
labelNameList=[]
labelPriceList=[]
names=[]
prices=[]
enteritemtoedit=None
editflag=None
counter =0
item = 0
itemprice=0.0
newname=None
new_price=None
Label1=None
Label2=None




 
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

def clickscanbtn():
    global scanedbarcode
    global flag

    flag = 0  

    while True:
        success, img = cap.read()

        if not success:
            break

        for code in decode(img):
            barcode_data = code.data.decode('utf-8')
            enterBarcode.delete(0, END) 
            enterBarcode.insert(0, barcode_data)
            print(barcode_data)
            flag = 1  
            break  

        cv2.imshow("image", img)
        if cv2.waitKey(1) & 0xFF == ord('q') or flag == 1:
            cv2.destroyAllWindows()
            break

          
def getManualBarcode():
     global depth
     global roundedTotal
     global item_price_total
     global receipt_name 
     global receipt_price
     global labelNameList
     global labelPriceList
     global counter
     ManualBarcode = enterBarcode.get()
     Barcode = ManualBarcode
     global names
     global prices 
     print(database.getItemName(ManualBarcode))
     
     item_name = database.getItemName(Barcode)
     item_price = database.getItemPrice(Barcode)
     if item_name != 0:

          database.itemSold(Barcode)
          

          name=database.searchItem(Barcode)[0]['name']
          price=database.searchItem(Barcode)[0]['price']
          

          item_price_total=item_price_total+float(price)
          roundedTotal= str(round(item_price_total,2))
          print(roundedTotal)


          receipt_name= Label(text = name)
          receipt_name.config(font=('TkDefaultFont',18))
          receipt_name.place(x=620,y=depth)
          labelNameList.append(receipt_name)
          names.append(item_name)
          prices.append(price)

          receipt_price=Label(text = price)
          receipt_price.config(font=('TkDefaultFont',18))
          receipt_price.place(x=900,y=depth)
          labelPriceList.append(receipt_price)
          print (depth)

          
          depth = depth+40
          counter=counter+1


          
     enterBarcode.delete(0,END)
enterbtn = Button(text="Enter", width=10, fg="black", bg="gray85",
                  command= getManualBarcode)
enterbtn.place(x=122, y=150)
scanbtn = Button(text="Scan", width=8, height=3, fg="black", bg="gray85",command=clickscanbtn)
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
    
     scanText2.pack()
     enterBarcode2 = Entry(dbWindow, fg="black", bg="gray85", width=40)
    
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
     if database.searchItem(barcode) != 0:
          if searchResults is not None:
               searchResults.config(text='Name: ' + database.searchItem(barcode)[0]['name'] + '  |  Price: ' + database.searchItem(barcode)[0]['price'] + '  |  Stock: ' + database.searchItem(barcode)[0]['stock'])
          else:
               searchResults = Label(dbWindow, text='Name: ' + database.searchItem(barcode)[0]['name'] + '  |  Price: ' + database.searchItem(barcode)[0]['price'] + '  |  Stock: ' + database.searchItem(barcode)[0]['stock'])
               searchResults.config(font=('TkDefaultFont', 20))
               searchResults.pack()
     else:
          if searchResults is not None:
               searchResults.config(text="There is no item with that barcode.")
          else:
               searchResults = Label(dbWindow, text="There is no item with that barcode.")
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
     dbWindow2.destroy()
     global searchResults

     if database.searchItem(barcode) != 0:
          if searchResults is not None:
               searchResults.config(text="There already is an item with that barcode.")
          else:
               searchResults = Label(dbWindow, text="There already is an item with that barcode.")
               searchResults.config(font=('TkDefaultFont', 20))
               searchResults.pack()
     
     else:
          database.insertItem(barcode, name, price, stock)
          if searchResults is not None:
               searchResults.config(text="Item has been added successfully.")
          else:
               searchResults = Label(dbWindow, text="Item has been added successfully.")
               searchResults.config(font=('TkDefaultFont', 20))
               searchResults.pack()



def clickrmvbtn(dbWindow, barcode):
     global searchResults
     if database.searchItem(barcode) == 0:
          if searchResults is not None:
               searchResults.config(text="Requested barcode does not exist.")
          else:
               searchResults = Label(dbWindow, text="Requested barcode does not exist.")
               searchResults.config(font=('TkDefaultFont', 20))
               searchResults.pack()
     
     else:

          database.removeItem(barcode)
     
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
     global searchResults
     dbWindow3.destroy()

     if database.searchItem(barcode) == 0:
          if searchResults is not None:
               searchResults.config(text="Requested barcode does not exist.")
          else:
               searchResults = Label(dbWindow, text="Requested barcode does not exist.")
               searchResults.config(font=('TkDefaultFont', 20))
               searchResults.pack()
     else:
          database.updatePrice(barcode, price)

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
     global searchResults
     dbWindow4.destroy()

     if database.searchItem(barcode) == 0:
          if searchResults is not None:
               searchResults.config(text="Requested barcode does not exist.")
          else:
               searchResults = Label(dbWindow, text="Requested barcode does not exist.")
               searchResults.config(font=('TkDefaultFont', 20))
               searchResults.pack()

     else:

          if searchResults is not None:
               searchResults.config(text="Stock has been updated successfully.")
          else:
               searchResults = Label(dbWindow, text="Stock has been updated successfully.")
               searchResults.config(font=('TkDefaultFont', 20))
               searchResults.pack()


def edit():
     global Amount
     
     editwindow = Toplevel(root)

     editwindow.title("edit")
     editwindow.geometry("500x281")
 
     Editgreeting = Label(editwindow, text="which item would you like to edit")
     Editgreeting.config(font=('TkDefaultFont', 20))
     Editgreeting.pack()
     global enteritemtoedit
     enteritemtoedit = Entry(editwindow, fg="black", bg="gray85", width=40)
     enteritemtoedit.place(x=120, y=50, height=40)
     

     
     


    
     AmountText = Label(editwindow, text="enter the desired amount")
     AmountText.config(font=('TkDefaultFont', 20))
     AmountText.place(x=120,y=80)
     global Amount
     Amount = Entry(editwindow, fg="black", bg="gray85", width=40)
     Amount.place(x=120, y=135, height=32)
     

     global item_name_list
     global item_price_list
     
     
     confirmbtn = Button(editwindow,text="confirm",command=lambda: clickconfirmbtn(labelNameList,labelPriceList,receipt_name,receipt_price))
     confirmbtn.place(x=220,y=180)


 
          

     

editbtn = Button(text="Edit", width=8, height=3, fg="black", bg="gray85",
                 command= edit)
editbtn.place(x=115, y=480)

def clickconfirmbtn(namelist,pricelist,receiptname,receiptprice):
     global item
     global editflag
     
     global itemprice
     global newname,new_price,Label1,Label2
     
     tmp1=enteritemtoedit.get()
     item=int(tmp1)-1
     tmp2=Amount.get()
     amount=int(tmp2)
     i=100

     
     

     itemprice=float(prices[item])
     print (names)
     print("first call")

     
     
     if amount ==0:
          editflag=1
          itemprice=-float(itemprice)
          for receiptname in namelist:
               receiptname.destroy()
          for receiptprice in pricelist:
               receiptprice.destroy()
          namelist=[]
          pricelist=[]
          
               
               
          names.pop(item)
          prices.pop(item)
          print(names)
 
          for name in names:
               newname=Label(root,text=name)
               newname.config(font=('TkDefaultFont',18))
               newname.place(x=620,y=i)
               namelist.append(newname)
               i=i+40    
          i=100
          for price in prices:
               new_price=Label(root,text=price)
               new_price.config(font=('TkDefaultFont',18))
               new_price.place(x=900,y=i)
               pricelist.append(new_price)
               i = i+40
     elif amount != 0:
          editflag=2
          itemprice=float(itemprice)*amount
          namelist[item].destroy()
          pricelist[item].destroy()
          editname=str(amount)+"x "+names[item]
          editprice=round(amount*float(prices[item]),2)
          Label1=Label(root,text=editname)
          Label1.config(font=('TkDefaultFont',18))
          Label1.place(x=620,y=100+40*item)
          namelist[item]=Label1
          Label2=Label(root,text=editprice)
          Label2.config(font=('TkDefaultFont',18))
          Label2.place(x=900,y=100+40*item)
          pricelist[item]=Label2
          
          
          

     


       
def clickendbtn(total,label1,label2,list1,list2): 



     if editflag !=None:


          total=round(float(total)+itemprice,2)
          if editflag == 1:
               for name in list1:
                    name.destroy()
               for price in list2:
                    price.destroy()


               newname.destroy()
               new_price.destroy()
          elif editflag==2:


               Label1.destroy()
               Label2.destroy()
     for label1 in list1:
          label1.destroy()
     for label2 in list2:
          label2.destroy()

     totalprice=Label(text="TOTAL:"+str(total))
     totalprice.config(font=('TkDefaultFont',18))
     totalprice.place(x=785,y=50)
     depth=100
    



     

     print(depth)

     






endbtn = Button(text="End", width=8, height=3, fg="black", bg="gray85",
                command=lambda: clickendbtn(roundedTotal,receipt_name,receipt_price,labelNameList,labelPriceList))

endbtn.place(x=215, y=480)
databasebtn = Button(text="Database", width=8, height=3, fg="black", bg="gray85", command=clickdbbtn)
databasebtn.place(x=315, y=480)


root.mainloop()
