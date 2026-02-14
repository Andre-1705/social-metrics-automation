# Social Metrics Automation

Herramienta para publicar y medir rendimiento en Facebook, Instagram, TikTok y WhatsApp (Cloud API). Incluye API REST con FastAPI y un CLI con Typer para orquestar publicaciones y obtener métricas.

## 📚 Documentación

### 🔥 Para Empezar (LEE ESTO PRIMERO)
- **[GUIA_APLICACION_META.md](GUIA_APLICACION_META.md)**: Guía completa paso a paso para configurar tu aplicación en Meta for Developers
- **[CHECKLIST_PUNTO1.md](CHECKLIST_PUNTO1.md)**: Checklist interactivo para ir marcando tu progreso
- **[COMANDOS_UTILES.md](COMANDOS_UTILES.md)**: Comandos copy-paste para agilizar tu trabajo

### 📖 Documentación Técnica
- **[CONFIGURACION_META.md](CONFIGURACION_META.md)**: Instrucciones detalladas de integración con Facebook/Instagram
- **[EJEMPLOS.md](EJEMPLOS.md)**: Casos de uso y ejemplos prácticos de la API
- **[ESTADO_INTEGRACION.md](ESTADO_INTEGRACION.md)**: Estado actual del proyecto y roadmap

### ✅ Informes de Progreso
- **[PUNTO1_COMPLETADO.md](PUNTO1_COMPLETADO.md)**: Resumen del trabajo completado en el Punto 1


## 🚀 Pila Tecnológica
- Python 3.11+
- FastAPI + Uvicorn
- httpx (async) para llamadas a APIs
- APScheduler para tareas periódicas
- Typer para CLI

## ⚡ Configuración Rápida

### 1. Preparar entorno
```bash
# Crear y activar entorno virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows PowerShell
# source .venv/bin/activate    # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Configurar credenciales

**IMPORTANTE**: Antes de configurar el `.env`, lee **[GUIA_APLICACION_META.md](GUIA_APLICACION_META.md)** para obtener tus credenciales correctamente.

```bash
# Copiar plantilla
cp .env.example .env

# Editar con tus valores reales
code .env
```

### 3. Verificar configuración
```bash
# Probar conexión con Meta
python test_meta.py
```

### 4. Iniciar API
```bash
# Opción 1: Con uvicorn directamente
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Opción 2: Con tarea de VS Code
# Ctrl+Shift+P → Tasks: Run Task → run-api
```

### 5. Probar API
```bash
# Documentación interactiva
http://localhost:8000/docs

# O con curl
curl http://localhost:8000/health
```

## 🔐 Políticas de Privacidad

La aplicación incluye las políticas de privacidad requeridas para las integraciones con redes sociales.

- **Política de Privacidad**: https://polit-priv.vercel.app/
- **Términos de Servicio**: https://polit-priv.vercel.app/terminos
- **Eliminación de Datos**: https://polit-priv.vercel.app/elimindatos

Ver [TERMS_OF_SERVICE.md](TERMS_OF_SERVICE.md) para más detalles.

## 🗑️ Eliminación de Datos de Usuarios (Meta)
La API expone endpoints para solicitudes de eliminación de datos exigidos por Meta:

- `GET /data-deletion` – Recibe solicitudes (compatible con `signed_request` y `user_id`)
- `POST /data-deletion` – Alternativa POST
- `GET /data-deletion/status/{code}` – Consulta de estado con `confirmation_code`

Configura en `.env` (opcional):

```env
SUPPORT_CONTACT_EMAIL=MARIAANDREACASTILLOARREGUI@GMAIL.COM
PUBLIC_BASE_URL=http://localhost:8000            # cambia a tu dominio público (p. ej. https://tu-app.onrender.com)
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
