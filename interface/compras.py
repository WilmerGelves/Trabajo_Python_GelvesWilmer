import funciones.funcionGlobales as globals
import main
def gestionCompra(op : int ):
    title = """
    ***********
    * Compra  *
    ***********
    """
    menuCompra = '\t1.Generar Compra.\n\t2.Salir.'
    globals.borrar_pantalla()
    if (op != 2):
        print(title)
        print(menuCompra)
        try:
            op = int(input('\t=>'))
        except ValueError:
            print('Opción inválida')
            globals.pausar_pantalla()
            gestionCompra(0)
        else:
            match(op):
                case 1:
                    pass
                case 2:
                    globals.borrar_pantalla()
                    print('Has salido de gestion de Compras')
                    globals.pausar_pantalla()
                    main.menuPrincipal(0)
                    
                case _:
                    print('Opción inválida...Intente nuevamente.')
                    globals.pausar_pantalla()
                    gestionCompra(0)
