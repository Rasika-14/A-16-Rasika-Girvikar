Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Phone(object):
    def __init__(self, phnname, model, price):
        self.phnname = phnname
        self.model = model
        self.price = price
    
    def getprice(self):
        return self.price
    
    def getmodel(self):
        return self.model
    
    def __str__(self):
        return self.phnname + ' : ' + str(self.getmodel()) +'  ::'+  str(self.getprice())

  
>>> def prices(rec, phnname, model, price):
    rec.append(Phone(phnname, model, price))
    return rec

>>> Record = []
>>> x = 'y'
>>> while x == 'y':
    phnname = input('Enter the name of the Phone: ')
    height = input('Enter model number of phone: ')
    model = input('price: ')
    Record = prices(Record, phnname, model, height)
    x = input('Another Phone? y/n: ')

    
Enter the name of the Phone: Redmi Note 9Pro
Enter model number of phone: 233454656867
price: 13999
Another Phone? y/n: y
Enter the name of the Phone: Sumsung A21s
Enter model number of phone: 323445667807
price: 17500
Another Phone? y/n: y
Enter the name of the Phone: Realme
Enter model number of phone: 2357899134
price: 12000
Another Phone? y/n: n
>>> n = 1
>>> for el in Record:
    print(n,'. ', el)
    n = n + 1

    
1 .  Redmi Note 9Pro : 13999  ::233454656867
2 .  Sumsung A21s : 17500  ::323445667807
3 .  Realme : 12000  ::2357899134
>>> 