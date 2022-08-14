print("This is a practice of a file seek and tell")

f = open("scratch.txt", "a+")

# s = f.read()
print(f.readline())
print(f.tell())
f.seek(2)
f.write("This is the append mode written in the file using a seek function")
f.close()