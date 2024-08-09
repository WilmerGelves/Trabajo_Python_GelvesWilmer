import funciones.funcionGlobales as globals

def gestionCompras(op : int ):
    title = """
    ***********************
    * MODULO DE SERVICIOS *
    ***********************
    """
    menuS = '\t1.Generar Compra.\n\t2.Salir.'
    globals.borrar_pantalla()
    if (op != 5):
        print(title)
        print(menuS)
        try:
            op = int(input('\t=>'))
        except ValueError:
            print('Opción inválida')
            globals.pausar_pantalla()
            gestionCompras(0)
        else:
            match(op):
                case 1:
                    pass
                case 2:
                    resultado = sv.buscarS()
                    if resultado is None:
                        print('El servicio no fue encontrado...')
                        globals.pausar_pantalla()
                        gestionS(0)
                    else:
                        print(resultado)
                        globals.pausar_pantalla()
                        gestionS(0)
                    
                case 3:
                    sv.modificarS()
                case 4:
                    sv.deleteS()
                case 5:
                    globals.borrar_pantalla()
                    print('Has salido de gestión de Servicios')
                    globals.pausar_pantalla()
                    main.menuPrincipal(0)
                case _:
                    print('Opción inválida...Intente nuevamente.')
                    globals.pausar_pantalla()
                    gestionS(0)
