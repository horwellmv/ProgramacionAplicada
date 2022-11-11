
def menu(opciones=[4]):
    try:
        entrada=int(input(" ----->  "))
        for i in opciones:
            if entrada==i:
                return entrada
        return "No es entrada valida."
    except:
        return "No es entrada valida."


# ---------------- MENU PRINCIPAL -----------------
run=True
while run:
    print("\n   MENU PRINCIPAL\n")
    print("1*  Clientes\n2*  Proveedores\n3*  Ventas\n4*  Salir\n")
    
    value=menu([1,2,3,4])

    print(value)
    if value == 1:
        pass
    if value == 2:
        pass
    if value == 3:
        pass
    if value == 4:
        run=False


print("\n--------  PROGRAMA FINALIZADO  --------\n")

