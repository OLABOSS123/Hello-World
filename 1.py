# notQuit = True
# while notQuit == True:
#     text = str(input("Enter an input: "))
#     if text.lower().__eq__("quit"):
#         notQuit = False
#     else:
#         print(text)


def slicer(word, start,stop):
    x = (word[start:stop])
    print (x)

slicer("banana",0,2)
