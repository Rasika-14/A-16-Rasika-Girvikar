Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Number = int(input("Enter any number to check it is armstrong number or not = "))
Enter any number to check it is armstrong number or not = 407
>>> sum = 0
>>> Temp = Number
>>> while Temp > 0:
	digit = Temp % 10
	sum += digit ** 3
	Temp //=10

	
>>> if Number == sum:
	print(Number,"is an Armstrong number")
else:
	print(Number,"is not an Armstrong number")

	
407 is an Armstrong number
>>> 