lst = ["Chuks","Ada","Henry","Benita"]
def remv(param):
    """This is a function to remove the first and last"""
    param.pop(0)
    param.pop()
    return param

NEW_LIST = remv(lst)
print(NEW_LIST)