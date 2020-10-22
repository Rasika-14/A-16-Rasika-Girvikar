Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n = int(print(input("Enter number")))
Enter number40
40
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    n = int(print(input("Enter number")))
TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
>>> n = input(print("enter no."))
enter no.
None23
>>> n = int(n)
>>> numbers = {}
>>> for i in range (1,n+1):
	numbers[i] = i * i

	
>>> print(numbers)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400, 21: 441, 22: 484, 23: 529}
>>> 