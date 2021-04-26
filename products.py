products = []
def read_file(filename):
    import os #載入模組
    if os.path.isfile(filename): #判斷程式有無在路徑內
        print('yes!')
        #讀取商品清單及價格
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                if '商品,價格' in line:
                    continue #繼續
                name,price = line.strip().split(",")
                products.append([name,price])
        print(products)
    else:
        print('Oh, No')
    return products

def user_input(products):
    #使用者輸入商品清單
        while True:
            name = input('請輸入商品名稱: ')
            if name == 'q':
                break
            price = input('請輸入商品價格： ')
        #    p = []
        #    p.append(name)
        #    p.append(price)
        #    p = [name, price]
            products.append([name, price])
        #    products.append(p)
        print(products)
        return products

def print_products(products):
    #印出所有購買清單
    for product in products:
        print(product)

def write_file(filename, products):
    #寫入商品名稱及價格
    with open(filename, "w", encoding="utf-8") as f:
        f.write("商品,價格\n")
        for p in products:
            f.write(p[0]+ "," + str(p[1]) + "\n")
        

products = read_file('produicts.csv')
products = user_input(produicts)
print_products(products)
write_file("produicts.csv", products)