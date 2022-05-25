

a=input("Enter you string: ")
palindrome=str(a)
if palindrome==palindrome[::-1]:
	print(palindrome,": Given String is palindrome")
else:
	print(palindrome,": Given String is not palindrome")
