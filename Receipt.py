
items=[]
prices=[]


def add_items(name, price):
    items.append(name)
    prices.append(price)

def receipt():
    print ("receipt")
    print ("="*30)
    total=0
    for i in range(len(items)):
        total+=prices[i]
        print(str(items[i])+ ":" + (25-len(str(items[i])))*" "+str(prices[i]))
    print ("="*30)
    print("total:"+20*" "+str(total))
