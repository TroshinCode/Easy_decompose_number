__version__ = '2.0. Last update: Oct 31, 2019'
__author__ = 'Anton Troshin'
baza = [] 
for k in range(2, 10001):
    position = True
    for s in range(2, k):
        if k%s == 0:
            position = False
            break
 
    if position:
        baza.append(k)
i = int(input('Enter: '))
memory = i
s = []
for x in baza:
    while i%x==0:
        i = i/x
        s.append(x)
        
print(str(memory) + ' = 1',
        *s, sep='*')

if i == 1:
    print('Операция прошла успешно')
else:
    print('Далее Вы должны разложить число, указанное ниже на простые множители самостоятельно,')
    print('и убедиться, что это число составное')
    print('-----')
    print(i)        