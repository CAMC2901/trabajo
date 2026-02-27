saldo=0
ent=""
while ent!="3":
  try:
      print("tu saldo es:", saldo)
      ent=input("Que desea hacer:\n1.Depositar\n2.Retirar\n3.salir\n")
      if ent =="1":
            deposito=float(input("ingrese la cantidad que va a depositar: "))
            saldo=(saldo)+(deposito)
            print(f"su saldo actual es de: {saldo}")
      elif ent=="2": 
            retiro=float(input("ingrese la cantidad que va a retirar: "))
            if retiro>saldo:
                print("cantidad mayor a su saldo")
            else:
                saldo=saldo-retiro
                print(f"su saldo actual es de: {saldo}")
      elif ent == "3":
            print("saliendo")
  except:
    print("no puede ingresar letras, solo numeros")


  