import funciones.funcionGlobales as globals
import main
def gestionVenta(op : int ):
    title = """
    ***********
    * Compra  *
    ***********
    """
    menuVentas = '\t1.Seleccionar productos.\n\t2.Salir.'
    globals.borrar_pantalla()
    if (op != 2):
        print(title)
        print(menuVentas)
        try:
            op = int(input('\t=>'))
        except ValueError:
            print('Opción inválida')
            globals.pausar_pantalla()
            gestionVenta(0)
        else:
            match(op):
                case 1:
                    pass
                case 2:
                    globals.borrar_pantalla()
                    print('Has salido de gestion venta')
                    globals.pausar_pantalla()
                    main.menuPrincipal(0)
                    
                case _:
                    print('Opción inválida...Intente nuevamente.')
                    globals.pausar_pantalla()
                    gestionVenta(0)
