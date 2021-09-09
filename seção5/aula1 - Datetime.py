from datetime import datetime, timedelta

data = datetime(2021, 8, 31)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

data2 = datetime.strptime('31/08/2021', '%d/%m/%Y')
print(data2)
print(data2.timestamp())

data3 = datetime.fromtimestamp(1630378800.0)
print(data3)


'''
Acrescentar dias
'''
data4 = datetime.strptime('20/08/2021 20:00:00', '%d/%m/%Y %H:%M:%S')
data4 = data4 + timedelta(days=5)
print(data4.strftime('%d/%m/%Y %H:%M:%S'))
