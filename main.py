import funciones.funcionGlobales as globals
import interface.ventas as ventas
def menuPrincipal(op):
    globals.borrar_pantalla()
    encabezdo = """
    **********************
    * Panadería Pan-Camp *
    **********************
    """
    options = '\t1.Venta.\n\t2.Compra.\n\t3.Gestion al pacientes.\n\t4.Salir'
    if (op != 3):
        print(encabezdo)
        print(options)
        try:
            op = int(input('\t=>'))
        except ValueError:
            print('Opción inválida...')
            globals.pausar_pantalla()
            menuPrincipal(0)
        else:
            match (op):
                case 1:
                    ventas.gestionVenta(0)
                case 2: 
                    pass
                case 3: 
                    globals.borrar_pantalla()
                    print('Fue un gusto servirle...Vuelva pronto.')
                    globals.pausar_pantalla()
                case _:
                    globals.borrar_pantalla()
                    print('Está ingresando una opción inválida...Intente nuevamente.')
                    globals.pausar_pantalla()
                    menuPrincipal(0)


if __name__ == '__main__':
    menuPrincipal(0)