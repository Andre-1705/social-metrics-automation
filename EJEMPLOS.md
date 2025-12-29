# Ejemplos de Uso de la API

Este archivo contiene ejemplos prácticos de cómo usar la API de Social Metrics Automation.

## 🚀 Iniciar el Servidor

```powershell
# Activar entorno virtual
.\.venv\Scripts\Activate.ps1

# Iniciar servidor
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

O usar la tarea de VS Code: `Ctrl+Shift+P` → `Tasks: Run Task` → `run-api`

## 🧪 Pruebas Rápidas

### Usando el script de prueba Python:
```powershell
python test_meta.py
```

### Usando curl:

#### 1. Verificar Estado de la API
```bash
curl http://localhost:8000/health
```

#### 2. Ver Información de la API
```bash
curl http://localhost:8000/
```

#### 3. Verificar Conexiones con Meta
```bash
curl http://localhost:8000/verify
```

## 📝 Ejemplos de Publicación

### Facebook - Solo Texto
```bash
curl -X POST http://localhost:8000/publish \
  -H "Content-Type: application/json" \
  -d '{
    "message": "¡Hola desde mi API de automatización! 🚀",
    "platforms": ["facebook"]
  }'
```

### Facebook - Texto + Imagen
```bash
curl -X POST http://localhost:8000/publish \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Compartiendo una imagen increíble 📸",
    "platforms": ["facebook"],
    "image_url": "https://picsum.photos/800/600"
  }'
```

### Facebook - Texto + Link
```bash
curl -X POST http://localhost:8000/publish \
  -H "Content-Type: application/json" \
  -d '{
    "message": "¡Mira este artículo interesante! 📰",
    "platforms": ["facebook"],
    "link": "https://developers.facebook.com"
  }'
```

### Instagram - Imagen con Caption
```bash
curl -X POST http://localhost:8000/publish \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Post automático en Instagram! 📱✨ #automation #api",
    "platforms": ["instagram"],
    "image_url": "https://picsum.photos/1080/1080"
  }'
```

### Publicar en Facebook e Instagram simultáneamente
```bash
curl -X POST http://localhost:8000/publish \
  -H "Content-Type: application/json" \
  -d '{
    "message": "¡Post en todas las plataformas! 🌐 #socialmedia",
    "platforms": ["facebook", "instagram"],
    "image_url": "https://picsum.photos/1080/1080"
  }'
```

## 📊 Ejemplos de Métricas

### Obtener Todas las Métricas
```bash
curl http://localhost:8000/metrics
```

### Filtrar Métricas con jq (si tienes jq instalado)
```bash
# Solo métricas de Facebook
curl http://localhost:8000/metrics | jq '.results[] | select(.platform == "facebook")'

# Solo métricas de Instagram
curl http://localhost:8000/metrics | jq '.results[] | select(.platform == "instagram")'
```

## 🐍 Ejemplos con Python

### Script Simple de Publicación

```python
import httpx
import asyncio

async def publicar_en_facebook():
    url = "http://localhost:8000/publish"
    data = {
        "message": "Post desde Python! 🐍",
        "platforms": ["facebook"],
        "image_url": "https://picsum.photos/800/600"
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data)
        print(response.json())

asyncio.run(publicar_en_facebook())
```

### Script para Obtener Métricas

```python
import httpx
import asyncio
import json

async def obtener_metricas():
    url = "http://localhost:8000/metrics"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        
        # Mostrar métricas formateadas
        for result in data["results"]:
            platform = result.get("platform")
            print(f"\n📊 {platform.upper()}")
            print(json.dumps(result, indent=2))

asyncio.run(obtener_metricas())
```

### Script Completo con Verificación

```python
import httpx
import asyncio

