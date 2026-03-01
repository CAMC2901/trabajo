class cuenta:
  def __init__(self, saldo):
        self.saldo=saldo
  def depositar(self, deposito):
    self.saldo=self.saldo+deposito
  def retirar(self, retiro):
    if retiro>self.saldo:
     print("cantidad mayor a su saldo")
    else:
     self.saldo=self.saldo-retiro
  def transferir(self, transferencia, otra_cuenta):
    tasa=transferencia*0.004
    total=transferencia+tasa
    if total> self.saldo:
        if otra_cuenta.saldo > tasa:
            self.saldo = 0
            otra_cuenta.saldo -= tasa
            cuenta_actual.saldo -=transferencia
        else:
         print("saldo insuficiente")
    elif transferencia == self.saldo:
        if otra_cuenta.saldo < tasa:
            print("La otra cuenta no tiene saldo para pagar la comisión")
        else:
            self.saldo = 0
            cuenta_actual.saldo = 0
            otra_cuenta.saldo -= tasa
    else:
     self.saldo -= total

ent=""
saldo_usuario=""
saldo_usuario2=""

try:
    saldo_usuario=float(input("ingrese su saldo de la cuenta de ahorro: "))
    saldo_usuario2=float(input("ingrese su saldo de la cuenta corriente: "))
    ahorro = cuenta(saldo_usuario)
    corriente = cuenta(saldo_usuario2)
    ent=(input("elija su cuenta:\n1.ahorro\n2.corriente\n"))
    if ent=="1":
     cuenta_actual=ahorro
     otra_cuenta=corriente
    elif ent=="2":
      cuenta_actual=corriente
      otra_cuenta=ahorro
    else:
      print("opcion no valida")
except:
   print("no puede ingresar letras, solo numeros")
ent2=""
while ent2!="5":
     try:
        ent2=(input("Que desea hacer:\n1.Depositar\n2.Retirar\n3.transferir\n4.consultar saldo\n5. salir\n"))
        if ent2 =="1":
                deposito=float(input("ingrese la cantidad que va a depositar: "))
                cuenta_actual.depositar(deposito)
                print(f"su saldo actual es de: {cuenta_actual.saldo}")
        elif ent2=="2": 
                retiro=float(input("ingrese la cantidad que va a retirar: "))
                cuenta_actual.retirar(retiro)
                print(f"su saldo actual es de: {cuenta_actual.saldo}")
        elif ent2 == "3":
                transferencia=float(input("ingrese la cantidad que va a transferir: "))
                cuenta_actual.transferir(transferencia, otra_cuenta)
                print(f"su saldo actual es de: {cuenta_actual.saldo}")
        elif ent2=="4":
            print(f"su saldo actual de ahorro es de: {cuenta_actual.saldo}, corriente: {otra_cuenta.saldo}")
        elif ent2=="5":
            print("saliendo")
     except:
        print("no puede ingresar letras, solo numeros")

