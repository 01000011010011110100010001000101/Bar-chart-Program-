import numpy as np, random
List = []
for i in range(5):
    List.append(random.randint(0,5))

print(List)

def Biggest(List):
    BIGGEST = List[0]

    for i in range(len(List)):
        if BIGGEST < List[i]:
            BIGGEST = List[i]

    return BIGGEST


def Matrix(Biggest, List):
    hight = Biggest(List)
    length = len(List)
    Matrix = np.full((hight, length), ' ')

    for i in range(length):
        Number = List[i]
        for j in range(hight-1,(hight-1)-Number,-1):
                
            
            Matrix[j][i] = "#"
            
    return Matrix


print(Matrix(Biggest, List))