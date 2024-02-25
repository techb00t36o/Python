# #Write a Python program to count the number of characters (character frequency) in a string.
# # Sample String : google.com'
# # Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

# str1 = input("Enter your text : ")


# for i in str1:
#     count=0
#     for j in str1:
#         if(i==j):
#             count=count+1
#     temp=count
# k=1
# for i in str1:
#     j=1
#     while(i!=j):
#         print("'",i,"' : ",temp)
str1 = input("Enter your text : ")

# Create an empty dictionary to store character frequencies
char_freq = {}

# Count the frequency of each character in the string
for char in str1:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

# Print the character frequency dictionary
print("Character frequency:")
print(char_freq)

#After so much try finally I solve this code