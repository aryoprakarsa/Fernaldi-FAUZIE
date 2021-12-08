def sum(bil1, bil2 = None):
    if(bil2 != None):
        return (bil1+bil2)
    else:
        return lambda bil2: bil1 + bil2

#print(sum(2,3))
#print(sum(2)(3))