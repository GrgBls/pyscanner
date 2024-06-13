from tinydb import TinyDB, Query
 
db = TinyDB('data.json')
 
Item = Query()
 
flag = 1
 
 
def searchItem(barcode):
    results = db.search(Item.code == barcode)
    if results:
        return(results)
 
    else:
        results = db.search(Item.name == x)
        if results: 
            return(results)
        else:
            return 0
 
def updatePrice(barcode, newPrice):
     results = db.search(Item.code == barcode)
     if results:
         db.update({'price': newPrice}, Item.code == barcode)
         return 1
     else:
         return 0
 
 
def insertItem(barcode, itemName, itemPrice, itemStock):
    results = db.search(Item.code == barcode)
    if results:
        return 0;
    else:
        db.insert({'code': barcode, 'name': itemName, 'price': itemPrice, 'stock': itemStock})
        return 1
 
def removeItem(barcode):
    results = db.search(Item.code == barcode)
    if results:
        db.remove(Item.code == barcode)
        return 0
    else:
        return 1
 
def getItemPrice(barcode):
    results = db.search(Item.code == barcode)
    if results:
        itemPrice = float(results[0]['price'])
        return itemPrice
    else:
        return 0
 
def getItemName(barcode):
    results = db.search(Item.code == barcode)
    if results:
        itemName = results[0]['name']
        return itemName
    else:
        return 0
 
def itemSold(barcode):
    results = db.search(Item.code == barcode)
    if results:
        itemStock = int(results[0]['stock'])
        itemStock = itemStock - 1
        db.update({'stock': str(itemStock)}, Item.code == barcode)
 
def updateStock(barcode, additionalStock):
    results = db.search(Item.code == barcode)
    if results:
        itemStock = int(results[0]['stock'])
        itemStock = itemStock + int(additionalStock)
        db.update({'stock': str(itemStock)}, Item.code == barcode)
        return 0
    else:
        return 1
 
 
 
insertItem("060639121670", "Mango Loco Monster", "1.5", "5")
print(searchItem("060639121670"))
print(getItemPrice("060639121670"))
print(getItemName("060639121670"))
itemSold("060639121670")
print(searchItem("060639121670"))
updateStock("060639121670", "10")
print(searchItem("060639121670"))

