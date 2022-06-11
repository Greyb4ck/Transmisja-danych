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

s = "aa"

b = string2bits(s)
#print(b)
#flag = true



def haming_coder(code):
    coded = []
    coded.append((code[0] + code[1] + code[3]) % 2)
    coded.append((code[0] + code[2] + code[3]) % 2)
    coded.append(code[0])
    coded.append((code[1] + code[2] + code[3]) % 2)
    coded.append(code[1])
    coded.append(code[2])
    coded.append(code[3])
    return coded


def haming_decoder(code):
    decoded = code
    x1_p = (code[2] + code[4] + code[6]) % 2
    x2_p = (code[2] + code[5] + code[6]) % 2
    x4_p = (code[4] + code[5] + code[6]) % 2
    
    x1_c = (code[0] + x1_p) % 2
    x2_c = (code[1] + x2_p) % 2
    x4_c = (code[3] + x4_p) % 2
    s = (x1_c * 1) + (x2_c * 2) + (x4_c * 4)
    print(s)
    if s > 0:
        decoded[s-1] = not decoded[s-1]
        flag = false
        print("false")
    return (decoded[2],decoded[4],decoded[5],decoded[6])


#t = [1 , 1, 0,1]
#co = haming_coder(t)
#print(t)
#print(co)
#print(haming_decoder(co))
#print(flag)

def haming_coder_1511(code):
    table_words = np.array([[0, 0,0,1],
                            [0, 0,1,0],
                                        [0, 0,1,1],
                            [0, 1,0,0],
                                        [0, 1,0,1],
                                        [0, 1,1,0],
                                        [0, 1,1,1],
                            [1, 0,0,0],
                                        [1, 0,0,1],
                                        [1, 0,1,0],
                                        [1, 0,1,1],
                                        [1, 1,0,0],
                                        [1, 1,0,1],
                                        [1, 1,1,0],
                                        [1, 1,1,1]])

    #print(table_words)
    tablica_p = np.zeros((11,4))
    #print(tablica_p)
    #print(table_words[13][3])
    c=0
    for j in range(0,4):
        for i in range(0,15):
            #if i != 0:
            #   if i != 1:
            #        if i != 3:
            #            if i != 7: 
            if i != 0 and i != 1 and i != 3 and i != 7: 
                            tablica_p[c][j]=table_words[i][j]
                            c += 1
        c=0

    I_k=np.eye(11)
    G = np.hstack(( tablica_p ,I_k))
    
    c = np.dot(code, G)%2
    return c
    



def haming_decoder_1511(code):
    table_words = np.array([[0, 0,0,1],
                            [0, 0,1,0],
                                        [0, 0,1,1],
                            [0, 1,0,0],
                                        [0, 1,0,1],
                                        [0, 1,1,0],
                                        [0, 1,1,1],
                            [1, 0,0,0],
                                        [1, 0,0,1],
                                        [1, 0,1,0],
                                        [1, 0,1,1],
                                        [1, 1,0,0],
                                        [1, 1,0,1],
                                        [1, 1,1,0],
                                        [1, 1,1,1]])

    #print(table_words)
    tablica_p = np.zeros((11,4))
    #print(tablica_p)
    #print(table_words[13][3])
    c=0
    for j in range(0,4):
        for i in range(0,15):
            #if i != 0:
            #   if i != 1:
            #        if i != 3:
            #            if i != 7: 
            if i != 0 and i != 1 and i != 3 and i != 7: 
                            tablica_p[c][j]=table_words[i][j]
                            c += 1
        c=0


        #np.transpose(H)
        #np.transpose(tablica_p)
    I_nk=np.eye(4)
    H = np.hstack((I_nk, np.transpose(tablica_p) ))
    #print(code)
    s = np.dot(code, np.transpose(H)) % 2
    S = 0
    #flag = True

    S = int(s[0] * 1 + s[1] * 2 + s[2] * 4 + s[3] * 8)
    #print(S)
    if S > 0:
        code[S-1] = not code[S-1]
        S = int(s[0] * 1) + int(s[1] * 2) + int(s[2] * 4) + int(s[3] * 8)
        if S > 0:
            print("false")

    code = code[4:]    
    return code



print(b)
data = [1, 0, 1, 0, 1, 0, 0, 1, 1,0, 0 ]
code1 = haming_coder_1511(data)
d_code = haming_decoder_1511(code1)

print(data)
print(code1)
print(d_code)

#print(tablica_p)



