Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Food(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def getprice(self):
        return self.price
    
    def __str__(self):
        return self.name + ' : ' + str(self.getprice())

  
>>> def buildmenu(names, costs):
    menu = []
    for i in range(len(names)):
        menu.append(Food(names[i], costs[i]))
    return menu

>>> names = ['Tea','Coffee','Cold Coffee', 'Donut', 'Cake', 'Pizza', 'Dosa', 'Vada']
>>> costs = [40, 50, 80, 40, 300, 400, 150, 100]
>>> Foods = buildmenu(names, costs)
>>> n = 1
>>> for el in Foods:
    print(n,'. ', el)
    n = n + 1

    
1 .  Tea : 40
2 .  Coffee : 50
3 .  Cold Coffee : 80
4 .  Donut : 40
5 .  Cake : 300
6 .  Pizza : 400
7 .  Dosa : 150
8 .  Vada : 100
>>> 