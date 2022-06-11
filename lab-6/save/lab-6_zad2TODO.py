import math
import numpy as np
bina = []
bn = []
def string2bits(s=''):
    for x in s:
        bina.append(bin(ord(x))[2:])
    bits = ''
    for i in range(0,len(bina)):
        bits += bina[i]
    return [int(i) for i in str(bits)]

s = "a"

b = string2bits(s)
#print(b)
#Flag = True



def Haming_Coder(code):
    coded = []
    coded.append((code[0] + code[1] + code[3]) % 2)
    coded.append((code[0] + code[2] + code[3]) % 2)
    coded.append(code[0])
    coded.append((code[1] + code[2] + code[3]) % 2)
    coded.append(code[1])
    coded.append(code[2])
    coded.append(code[3])
    return coded


def Haming_Decoder(code):
    decoded = code
    x1_p = (code[2] + code[4] + code[6]) % 2
    x2_p = (code[2] + code[5] + code[6]) % 2
    x4_p = (code[4] + code[5] + code[6]) % 2
    
    x1_c = (code[0] + x1_p) % 2
    x2_c = (code[1] + x2_p) % 2
    x4_c = (code[3] + x4_p) % 2
    S = (x1_c * 1) + (x2_c * 2) + (x4_c * 4)
    print(S)
    if S > 0:
        decoded[S-1] = not decoded[S-1]
        Flag = False
        print("False")
    return (decoded[2],decoded[4],decoded[5],decoded[6])


#T = [1 , 1, 0,1]
#co = Haming_Coder(T)
#print(T)
#print(co)
#print(Haming_Decoder(co))
#print(Flag)
table_words = np.array([[0, 0,0,1],
                        [0, 0,1,0],
                                    [0, 0,1,1],
                        [0, 1,0,0],
                                    [0, 1,0,1],
                                    [0, 1,1,0],
                                    [0, 1,1,1],
                        [1, 0,0,0],
                                    [1, 0,0,1],
                                    [1, 0,1,1],
                                    [1, 1,0,0],
                                    [1, 1,0,1],
                                    [1, 1,1,0],
                                    [1, 1,1,1]])

#print(table_words)
tablica_P = np.zeros((11,4))
#print(tablica_P)
#print(table_words[13][3])
c=0
for j in range(0,3):
    for i in range(0,14):
        if i != 0 & i != 1 & i != 3 & i != 7: 
            tablica_P[c][j]=table_words[i][j]
            c += 1
    c=0

print(tablica_P)
