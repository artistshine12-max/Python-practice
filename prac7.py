#Some important and commonly used string functions:
#1. To measure the length of string
a="I am happy."
print(len(a))
#2. To check whether a string enters with a specific phrase or letter
print(a.endswith("."))
print(a.endswith("ppy."))
#3. To count the total no. of occurences of a character i a string.
print(a.count("p"))
#4.To capitalize the first character of the string.
b="abcd"
print(b.capitalize())
#5.To find a word in the string and print the index of its first occurence
print(a.find("am"))
