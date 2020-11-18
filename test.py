spam = ['apples', 'bananas', 'tofu', 'cats']
i = 0
for i in range(len (spam)):
    if i == len(spam) -1:
        print ('and', spam[i])
    elif i == len (spam) -2:
        print (spam [i], end=' ')
    else:
        print (spam [i], end=', ')