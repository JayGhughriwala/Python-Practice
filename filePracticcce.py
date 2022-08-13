# This is a the practice of the file basics we are opening a file in a write mode and then append mode

fIle = open("C:\\Users\\Asus\\AppData\\Roaming\\JetBrains\\PyCharmCE2021.2\\scratches\\scratch.txt", "r")
# print(fIle.read())
#   Now Open in the write mode
# fIle = open("C:\\Users\\Asus\\AppData\\Roaming\\JetBrains\\PyCharmCE2021.2\\scratches\\scratch.txt", "w")
# fIle.write("This is the write mode")
# fIle.close()

#  in write mode you can notice that all previous data is deleted and new data is writtern

#  Now open in the append mode this remain our contain as it is and then we can add new content

fIle = open("C:\\Users\\Asus\\AppData\\Roaming\\JetBrains\\PyCharmCE2021.2\\scratches\\scratch.txt", "a")

fIle.write("\nThis is the append mode")
fIle.write("\nThis is the append mode")
fIle.write("\nThis is the append mode")
fIle.write("\nThis is the append mode")

#  If you wanted to see How many characters are you writing in the file you can use the len() function or use the varible also

#  we also have read and write both modes or another also we can use that according to our need

a = fIle.write("This is the Write mode")
print(a)

fIle.close()
