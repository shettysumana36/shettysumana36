def remove_word(str,word):
    str2=str.replace(word,'')
    return str2
str3=("Hello good morning hello good")
print("Before remove")
print(str3)
str4=remove_word(str3,"Hello")
print(str4)