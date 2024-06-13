
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

if __name__ == "__main__":
    add_items("red bull", 1.5)
    add_items("monster", 1.2)
    add_items("hell", 0.9)
    add_items("water", 0.5)

    receipt()
    
