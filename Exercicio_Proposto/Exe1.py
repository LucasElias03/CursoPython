
n1 = input('Digite um número inteiro: ')


try:
   nu_int = int(n1)

   if (nu_int % 2 == 0):
       print(n1,'e um número PAR')
   else:
        print(n1,'e um número IMPAR')
except:
    print(f'({n1}) não e um número inteiro')


