from sqlmodel import Session, select, SQLModel  
from database import engine
from models import Arreglo, VariacionArreglo

def insertar_productos_prueba():
    # 1. Creación de tablas físicas si el archivo .db está vacío
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        statement = select(Arreglo)
        existente = session.exec(statement).first()
        
        if existente is not None:
            print("El catálogo ya tiene productos de prueba.")
            return
        
        variaciones_ramo = [
            VariacionArreglo(nombre="Ramo de 1 Rosa Eterna", precio=4.50, imagen_url="/static/imagenes/ramo_1rosa.jpg"),
            VariacionArreglo(nombre="Ramo de 3 Rosas Eternas", precio=8.00, imagen_url="/static/imagenes/ramo_3rosas.jpg"),
            VariacionArreglo(nombre="Ramo de 7 Rosas Eternas", precio=13.00, imagen_url="/static/imagenes/ramo_7rosas.jpg"), 
            VariacionArreglo(nombre="Ramo 3 rosas + globo foil", precio=12.00, imagen_url="/static/imagenes/ramo_rosas_globo.jpg"),
        ]

        # Creación de diseños predeterminados basados en tu marca
        producto1 = Arreglo(
            nombre="Ramo de rosas eternas",
            descripcion="Ramo artesanal estructurado con rosas de listón satinado, ensamblado sobre una estructura firme y envuelto en papel coreano con detalles de lazo y más.",
            precio=25.0,
            imagen_url="/static/imagenes/ramo_rosas_eternas.jpg",
            colores_disponibles=["Morado", "Rosado", "Blanco con Dorado"],
            stock_disponible=5,
            activo=True,
            variaciones=variaciones_ramo
        )
        
        variaciones_tazas = [
            VariacionArreglo(nombre="Taza sencilla con envoltura", precio=10.00, imagen_url="/static/imagenes/taza_sencilla.jpg"),
            VariacionArreglo(nombre="Taza con peluche + globo", precio=18.00, imagen_url="/static/imagenes/tazas_decoracion.png"),
            VariacionArreglo(nombre="Taza con globo + polaroids + peluche", precio=25.00, imagen_url="/static/imagenes/taza_fotos.jpg"),
        ]

        producto2 = Arreglo(
            nombre="Arreglo con tazas",
            descripcion="Arreglo artesanal diseñado sobre base de taza cerámica, con rosas de listón satinado dispuestas en cúpula y detalles decorativos integrados.",
            precio=40.0,
            imagen_url="/static/imagenes/tazas_decoradas.jpg",
            colores_disponibles=["Rojo", "Amarillo", "Morado"], # Modificado para que tenga sentido con la descripción
            stock_disponible=3,
            activo=True,
            variaciones=variaciones_tazas
        )
        
        variaciones_marco = [
        VariacionArreglo(nombre="Marco sencillo", precio=10.00, imagen_url="/static/imagenes/marco_sencillo.jpg"),
        VariacionArreglo(nombre="Marco personalizado 3D", precio=20.00, imagen_url="/static/imagenes/marco_3d.jpg"),
        VariacionArreglo(nombre="Marco con luces led personalizado", precio=20.00, imagen_url="/static/imagenes/marco_led.jpg"),
        ]

        producto3 = Arreglo(
            nombre="Marco de Recuerdos Personalizado",
            descripcion="Cuadro de madera con fondo personalizado, decoración adaptada a tu momento especial.",
            precio=18.5,
            imagen_url="/static/imagenes/marcos_personalizados.jpg",
            colores_disponibles=["Rosado", "Negro", "Marrón"], 
            stock_disponible=4,
            activo=True,
            variaciones=variaciones_marco
        )
        
        variaciones_bouquet = [
        VariacionArreglo(nombre="Bouquet sencillo + globos foil", precio=20.00, imagen_url="/static/imagenes/bouquet_basico.jpg"),
        VariacionArreglo(nombre="Bouquet con lazos globos foil", precio=20.00, imagen_url="/static/imagenes/bouquet_intermedio.jpg"),
        VariacionArreglo(nombre="Bouquet personalizado + globos con helio", precio=30.00, imagen_url="/static/imagenes/bouquet_rosas_helio.jpg"),
        ]
        
        producto4 = Arreglo(
            nombre="Bouquet eterno personalizado",
            descripcion="Arreglo con base redonda o corazón, hecho a mano con rosas de listón satinado y una estructura abierta diseñada para integrar globos, dulces y detalles a gusto del cliente.",
            precio=10.00,
            imagen_url="/static/imagenes/bouquet_eterno.jpg",
            colores_disponibles=["Rosado", "Azul rey", "Morado", "Amarillo"], 
            stock_disponible=4,
            activo=True,
            variaciones=variaciones_bouquet
        )
        
        
        variaciones_fotos = [
        VariacionArreglo(nombre="Ramo fotográfico (6 fotos) + flores", precio=12.00, imagen_url="/static/imagenes/ramo_6fotos.jpg"),
        VariacionArreglo(nombre="Ramo fotográfico (8 fotos) + flores + chocolates", precio=15.00, imagen_url="/static/imagenes/ramo_8fotos.jpg"),
        VariacionArreglo(nombre="Ramo fotográfico (10 fotos) + flores + adicional", precio=20.00, imagen_url="/static/imagenes/bouquet_personalizado.jpg"),
        ]
        
        producto5 = Arreglo(
            nombre="Ramo fotográfico",
            descripcion="Ramo de rosas satinadas, que integra soportes visuales discretos entre las flores para exhibir tus fotografías y recuerdos más preciados.",
            precio=10.00,
            imagen_url="/static/imagenes/ramo_fotografico.jpg",
            colores_disponibles=["Rosado", "Azul rey", "Morado", "Amarillo"], 
            stock_disponible=3,
            activo=True,
            variaciones=variaciones_fotos
        )
        
        variaciones_globos = [
        VariacionArreglo(nombre="Bouquet sencillo", precio=12.00, imagen_url="/static/imagenes/bouquet_facil.jpg"),
        VariacionArreglo(nombre="Bouquet combinación dos colores + color adicional + globos foil", precio=20.00, imagen_url="/static/imagenes/bouquet_sencillo.jpg"),
        VariacionArreglo(nombre="Bouquet personalizado + globos helio", precio=30.00, imagen_url="/static/imagenes/bouquet_helio.jpg"),
        ]

        producto6 = Arreglo(
            nombre="Bouquet de globos personalizado",
            descripcion="Ramo de rosas satinadas, que integra soportes visuales discretos entre las flores para exhibir tus fotografías y recuerdos más preciados.",
            precio=10.00,
            imagen_url="/static/imagenes/bouquet_globos.jpg",
            colores_disponibles=["Rosado","Morado", "Fucsia"], 
            stock_disponible=4,
            activo=True,
            variaciones=variaciones_globos
        )

        # Guardar en la base de datos
        session.add(producto1)
        session.add(producto2)
        session.add(producto3)
        session.add(producto4)
        session.add(producto5)
        session.add(producto6)
        session.commit()
        print("¡Catálogo de prueba creado exitosamente! 🌹")

if __name__ == "__main__":
    insertar_productos_prueba()