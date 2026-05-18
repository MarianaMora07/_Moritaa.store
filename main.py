from fastapi import FastAPI, Request, Form, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlmodel import Session, select 
from database import crear_base_de_datos, get_session
from models import Arreglo  

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Configuramos la carpeta de las plantillas HTML
templates = Jinja2Templates(directory="templates")

# Evento que se ejecuta al iniciar el servidor uvicorn
@app.on_event("startup")
def on_startup():
    crear_base_de_datos()  # crea el archivo .db con las tablas

# Una función simulada para probar el flujo de la IA
def simular_ia(descripcion: str) -> str:
    # Aquí irá la conexión real con el modelo más adelante
    return f"Basado en tu petición ('{descripcion}'), te sugiero una cúpula de vidrio mediana con una rosa eterna principal color rojo carmín, detalles de flores preservadas blancas alrededor y luces LED cálidas para darle un toque mágico."

@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_session)):
    # Buscamos todos los arreglos que estén marcados como activos
    statement = select(Arreglo).where(Arreglo.activo == True)
    arreglos = db.exec(statement).all()
    
    # CORRECCIÓN: Pasamos el 'request' como primer argumento, luego el context
    return templates.TemplateResponse(
        request=request,
        name="index.html", 
        context={"arreglos": arreglos}
    )

@app.post("/ia-sugerencia", response_class=HTMLResponse)
def ia_sugerencia(request: Request, descripcion: str = Form(...)):
    respuesta_texto = simular_ia(descripcion)
    
    html_fragmento = f"""
    <div class="p-6 bg-purple-950/60 rounded-2xl border border-fuchsia-500/30 shadow-2xl space-y-3 anim-scale">
        <h4 class="font-display font-bold text-purple-200 flex items-center gap-2 text-lg">
            <span>✨</span> Propuesta Exclusiva de Diseño
        </h4>
        <p class="text-purple-100/90 leading-relaxed text-sm bg-purple-900/30 p-4 rounded-xl border border-purple-800/40">
            {respuesta_texto}
        </p>
        <div class="text-right">
            <button class="bg-gradient-to-r from-fuchsia-500 to-purple-500 text-white font-bold text-xs px-4 py-2 rounded-lg hover:opacity-90 transition">
                Solicitar este Diseño 🌹
            </button>
        </div>
    </div>
    """
    return HTMLResponse(content=html_fragmento)