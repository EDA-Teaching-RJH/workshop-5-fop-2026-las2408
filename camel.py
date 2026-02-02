#Camel Case Input
camelCaseName = input("Enter Variable Name: ")
for chr in camelCaseName:
    if chr.isupper():
        print("_" + chr.lower(), end = "")
    else:
        print(chr, end = "")