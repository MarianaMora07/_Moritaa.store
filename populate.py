from sqlmodel import Session, select, SQLModel  
from database import engine
from models import Arreglo

def insertar_productos_prueba():
    # 1. Creación de tablas físicas si el archivo .db está vacío
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        statement = select(Arreglo)
        existente = session.exec(statement).first()
        
        if existente is not None:
            print("El catálogo ya tiene productos de prueba.")
            return

        # Creación de diseños predeterminados basados en tu marca
        producto1 = Arreglo(
            nombre="Ramo de rosas eternas",
            descripcion="Ramo artesanal estructurado con rosas de listón satinado, ensamblado sobre una estructura firme y envuelto en papel coreano con detalles de lazo y más.",
            precio=25.0,
            imagen_url="/static/imagenes/ramo_rosas_eternas.jpg", # Corregido con barra inicial /
            colores_disponibles=["Morado", "Rosado", "Blanco con Dorado"],
            stock_disponible=5,
            activo=True
        )

        producto2 = Arreglo(
            nombre="Arreglo con tazas",
            descripcion="Arreglo artesanal diseñado sobre base de taza cerámica, con rosas de listón satinado dispuestas en cúpula y detalles decorativos integrados.",
            precio=40.0,
            imagen_url="/static/imagenes/tazas_decoradas.jpg",
            colores_disponibles=["Rojo", "Amarillo", "Morado"], # Modificado para que tenga sentido con la descripción
            stock_disponible=3,
            activo=True
        )

        producto3 = Arreglo(
            nombre="Marco de Recuerdos Personalizado",
            descripcion="Cuadro de madera con fondo personalizado, decoración adaptada a tu momento especial.",
            precio=18.5,
            imagen_url="/static/imagenes/marcos_personalizados.jpg",
            colores_disponibles=["Rosado", "Negro", "Marrón"], 
            stock_disponible=4,
            activo=True
        )

        # Guardar en la base de datos
        session.add(producto1)
        session.add(producto2)
        session.add(producto3)
        session.commit()
        print("¡Catálogo de prueba creado exitosamente! 🌹")

if __name__ == "__main__":
    insertar_productos_prueba()