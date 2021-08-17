test= [[]]
test2=['a']
test.append(test2)
for i in range(10):
    # test[i],test[-1] = test[-1], test[i]
    if test2 not in test:
        test.append(test2)
print(test)