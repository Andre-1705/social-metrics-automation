# 🚀 Comandos Útiles - Social Metrics Automation

Comandos copy-paste para agilizar tu configuración.

---

## 📦 Setup Inicial

### Crear entorno virtual (si no existe)
```powershell
python -m venv .venv
```

### Activar entorno virtual
```powershell
# PowerShell (Windows)
.\.venv\Scripts\Activate.ps1

# Bash (Linux/Mac/Git Bash)
source .venv/bin/activate
```

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Crear .env desde plantilla
```powershell
Copy-Item .env.example .env
```

### Abrir .env en VS Code
```bash
code .env
```

---

## 🔍 Verificación

### Probar conexión con Meta
```bash
python test_meta.py
```

### Verificar formato de .env
```powershell
Get-Content .env | Select-String "FACEBOOK|INSTAGRAM"
```

---

## 🌐 Iniciar Servidor

### Con uvicorn (desarrollo)
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Con uvicorn en puerto específico
```bash
uvicorn app.main:app --reload --port 8080
```

### Abrir documentación en navegador
```powershell
Start-Process "http://localhost:8000/docs"
```

---

## 🧪 Pruebas con curl

### Health check
```bash
curl http://localhost:8000/health
```

### Información de la API
```bash
curl http://localhost:8000/
```

### Verificar credenciales
```bash
curl http://localhost:8000/verify
```

### Publicar en Facebook (solo texto)
```bash
curl -X POST http://localhost:8000/publish `
  -H "Content-Type: application/json" `
  -d '{
    "message": "Hola desde mi API 🚀",
    "platforms": ["facebook"]
  }'
```

### Publicar con imagen (Facebook + Instagram)
```bash
curl -X POST http://localhost:8000/publish `
  -H "Content-Type: application/json" `
  -d '{
    "message": "Post con imagen 📸 #automation",
    "platforms": ["facebook", "instagram"],
    "image_url": "https://picsum.photos/800/600"
  }'
```

### Publicar con link (solo Facebook)
```bash
curl -X POST http://localhost:8000/publish `
  -H "Content-Type: application/json" `
  -d '{
    "message": "Mira este enlace interesante 🔗",
    "platforms": ["facebook"],
    "link": "https://github.com"
  }'
```

### Obtener métricas
```bash
curl http://localhost:8000/metrics
```

---

## 🔧 Graph API Explorer

### URLs útiles
```
# Graph API Explorer
https://developers.facebook.com/tools/explorer/

# Access Token Debugger
https://developers.facebook.com/tools/debug/accesstoken/

# Meta for Developers Console
https://developers.facebook.com/apps
```

### Queries útiles en Graph API Explorer

#### Obtener información de tu cuenta
```graphql
GET /me?fields=id,name,email
```

#### Listar páginas que administras
```graphql
GET /me/accounts
```

#### Obtener información de una página
```graphql
GET /{PAGE_ID}?fields=id,name,fan_count,access_token
```

#### Obtener Instagram Business Account de una página
```graphql
GET /{PAGE_ID}?fields=instagram_business_account
```

#### Obtener métricas de Facebook Page
```graphql
GET /{PAGE_ID}/insights?metric=page_fans,page_engaged_users
```

#### Obtener información de Instagram Business Account
```graphql
GET /{INSTAGRAM_BUSINESS_ID}?fields=id,username,followers_count,media_count
```

#### Listar posts recientes de Facebook
```graphql
GET /{PAGE_ID}/posts?fields=id,message,created_time,likes.summary(true),comments.summary(true)
```

#### Listar medios de Instagram
```graphql
GET /{INSTAGRAM_BUSINESS_ID}/media?fields=id,caption,media_type,media_url,timestamp,like_count,comments_count
```

---

## 🐍 CLI Commands

### Ayuda del CLI
```bash
python -m app.cli --help
```

### Publicar desde CLI
```bash
python -m app.cli publish "Mi mensaje" --platforms facebook instagram
```

### Obtener métricas desde CLI
```bash
python -m app.cli metrics
```

