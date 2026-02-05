# input truth table 

B = list(map(lambda x: x.lower() in ("true", "1"), input().split()))

if B[1]:
    print(B[1])


lenght = len(B)
b = 0

while lenght > 1:
    b += 1
    lenght /= 2

def negater(index, freq, switch):
    if index >= freq and (index % freq == 0):
        return not switch
    return switch

def create_truth_table(a):

    truth_table = []

    for i in range(a):
        row = []
        f = 2**(a-1-i)
        sw = True
        
        for j in range(2**a):
            row.append(sw)
            sw = negater(j+1, f, sw)
        
        truth_table.append(row)
            
    return truth_table

A = create_truth_table(b)
A.append(B)
lti = next((i for i in range(len(B)-1, -1, -1) if B[i]), None)

for i in range(2**b):
    
    if not A[b][i]:
        continue
    
    print("(", end="")
    
    for j in range(b):
        if A[j][i]:
            print(chr(97+j), end="")
        else:
            print("¬"+chr(97+j), end="")
        if j < b-1:
            print(" ∧ ", end="")
    
    print(")", end="")
    
    if i < lti:
        print(" ∨ ", end="")
