from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship, JSON

#TABLA DE USUARIOS
class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    email: str = Field(unique=True, index=True)
    password_hash: str
    telefono: Optional[str] = None
    es_admin: bool = Field(default=False)
    fecha_registro: datetime = Field(default_factory=datetime.utcnow)

    # Relaciones (Para buscar fácil en Python qué ha hecho este usuario)
    consultas: List["ConsultaIA"] = Relationship(back_populates="usuario")
    pedidos: List["SolicitudPedido"] = Relationship(back_populates="usuario")


class Arreglo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    descripcion: str
    precio: float
    imagen_url: Optional[str] = None
    colores_disponibles: List[str] = Field(default=[], sa_type=JSON)
    stock_disponible: int
    activo: bool = Field(default=True)

    # Relación para buscar fácil en Python las opciones de este arreglo
    # Si eliminas un arreglo del catálogo, sus variaciones se limpian solas 
    variaciones: List["VariacionArreglo"] = Relationship(
        back_populates="producto_principal",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}
    )


# NUEVA TABLA: VARIACIONES O TAMAÑOS COMPLEMENTARIOS
class VariacionArreglo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str              
    precio: float             
    imagen_url: Optional[str] = None
    activo: bool = Field(default=True)

    # Clave foránea
    arreglo_id: int = Field(foreign_key="arreglo.id")

    # Relación inversa para saber a qué producto padre pertenece esta variación
    producto_principal: Arreglo = Relationship(back_populates="variaciones")

#TABLA DE HISTORIAL DE IA
class ConsultaIA(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    usuario_id: Optional[int] = Field(default=None, foreign_key="usuario.id")
    peticion_cliente: str
    respuesta_ia: str
    fecha_consulta: datetime = Field(default_factory=datetime.utcnow)

    # Relaciones
    usuario: Optional[Usuario] = Relationship(back_populates="consultas")
    pedido: Optional["SolicitudPedido"] = Relationship(back_populates="consulta_ia")

#TABLA DE SOLICITUDES DE PEDIDOS
class SolicitudPedido(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="usuario.id")
    consulta_ia_id: Optional[int] = Field(default=None, foreign_key="consultaia.id")
    detalles_personalizacion: Optional[str] = None
    estatus: str = Field(default="Pendiente")  # Pendiente, Preparación, Listo
    fecha_solicitud: datetime = Field(default_factory=datetime.utcnow)

    # Relaciones
    usuario: Usuario = Relationship(back_populates="pedidos")
    consulta_ia: Optional[ConsultaIA] = Relationship(back_populates="pedido")