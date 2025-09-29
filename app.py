from fastapi import FastAPI
from mangum import Mangum # <-- ¡Nueva importación!

# 1. Crear una instancia de FastAPI (igual que antes)
app = FastAPI()

# 2. Definir tus rutas (igual que antes)
@app.get("/")
def read_root():
    """Ruta principal de saludo."""
    return {"mensaje": "¡Hola Mundo! ¡Mi primera API con FastAPI en AWS Lambda!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    """Ruta de ejemplo con parámetros."""
    return {"item_id": item_id, "q": q, "mensaje": "Esto es un ítem específico en Lambda"}


# 3. Definir el handler para AWS Lambda usando Mangum (¡El cambio clave!)
# Mangum toma el objeto 'app' de FastAPI y lo convierte en una función
# que AWS Lambda puede invocar.
handler = Mangum(app)