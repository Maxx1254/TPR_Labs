import pandas as pd

pd.options.display.max_columns = 9
pd.set_option('display.width', 1400)

with open('A.txt') as fileA:
    M1 = float(fileA.readline())
    D1 = float(fileA.readline())
    P1 = float(fileA.readline())
    D2 = float(fileA.readline())
    P2 = float(fileA.readline())

with open('B.txt') as fileB:
    M2 = float(fileB.readline())
    D11 = float(fileB.readline())
    P11 = float(fileB.readline())
    D22 = float(fileB.readline())
    P22 = float(fileB.readline())

with open('C.txt') as fileC:
    P3 = float(fileC.readline())
    P4 = float(fileC.readline())
    P5 = float(fileC.readline())
    P6 = float(fileC.readline())

print('Варіант А')
CD1 = D1 * 5 - M1
print('Будівництво великого заводу: Великий попит:')
print('Чистий дохід:',CD1, '\n')

MZ1 = D2 * 5 - M1
print('Будівництво великого заводу: Малий попит:')
print('Можливі збитки:',MZ1, '\n')

print('Варіант Б')

CD2 = D11 * 5 - M2
print('Будівництво малого заводу: Великий попит:')
print('Чистий дохід:',CD2, '\n')

MZ2 = D22 * 5 - M2
print('Будівництво малого заводу: Малий попит:')
print('Можливі збитки:',MZ2, '\n')

print('Варіант В')
print('Затримка в один рік\n')
CD3 = D1 * 4 - M1
print('Будівництво великого заводу: Великий попит:')
print('Чистий дохід:',CD3, '\n')
MZ3 = D2 * 4 - M1
print('Будівництво великого заводу: Малий попит:')
print('Можливі збитки:',MZ3, '\n')
CD4 = D11 * 4 - M2
print('Будівництво малого заводу: Великий попит:')
print('Чистий дохід:',CD4, '\n')
MZ4 = D22 * 4 - M2
print('Будівництво малого заводу: Малий попит:')
print('Можливі збитки:',MZ4, '\n')

NVPA = 0.8 * CD1 + 0.2 * MZ1
NVPA = round(NVPA,2)
print('Результат прибутку Варіанту А:', NVPA, 'тис.грн', '\n')

NVPB = 0.8 * CD2 + 0.2 * MZ2
NVPB = round(NVPB,2)
print('Результат прибутку Варіанту Б:', NVPB, 'тис.грн', '\n')

NVPCA = 0.7*((0.9*CD3)+(0.1*MZ3))-(0.3*M1)
NVPCA = round(NVPCA,2)
print('Результат прибутку Варіанту В(А):', NVPCA, 'тис.грн', '\n')

NVPCB = 0.7*((0.9*CD4)+(0.1*MZ4))-(0.3*M2)
NVPCB = round(NVPCB,2)
print('Результат прибутку Варіанту В(Б):', NVPCB, 'тис.грн', '\n')

if (NVPA > NVPB and NVPA > NVPCA and NVPA > NVPCB):
    print('Найкраща стратегія - Варіант А\n')
elif (NVPB > NVPA and NVPB > NVPCA and NVPB > NVPCB):
    print('Найкраща стратегія - Варіант Б\n')
elif (NVPCA > NVPA and NVPCA > NVPB or NVPCB > NVPB and NVPCB > NVPA):
    print('Найкраща стратегія - Варіант В\n')
else:
    print('Не вдалось вибрати ідеальну стратегію!\n')

print(M1, M2, CD3, CD4, MZ3, MZ4)
