
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
result = n1 - n2
print(result)
if result < 0:
    print(f'A subtração entre {n1}, {n2} dará um valor NEGATIVO.')
elif result == 0:
    print(f'A subtração entre {n1}, {n2} dará um valor NEUTRO')
else:
    print(f'A subtração entre {n1}, {n2} dará um valor POSITIVO.')






