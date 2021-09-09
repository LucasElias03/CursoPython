
hora = input('Que hora são? ')

if hora.isdigit():
   hora = float(hora)

   if hora >= 0 and hora <= 23:
       if hora <= 11:
           print('Bom Dia')
       elif hora <= 17:
           print('Boa Tarde')
       else:
           print('Boa Noite')
   else:
       print(f'O horario deve esta entre (0, 23): ')


else:
     print('"ERROR" Digite um horario !!!')


