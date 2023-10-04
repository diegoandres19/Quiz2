
class Hotel:
   
    def anadirHuespedes(lista):
        nombre = input("Ingrese el nombre del huesped: ")
        doc = int(input("Ingrese el documento de identidad del huesped: "))
        habitacion = int(input("Ingrese el numero de la habitacion: "))
        if lista.count(habitacion) == 0:
            lista.append(nombre)
            lista.append(doc)
            lista.append(habitacion)
            print("Se ha añadido el huesped " + nombre + " con documento de identidad " + str(doc) + " a la habitacion " + str(habitacion))
        else:
            print("La habitacion " + str(habitacion) + " ya esta ocupada")
        return lista

    def eliminarHuespedes(lista):
        doc = int(input("Ingrese el documento de identidad del huesped: "))
        if lista.count(doc) == 1:
            posit = lista.index(doc)
            lista.pop(posit)
            lista.pop(posit)
            lista.pop(posit)
            print("Se ha eliminado al huesped con documento de identidad " + str(doc))
        else:
            print("El documento: " + str(doc) + " no esta registrado")
        return lista

    
    def consultarVigentes(lista):
        opt = int(input("Ingrese la opcion (1 Individual y 2 Total): "))
        if opt == 1:
            doc = int(input("Ingrese el documento de identidad del huesped: "))
            if lista.count(doc) == 1:
                posicion = lista.index(doc)
                print("Nombre: " + lista[posicion - 1])
                print("Documento: " + str(lista[posicion]))
                print("Habitacion: " + str(lista[posicion + 1]))
            else:
                print("El documento: " + str(doc) + " no esta registrado")
        elif opt == 2:
            opt = int(input("Ingrese la opcion: "))
            if opt == 1:
                doc = int(input("Ingrese el documento del huesped: "))
                if lista.count(doc) == 1:
                    posicion = lista.index(doc)
                    print("Nombre: " + lista[posicion - 1])
                    print("Documento: " + str(lista[posicion]))
                    print("Habitacion: " + str(lista[posicion + 1]))
                else:
                    print("El documento " + str(doc) + " no esta registrado")
            elif opt == 2:
                for i in range(0, len(lista), 3):
                    print("Nombre: " + lista[i])
                    print("Documento: " + str(lista[i + 1]))
                    print("Habitacion: " + str(lista[i + 2]))
            else:
                print("opcion no valida")
        else:
            print("opcion no valida")
        return lista





    