d1 = {'b' : 100, 'a' : 200}
d2 = {'y' : 300, 'x' : 200}
print("dictionary 1=:" ,d1)
print("dictionary 2=:" ,d2)
d = d1.copy()
d.update(d2)
print("merged dictionary:" ,d)