---

## 📊 Desarrollo

### Ejecutar tests
```bash
pytest
```

### Ejecutar tests con verbose
```bash
pytest -v
```

### Ejecutar test específico
```bash
pytest tests/test_health.py
```

### Ver cobertura
```bash
pytest --cov=app tests/
```

### Formatear código con black
```bash
black app/ tests/
```

### Linter con flake8
```bash
flake8 app/ tests/
```

---

## 🔐 Variables de Entorno

### Ver variables relacionadas con Meta
```powershell
Get-Content .env | Select-String "FACEBOOK|INSTAGRAM|META"
```

### Verificar que .env está cargado
```python
python -c "from app.config import get_settings; s=get_settings(); print(f'App ID: {s.facebook_app_id}'); print(f'Page ID: {s.facebook_page_id}')"
```

### Limpiar variable específica
```powershell
# Cuidado: esto remueve la línea del archivo
(Get-Content .env) | Where-Object { $_ -notmatch "FACEBOOK_PAGE_ID" } | Set-Content .env
```

---

## 🧹 Limpieza

### Limpiar cache de Python
```powershell
Get-ChildItem -Recurse -Filter "__pycache__" | Remove-Item -Recurse -Force
Get-ChildItem -Recurse -Filter "*.pyc" | Remove-Item -Force
```

### Desactivar entorno virtual
```bash
deactivate
```

### Eliminar entorno virtual
```powershell
Remove-Item -Recurse -Force .venv
```

---

## 📝 Git

### Ver estado
```bash
git status
```

### Agregar cambios (excluyendo .env)
```bash
git add .
git reset .env  # asegurar que .env no se suba
```

### Commit
```bash
git commit -m "Configuración completa de Meta integration"
```

### Ver .gitignore
```powershell
Get-Content .gitignore
```

---

## 🔄 Actualización

### Actualizar dependencias
```bash
pip install --upgrade -r requirements.txt
```

### Congelar dependencias actuales
```bash
pip freeze > requirements.txt
```

### Ver versión de Python
```bash
python --version
```

---

## 📱 Meta App - PowerShell Helpers

### Abrir Meta for Developers
```powershell
Start-Process "https://developers.facebook.com/apps"
```

### Abrir Graph API Explorer
```powershell
Start-Process "https://developers.facebook.com/tools/explorer/"
```

### Abrir Token Debugger
```powershell
Start-Process "https://developers.facebook.com/tools/debug/accesstoken/"
```

### Abrir tu política de privacidad
```powershell
Start-Process "https://polit-priv.vercel.app/"
```

---

## 💻 VS Code

### Abrir en VS Code
```bash
code .
```

### Abrir archivo específico
```bash
code .env
code GUIA_APLICACION_META.md
```

### Ejecutar tarea
```powershell
# Desde terminal integrada
Ctrl+Shift+P → "Tasks: Run Task" → "run-api"
```

---

## 🎯 Quick Start Completo

```powershell
# 1. Setup
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 2. Configurar
Copy-Item .env.example .env
code .env  # editar con tus valores

# 3. Verificar
python test_meta.py

# 4. Iniciar
uvicorn app.main:app --reload

# 5. Probar (en otra terminal)
curl http://localhost:8000/docs
Start-Process "http://localhost:8000/docs"
```

---

## 🆘 Troubleshooting

### Ver logs en tiempo real
```bash
# Ya incluido en uvicorn --reload
# Los logs aparecen automáticamente en la terminal
```

### Verificar puerto en uso
```powershell
Get-NetTCPConnection -LocalPort 8000
```

### Matar proceso en puerto 8000
```powershell
$process = Get-NetTCPConnection -LocalPort 8000 -ErrorAction SilentlyContinue
if ($process) {
    Stop-Process -Id $process.OwningProcess -Force
}
```

### Reinstalar dependencias desde cero
```powershell
Remove-Item -Recurse -Force .venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

**Última actualización**: Enero 2026
**Tip**: Marca esta página como favorito en tu navegador para acceso rápido
