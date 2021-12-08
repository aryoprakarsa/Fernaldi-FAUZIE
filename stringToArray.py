def stringToArray(kalimat):
    kata = []
    temp = ""

    for karakter in kalimat:
        if karakter != " ":
            temp += karakter
        else:
            kata.append(temp)
            temp = ""
    
    if(len(temp) != 0):
        kata.append(temp)
        temp = ""

    for i in range(len(kata)):
        temp = []
        for karakter in kata[i]:
            temp.append(karakter)
        kata[i] = temp
        
    return(kata)

#print(stringToArray("saya suka coding"))       