# Social Metrics Automation

Herramienta base para publicar y medir rendimiento en Facebook, Instagram, TikTok y WhatsApp (Cloud API). Incluye API REST con FastAPI y un CLI con Typer para orquestar publicaciones y obtener métricas.

## Pila
- Python 3.11+
- FastAPI + Uvicorn
- httpx (async) para llamadas a APIs
- APScheduler para tareas periódicas
- Typer para CLI

## Configuración rápida
1. Crea y activa un entorno virtual (ejemplo con `python -m venv .venv`).
2. Instala dependencias: `pip install -r requirements.txt`.
3. Copia `.env.example` a `.env` y rellena los tokens de cada plataforma.
4. Ejecuta la API: `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`.
5. Ejecuta el CLI: `python -m app.cli --help`.

## Políticas de Privacidad
La aplicación incluye las políticas de privacidad requeridas para las integraciones con redes sociales.
URL: https://polit-priv.vercel.app/

## Términos de Servicio
Puedes configurar una URL distinta para los términos de servicio mediante la variable `TERMS_OF_SERVICE_URL`. Si no la defines, se utilizará la misma URL que `PRIVACY_POLICY_URL`.

## Eliminación de Datos de Usuarios (Meta)
La API expone endpoints para solicitudes de eliminación de datos exigidos por Meta:

- `GET /data-deletion` – Recibe solicitudes (compatible con `signed_request` y `user_id`)
- `POST /data-deletion` – Alternativa POST
- `GET /data-deletion/status/{code}` – Consulta de estado con `confirmation_code`

Configura en `.env` (opcional):

```env
SUPPORT_CONTACT_EMAIL=tu@correo.com
PUBLIC_BASE_URL=http://localhost:8000
```

En la configuración de tu App en Meta (Configuración → Básica), agrega la **URL de eliminación de datos** apuntando a tu endpoint público, por ejemplo: `https://tu-dominio.com/data-deletion`.

## Endpoints básicos
- `GET /health`: estado de la aplicación.
- `POST /publish`: publica un mensaje en las plataformas configuradas.
- `GET /metrics`: devuelve métricas agregadas simples.

## Integración con Meta

✅ **Facebook**: Publicación con soporte para texto, imágenes y links + métricas detalladas
✅ **Instagram**: Publicación de imágenes con caption + métricas de cuenta y medios

Ver [CONFIGURACION_META.md](CONFIGURACION_META.md) para instrucciones detalladas de configuración.

## Endpoints de la API

### `GET /` - Información de la API
Retorna información básica de la API y enlaces útiles.

### `GET /health` - Estado
Verifica que la API esté funcionando.

### `GET /verify` - Verificar Conexiones
Verifica las credenciales de Facebook e Instagram.

```bash
curl http://localhost:8000/verify
```

### `POST /publish` - Publicar Contenido
Publica en las plataformas seleccionadas.

**Parámetros:**
- `message` (requerido): Texto del mensaje
- `platforms` (opcional): Array de plataformas ["facebook", "instagram", "tiktok", "whatsapp"]
- `image_url` (opcional): URL de imagen (requerido para Instagram)
- `link` (opcional): URL para compartir (solo Facebook)

**Ejemplos:**
```bash
# Solo texto en Facebook
curl -X POST http://localhost:8000/publish \
  -H "Content-Type: application/json" \
  -d '{"message": "Hola!", "platforms": ["facebook"]}'

# Con imagen en Facebook e Instagram
curl -X POST http://localhost:8000/publish \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Post con imagen 📸",
    "platforms": ["facebook", "instagram"],
    "image_url": "https://picsum.photos/800/600"
  }'
```

### `GET /metrics` - Obtener Métricas
Retorna métricas de todas las plataformas configuradas.

```bash
curl http://localhost:8000/metrics
```

## Estado del Proyecto

✅ **Implementado:**
- FastAPI con endpoints REST
- Cliente de Facebook con publicación y métricas
- Cliente de Instagram con publicación y métricas
- Verificación de credenciales
- Soporte para imágenes y links
- Métricas detalladas con insights

🚧 **Pendiente:**
- TikTok API (stub creado)
- WhatsApp Cloud API (stub creado)
- Sistema de webhooks para eventos
- Dashboard de métricas
- Autenticación OAuth completa
- Programación de publicaciones
