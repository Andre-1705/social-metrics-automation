# ✅ Checklist: Qué te falta para configurar Meta

## 📋 PARTE 1: Configurar tu archivo .env (Local)

### ✅ Paso 1: Abrir tu archivo `.env`
```powershell
code .env
```

### ✅ Paso 2: Agregar estas líneas (si no están)
```env
# Email de contacto (pon tu correo)
SUPPORT_CONTACT_EMAIL=tu@correo.com

# URL pública de tu API (lee abajo qué poner aquí)
PUBLIC_BASE_URL=http://localhost:8000
```

**¿Qué poner en `PUBLIC_BASE_URL`?**
- **Si estás probando en LOCAL**: deja `http://localhost:8000`
- **Si ya tienes un servidor/dominio**: pon `https://tu-dominio.com` (SIN barra al final)
- **Si quieres probar con Meta ahora**: necesitas crear una URL pública temporal con ngrok (ver Paso 3 opcional)

---

## 📋 PARTE 2: Configurar en Meta (Dashboard)

### ✅ Paso 3: Ir a Meta for Developers
1. Ve a: https://developers.facebook.com/apps
2. Selecciona tu aplicación (o créala si no tienes)
3. Ve al menú lateral → **Configuración** → **Básica**

### ✅ Paso 4: Rellenar campos obligatorios

En la página de "Configuración → Básica", completa estos campos:

**Campo 1: Política de privacidad**
```
https://polit-priv.vercel.app/
```

**Campo 2: Términos de servicio**
```
https://polit-priv.vercel.app/
```

**Campo 3: URL de eliminación de datos** ⚠️ **IMPORTANTE**
```
https://tu-dominio.com/data-deletion
```

**¿Qué URL poner exactamente?**
- **Si tienes dominio propio**: `https://tu-dominio.com/data-deletion`
- **Si estás en Vercel/Netlify/Railway**: `https://tu-app.vercel.app/data-deletion`
- **Si aún no tienes servidor público**: 
  - Por ahora deja el campo vacío
  - Usa ngrok (ver Paso 5 opcional)
  - O despliega primero tu API en un servidor

**Campo 4: Correo de contacto**
```
tu@correo.com
```

**Campo 5: Categoría de la aplicación**
- Selecciona: **"Redes sociales"** o **"Empresa"**

### ✅ Paso 5: Agregar productos

En el menú lateral, ve a **Agregar Productos**:
1. Busca **"Facebook Login"** → Configúralo
2. Busca **"Instagram Graph API"** → Configúralo

---

## 📋 PARTE 3 (OPCIONAL): Crear URL pública temporal con ngrok

**Solo si quieres probar AHORA y no tienes dominio:**

### Paso 1: Descargar ngrok
```
https://ngrok.com/download
```

### Paso 2: Iniciar tu API local
```powershell
.\.venv\Scripts\Activate.ps1
uvicorn app.main:app --reload
```

### Paso 3: En otra terminal, ejecutar ngrok
```powershell
ngrok http 8000
```

### Paso 4: Copiar la URL que te da ngrok
Verás algo como:
```
Forwarding  https://abc123.ngrok.io -> http://localhost:8000
```

### Paso 5: Actualizar .env
```env
PUBLIC_BASE_URL=https://abc123.ngrok.io
```

### Paso 6: En Meta, poner en "URL de eliminación de datos":
```
https://abc123.ngrok.io/data-deletion
```

⚠️ **IMPORTANTE**: La URL de ngrok cambia cada vez que lo reinicias (versión gratuita)

---

## 📋 PARTE 4: Verificar que todo funciona

### ✅ Paso 1: Probar endpoint localmente
```powershell
curl "http://localhost:8000/data-deletion?platform=facebook&user_id=123"
```

Deberías ver algo como:
```json
{
  "status": "received",
  "confirmation_code": "abc123...",
  "url": "http://localhost:8000/data-deletion/status/abc123..."
}
```

### ✅ Paso 2: Probar con tu URL pública (si tienes)
```powershell
curl "https://tu-dominio.com/data-deletion?platform=facebook&user_id=123"
```

### ✅ Paso 3: Ver documentación interactiva
Abre en tu navegador:
```
http://localhost:8000/docs
```

---

## 📝 RESUMEN: ¿Qué te falta?

### En tu computadora:
- [ ] Editar `.env` y poner tu `SUPPORT_CONTACT_EMAIL`
- [ ] Decidir si usas dominio propio, ngrok, o esperas a desplegar

### En Meta Dashboard:
- [ ] Ir a Configuración → Básica
- [ ] Poner URL de políticas: `https://polit-priv.vercel.app/`
- [ ] Poner URL de términos: `https://polit-priv.vercel.app/`
- [ ] Poner URL de eliminación: `https://tu-dominio.com/data-deletion` (cuando la tengas)
- [ ] Poner tu correo de contacto
- [ ] Seleccionar categoría: "Redes sociales"
- [ ] Agregar productos: Facebook Login + Instagram Graph API

### Tokens:
- [ ] Obtener Page Access Token (ver CONFIGURACION_META.md)
- [ ] Obtener Page ID
- [ ] Obtener Instagram Business ID
- [ ] Actualizar `.env` con los tokens nuevos

---

## 🆘 ¿Cuál es tu situación?

**Opción A: Solo quiero probar en local**
→ Deja `PUBLIC_BASE_URL=http://localhost:8000`
→ En Meta, por ahora no pongas URL de eliminación (o usa ngrok)

**Opción B: Quiero configurar Meta completamente ahora**
→ Usa ngrok para crear URL temporal
→ Sigue PARTE 3

**Opción C: Voy a desplegar a un servidor primero**
→ Despliega tu API a Vercel/Railway/etc
→ Actualiza `PUBLIC_BASE_URL` con tu dominio
→ En Meta pon: `https://tu-dominio.com/data-deletion`

---

## 📞 Próximos pasos

1. Dime cuál es tu situación (A, B o C)
2. Te ayudo a completar lo que falta
3. Probamos que todo funcione

