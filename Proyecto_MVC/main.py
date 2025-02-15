from models.Modelo import Tienda
from controllers.Controlador import ControladorTienda
from views.Vista import VistaTienda

if __name__ == "__main__":
    modelo = Tienda()
    modelo.agregar_producto(1, "Manzana", 1.5, 100)
    modelo.agregar_producto(2, "Plátano", 1.0, 150)
    modelo.agregar_producto(3, "Pera", 2.0, 80)

    controlador = ControladorTienda(modelo, None) 
    vista = VistaTienda(controlador)  
    controlador.vista = vista  
