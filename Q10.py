Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> net_amount = 0
>>> while True:
    str = input ("Enter transaction: ")
    transaction = str.split(" ")

    type = transaction [0]
    amount = int (transaction [1])

    if type=="D" or type=="d":
        net_amount += amount
    elif type=="W" or type=="w":
        net_amount -= amount
    else:
        pass

    str = input ("want to continue (Y for yes) : ")
    if not (str[0] =="Y" or str[0] =="y") :
        break

Enter transaction: D 10000
want to continue (Y for yes) : y
Enter transaction: W 2000
want to continue (Y for yes) : Y 
Enter transaction: W 3000
want to continue (Y for yes) : Y
Enter transaction: D 80000
want to continue (Y for yes) : Y
Enter transaction: W 1000
want to continue (Y for yes) : n
>>> print("Net amount: ", net_amount)
Net amount:  84000
>>> 