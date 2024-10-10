products=[]
#product=[]

def add_product(id,name,category,price):
    #for i in (id,name,category,price):
    product=[id,name,category,price]
    products.append(product)
    print(id," product is added")

#3.delete products
def del_product(id):
    for product in products:
        if id in product:
            products.remove(product)
            print("product deleted successfully")
        else:
            print("not found")

#2.update product
def update_product(id,name,category,price):
    for product in products :
        if product[0]==id:
            if name:
                product[1]=name
            if category:
                product[2]=category
            if price:
                product[3]=price
            return "product updated successfully"
    return "product not found"



#4.get product by id:
def get_product(id):
    for product in products:
        if product[0]==id:
            return product
    return "product not found"

#5.get all products
def get_all_products():
    return products

#6.get product by category
def get_productbycat(category):
    count=0
    for product in products:
        if product[2]==category:
            count+=1
            print(product)
    if(count==0):
        print("no element")

#7.get product between prices
def get_productprices(a,b):
    count=0
    for product in products:
        if a<=product[3]<=b:
            count+=1
            print(product)
            
    if(count==0):
        print("no element")


while(True):
    print("PRODUCT APPLICATION  \n 1.add product \n 2.update product \n 3.delete product \n 4.get product by pid \n 5.get all products \n 6.get product by category \n 7.get product between prices")
    match=int(input("enter: "))
    if(match==1 or match==2):
    
        id=int(input("enter product id: "))
        name=input("enter the product name: ")
        category=input("enter category: ")
        price=int(input("enter the price of product: "))
    #add product2
    if(match==1):
        add_product(id,name,category,price)
        print(products)
    #delete product
    else:
        update_product(id,name,category,price)
        print(products)
    if(match==3):
        id=int(input("enter id: "))
        del_product(id)
        print(products)
    if(match==4):
        id=int(input("enter product id: "))
        print(get_product(id))
        #print(products)
    if(match==5):
        get_all_products()
        #print(products)
    if(match==6):
        category=input("enter category")
        get_productbycat(category)

    if(match==7):
        a,b=map(int,input().split())
        get_productprices(a,b)



    
    

    
        
         

