# # function which return reverse of a string
#
# def isPalindrome(s):
# 	return s == s[::-1]
#
#
# # Driver code
# s = "malayalam"
# ans = isPalindrome(s)
#
# if ans:
# 	print(True)
# else:
# 	print(False)
#
#
# # function to check string is
# # palindrome or not
# def isPalindrome(str):
#
# 	# Run loop from 0 to len/2
# 	for i in range(0, int(len(str)/2)):
# 		if str[i] != str[len(str)-i-1]:
# 			return False
# 	return True
#
# # main function
# s = "malayalam"
# ans = isPalindrome(s)
#
# if (ans):
# 	print(True)
# else:
# 	print(False)
#
#
# # function to check string is
# # palindrome or not
# def isPalindrome(s):
# 	# Using predefined function to
# 	# reverse to string print(s)
# 	rev = ''.join(reversed(s))
#
# 	# Checking if both string are
# 	# equal or not
# 	if (s == rev):
# 		return True
# 	return False
#
#
# # main function
# s = "malayalam"
# ans = isPalindrome(s)
#
# if (ans):
# 	print(True)
# else:
# 	print(False)
#
#
# # Python program to check
# # if a string is palindrome
# # or not
#
# x = "malayalam"
#
# w = ""
# for i in x:
# 	w = i + w
#
# if (x == w):
# 	print(True)
# else:
# 	print(False)
#
#
# # Python program to check
# # if a string is palindrome
# # or not
# st = 'malayalam'
# j = -1
# flag = 0
# for i in st:
# 	if i != st[j]:
# 		j = j - 1
# 		flag = 1
# 		break
# 	j = j - 1
# if flag == 1:
# 	print(False)
# else:
# 	print(True)
#
#
# # Recursive function to check if a
# # string is palindrome
#
# def isPalindrome(s):
# 	# to change it the string is similar case
# 	s = s.lower()
# 	# length of s
# 	l = len(s)
#
# 	# if length is less than 2
# 	if l < 2:
# 		return True
#
# 	# If s[0] and s[l-1] are equal
# 	elif s[0] == s[l - 1]:
#
# 		# Call is pallindrome form substring(1,l-1)
# 		return isPalindrome(s[1: l - 1])
#
# 	else:
# 		return False
#
#
# # Driver Code
# s = "MalaYaLam"
# ans = isPalindrome(s)
#
# if ans:
# 	print(True)
#
# else:
# 	print(False)


def is_palindrome(word):
    if len(word) == 1: return True
    if word[0] != word[-1]: return False
    return is_palindrome(word[1:-1])


word = "nepalapen"
print(word[::-1] == word[::1])