class SocialMediaAPI:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
    
    async def verificar_conexiones(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/verify")
            return response.json()
    
    async def publicar(self, message, platforms=None, image_url=None, link=None):
        data = {
            "message": message,
            "platforms": platforms or ["facebook"],
        }
        if image_url:
            data["image_url"] = image_url
        if link:
            data["link"] = link
        
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{self.base_url}/publish", json=data)
            return response.json()
    
    async def obtener_metricas(self):
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/metrics")
            return response.json()

async def main():
    api = SocialMediaAPI()
    
    # Verificar conexiones
    print("Verificando conexiones...")
    verificacion = await api.verificar_conexiones()
    print(verificacion)
    
    # Publicar
    print("\nPublicando en Facebook...")
    resultado = await api.publicar(
        message="Post desde Python con mi API! 🚀",
        platforms=["facebook"],
        image_url="https://picsum.photos/800/600"
    )
    print(resultado)
    
    # Obtener métricas
    print("\nObteniendo métricas...")
    metricas = await api.obtener_metricas()
    print(metricas)

if __name__ == "__main__":
    asyncio.run(main())
```

## 🌐 Ejemplos con JavaScript/Node.js

```javascript
// Usando fetch (Node 18+)
async function publicarEnFacebook() {
  const response = await fetch('http://localhost:8000/publish', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      message: 'Post desde JavaScript! 🚀',
      platforms: ['facebook'],
      image_url: 'https://picsum.photos/800/600'
    })
  });
  
  const data = await response.json();
  console.log(data);
}

publicarEnFacebook();
```

## 📱 Ejemplos con PowerShell

```powershell
# Publicar en Facebook
$body = @{
    message = "Post desde PowerShell! 🚀"
    platforms = @("facebook")
    image_url = "https://picsum.photos/800/600"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/publish" `
    -Method POST `
    -ContentType "application/json" `
    -Body $body

# Obtener métricas
Invoke-RestMethod -Uri "http://localhost:8000/metrics" -Method GET
```

## 🔄 Automatización con Schedule

### Publicar diariamente a las 10:00 AM

```python
import schedule
import time
import httpx
import asyncio

async def publicar_diario():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:8000/publish",
            json={
                "message": f"Buenos días! 🌅 Post automático del día",
                "platforms": ["facebook"],
                "image_url": "https://picsum.photos/800/600"
            }
        )
        print(f"Publicado: {response.json()}")

def job():
    asyncio.run(publicar_diario())

# Programar para las 10:00 AM todos los días
schedule.every().day.at("10:00").do(job)

print("Scheduler iniciado. Esperando...")
while True:
    schedule.run_pending()
    time.sleep(60)
```

## 📋 Casos de Uso Reales

### 1. Notificaciones de Eventos
```python
async def notificar_evento(titulo, descripcion, imagen_url):
    data = {
        "message": f"🎉 {titulo}\n\n{descripcion}",
        "platforms": ["facebook", "instagram"],
        "image_url": imagen_url
    }
    # ... publicar
```

### 2. Compartir Artículos de Blog
```python
async def compartir_articulo(titulo, link, imagen):
    data = {
        "message": f"📝 Nuevo artículo: {titulo}",
        "platforms": ["facebook"],
        "link": link,
        "image_url": imagen
    }
    # ... publicar
```

### 3. Promociones y Ofertas
```python
async def publicar_promocion(oferta, descuento, imagen):
    data = {
        "message": f"🎁 {oferta}\n💰 {descuento}% de descuento\n#oferta #descuento",
        "platforms": ["facebook", "instagram"],
        "image_url": imagen
    }
    # ... publicar
```

## 🔍 Documentación Interactiva

Visita http://localhost:8000/docs para ver la documentación Swagger interactiva donde puedes probar todos los endpoints directamente desde el navegador.

## 💡 Tips

1. **Imágenes para Instagram**: Usa imágenes de al menos 1080x1080px
2. **Hashtags**: Instagram permite hasta 30 hashtags
3. **Rate Limits**: Facebook tiene límites de 200 llamadas por hora por usuario
4. **Tokens**: Los tokens de desarrollo expiran rápido, implementa OAuth para producción
5. **Errores**: Siempre revisa el campo `status` en las respuestas
