class Hotel:
    def addHuesped(lista):
        nombre = input("Ingrese el nombre del huesped: ")
        doc = int(input("Ingrese el documento de identidad del huesped: "))
        habitacion = int(input("Ingrese el numero de la habitacion: "))
        if lista.count(habitacion) == 0:
            lista.append(nombre)
            lista.append(doc)
            lista.append(habitacion)
            print(f"Se ha añadido a \"{nombre}\", con documento de identidad {doc}, a la habitación {habitacion}")
        else:
            print(f"La habitación {habitacion} ya está ocupada.")
        return lista

    def eliminarHuesped(lista):
        doc = int(input("Ingrese el documento de identidad del huesped: "))
        if lista.count(doc) == 1:
            posicion = lista.index(doc)
            lista.pop(posicion)
            print(f"Se ha eliminado el huesped con documento de identidad: {doc}")
        else:
            print(f"El documento de identidad \"{doc}\" no esta registrado")
        return lista

    def consulVigentes(lista):
        opt = int(input("Ingrese la opcion (1) para una consulta individual y (2) para una general): "))
        if opt == 1:
            doc = int(input("Ingrese el documento de identidad del huesped: "))
            if lista.count(doc) == 1:
                posicion = lista.index(doc)
                print(f"Nombre: {lista[posicion -1]}")
                print(f"Documento de identidad: {lista[posicion]}")
                print(f"Habitacion: {lista[posicion + 1]}")
            else:
                print(f"El documento de identidad {doc} no esta registrado")
        elif opt == 2:
            for i in range(0, len(lista), 3):
                    print(f"Nombre: {lista[i]}")
                    print(f"Documento de identidad: {lista[i + 1]}" )
                    print(f"Habitacion: {lista[i + 2]}")
            else:
                print("La opcion ingresada no es valida")
        else:
            print("La opcion ingresada no es valida")
        return lista

    def consulHabs(lista):
        opt = int(input("Ingrese la opcion (1) para ver las habitaciones disponibles y (2) para ver las ocupadas: "))
        if opt == 1:
            for i in range(1, 11):
                if lista.count(i) == 0:
                    print(f"Habitacion {i} disponible")
        elif opt == 2:
            for i in range(1, 11):
                if lista.count(i) == 1:
                    print(f"Habitacion {i} ocupada")
        else:
            print("La opcion ingresada no es valida")
        return lista

    def salir(self):
        print("Gracias por Preferirnos")
        return False

    def menu(lista):
        opt = 0
        while opt != 5:
            print("1. Añadir Huesped")
            print("2. Eliminar Huesped")
            print("3. Consultas vigentes por Huesped")
            print("4. Consulta de habitaciones")
            print("5. Salir")
            opt = int(input("Ingrese la opcion: "))
            if opt == 1:
                lista = Hotel.addHuesped(lista)
            elif opt == 2:
                lista = Hotel.eliminarHuesped(lista)
            elif opt == 3:
                lista = Hotel.consulVigentes(lista)
            elif opt == 4:
                lista = Hotel.consulHabs(lista)
            elif opt == 5:
                lista = Hotel.salir(lista)
            else:
                print("Opcion ingresada no valida")

lista = []
lista = Hotel.menu(lista)