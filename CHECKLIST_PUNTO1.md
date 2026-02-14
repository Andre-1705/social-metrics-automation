# 📝 Checklist Rápido: Configuración Meta App

Usa este checklist mientras sigues la [GUIA_APLICACION_META.md](GUIA_APLICACION_META.md)

---

## ✅ Paso 1: Aplicación en Meta

- [ ] Acceder a https://developers.facebook.com/apps
- [ ] Crear app o seleccionar existente
- [ ] Tipo: "Empresa" o "Consumidor"

---

## ✅ Paso 2: Información Básica

En **Configuración → Básica**:

- [ ] Nombre para mostrar: `_____________________`
- [ ] Espacio de nombres: `_____________________`
- [ ] URL política privacidad: `https://polit-priv.vercel.app/`
- [ ] URL términos servicio: `https://polit-priv.vercel.app/terminos`
- [ ] Categoría: `_____________________`
- [ ] Email contacto: `MARIAANDREACASTILLOARREGUI@GMAIL.COM`
- [ ] Icono app (opcional): `☐`
- [ ] **Guardar cambios**

---

## ✅ Paso 3: Productos

### Facebook Login
- [ ] Agregar producto "Facebook Login"
- [ ] URI OAuth válidos:
  ```
  https://social-metrics-automation.onrender.com/auth/facebook/callback
  http://localhost:8000/auth/facebook/callback
  ```
- [ ] URL cierre sesión: `https://social-metrics-automation.onrender.com/logout`
- [ ] Dominios:
  ```
  social-metrics-automation.onrender.com
  localhost
  ```
- [ ] **Guardar cambios**

### Instagram Graph API
- [ ] Agregar producto "Instagram Graph API"

---

## ✅ Paso 4: Eliminación de Datos

- [ ] URL eliminación datos: `https://polit-priv.vercel.app/elimindatos`
- [ ] **Guardar cambios**

---

## ✅ Paso 5: Credenciales de App

En **Configuración → Básica**:

- [ ] App ID: `_____________________`
- [ ] App Secret: `_____________________`
- [ ] ✅ Guardados de forma segura

---

## ✅ Paso 6: Webhooks (Opcional)

- [ ] URL callback: `https://social-metrics-automation.onrender.com/webhooks/meta`
- [ ] Token verificación: `_____________________`
- [ ] Campos: `feed`, `page`, `comments`, `reactions`

---

## ✅ Paso 7: Tokens de Acceso

### En Graph API Explorer: https://developers.facebook.com/tools/explorer/

**Permisos a seleccionar:**
- [ ] `pages_show_list`
- [ ] `pages_read_engagement`
- [ ] `pages_manage_posts`
- [ ] `pages_read_user_content`
- [ ] `instagram_basic`
- [ ] `instagram_content_publish`
- [ ] `instagram_manage_insights`

**Query para Page Access Token:**
```
GET /me/accounts
```
- [ ] Page ID: `_____________________`
- [ ] Page Access Token: `_____________________`

**Query para Instagram Business ID:**
```
GET /{TU_PAGE_ID}?fields=instagram_business_account
```
- [ ] Instagram Business ID: `_____________________`

---

## ✅ Paso 8: Actualizar .env

Abrir archivo `.env` y reemplazar:

```env
FACEBOOK_APP_ID=_____________________
FACEBOOK_APP_SECRET=_____________________
FACEBOOK_PAGE_ACCESS_TOKEN=_____________________
FACEBOOK_PAGE_ID=_____________________
INSTAGRAM_ACCESS_TOKEN=_____________________
INSTAGRAM_BUSINESS_ID=_____________________
```

- [ ] ✅ Archivo `.env` actualizado
- [ ] ✅ Valores verificados (sin espacios ni comillas extra)

---

## ✅ Paso 9: Verificación

```powershell
# Activar entorno virtual
.\.venv\Scripts\Activate.ps1

# Probar conexión
python test_meta.py
```

**Resultado esperado:**
```
✅ Conexión con Meta verificada exitosamente
```

- [ ] ✅ Test ejecutado exitosamente
- [ ] ❌ Hay errores (revisar sección troubleshooting en guía)

---

## ✅ Paso 10: Iniciar API

```bash
uvicorn app.main:app --reload
```

- [ ] Servidor iniciado en http://localhost:8000
- [ ] Docs accesibles en http://localhost:8000/docs
- [ ] Endpoint `/verify` funciona
- [ ] Endpoint `/health` funciona

---

## 🎯 Checklist Final Completo

- [ ] Aplicación creada en Meta
- [ ] Información básica completa
- [ ] Política privacidad configurada
- [ ] Términos de servicio configurados
- [ ] URL eliminación datos configurada
- [ ] Facebook Login agregado
- [ ] Instagram Graph API agregado
- [ ] App ID obtenido
- [ ] App Secret obtenido
- [ ] Page Access Token obtenido
- [ ] Page ID obtenido
- [ ] Instagram Business ID obtenido
- [ ] Archivo `.env` actualizado
- [ ] `test_meta.py` ejecutado exitosamente
- [ ] API funcionando correctamente

---

## 🆘 Ayuda Rápida

**Si test_meta.py falla:**
1. Revisa que los tokens estén correctos en `.env`
2. Verifica permisos en Graph API Explorer
3. Usa Access Token Debugger: https://developers.facebook.com/tools/debug/accesstoken/
4. Consulta sección "Resolución de Problemas" en GUIA_APLICACION_META.md

**Si no encuentras tu Instagram Business ID:**
1. Asegúrate de tener cuenta Instagram Business (no personal)
2. Conecta Instagram a tu página de Facebook
3. Usa query: `GET /{page_id}?fields=instagram_business_account`

**Si tokens expiran:**
- Los User Access Tokens expiran en ~1-2 horas
- Los Page Access Tokens pueden durar hasta 60 días
- Ver Punto 2 para renovación automática

---

**Fecha**: _____________________
**Hora inicio**: _____________________
**Hora fin**: _____________________
**Notas**: 

---

✅ **PUNTO 1 COMPLETADO** cuando todos los checks estén marcados
