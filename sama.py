def sama(kata) : 
    for i in range(len(kata)//2):
        if kata[i] != kata[len(kata)-i-1]:
            return False
    return True

#print(sama('radar')) 
#print(sama('kodok')) 
#print(sama('sapi'))