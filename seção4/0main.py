from seção4.classes.cp import ContaPoupanca
from seção4.classes.cc import ContaCorrente

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(100)
cp.sacar(50)
cp.sacar(50)
cp.sacar(50)
print('###########################')

cc = ContaCorrente(1111, 3333, 0,)
cc.depositar(50)
cc.sacar(25)
cc.sacar(25)
cc.sacar(25)