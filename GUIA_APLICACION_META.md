# 🔐 Guía Completa: Configuración de Aplicación en Meta for Developers

## 📋 Punto 1: Cerrar Detalles de la Aplicación

### 🎯 Información de tu Aplicación Actual

Basado en tu configuración actual en `.env`:
- **Email de contacto**: MARIAANDREACASTILLOARREGUI@GMAIL.COM
- **URL Base Pública**: https://social-metrics-automation.onrender.com
- **Política de Privacidad**: https://polit-priv.vercel.app/
- **Términos de Servicio**: https://polit-priv.vercel.app/terminos
- **Eliminación de Datos**: https://polit-priv.vercel.app/elimindatos
- **Facebook Page ID**: 33574390302148277 (⚠️ verificar si es correcto)
- **Instagram Business ID**: 987654321 (⚠️ placeholder - necesita actualización)

---

## 🚀 Paso a Paso: Configurar tu App en Meta

### 1️⃣ Crear o Acceder a tu Aplicación

1. **Ve a**: https://developers.facebook.com/apps
2. **Inicia sesión** con tu cuenta de Facebook
3. Opciones:
   - **Si ya tienes una app**: Haz clic en ella para configurarla
   - **Si necesitas crear una nueva**:
     - Clic en "Crear aplicación"
     - Selecciona **"Empresa"** o **"Consumidor"** según tu caso
     - Nombre: "Social Metrics Automation" (o el que prefieras)
     - Email de contacto: MARIAANDREACASTILLOARREGUI@GMAIL.COM
     - Clic en "Crear aplicación"

### 2️⃣ Completar Información Básica de la Aplicación

Ve a **Configuración → Básica** en el panel izquierdo:

#### ✅ Campos Obligatorios:

**Nombre para mostrar**:
```
Social Metrics Automation
```

**Espacio de nombres de la aplicación** (App Namespace):
```
socialmetricsautomation
```
(solo letras minúsculas, sin espacios ni guiones)

**URL de política de privacidad**:
```
https://polit-priv.vercel.app/
```

**URL de términos del servicio**:
```
https://polit-priv.vercel.app/terminos
```

**Categoría de la aplicación**:
- Selecciona: **"Empresas y páginas"** o **"Herramientas de marketing"**

**Email de contacto**:
```
MARIAANDREACASTILLOARREGUI@GMAIL.COM
```

**Icono de la aplicación** (opcional pero recomendado):
- Tamaño: 1024x1024 píxeles
- Formato: PNG con fondo transparente
- Contenido: Logo de tu app

**Guarda los cambios** haciendo clic en "Guardar cambios" al final de la página.

---

### 3️⃣ Configurar Productos de la Aplicación

#### A) Facebook Login

1. En el panel izquierdo, busca **"Facebook Login"**
2. Si no está agregado, haz clic en **"Configurar"** o **"Agregar producto"**
3. Ve a **Configuración** de Facebook Login
4. Configura:

**URI de redirección de OAuth válidos**:
```
https://social-metrics-automation.onrender.com/auth/facebook/callback
http://localhost:8000/auth/facebook/callback
```
(segunda línea solo para desarrollo local)

**URL de cierre de sesión**:
```
https://social-metrics-automation.onrender.com/logout
```

**Dominios de aplicaciones**:
```
social-metrics-automation.onrender.com
localhost
```

**Guarda los cambios**

#### B) Instagram Graph API

1. En el panel izquierdo, busca **"Instagram Graph API"**
2. Si no está agregado, haz clic en **"Configurar"** o **"Agregar producto"**
3. No requiere configuración adicional en este paso

---

### 4️⃣ Configurar Eliminación de Datos (Data Deletion)

Meta **requiere** que proporciones una URL de callback para la eliminación de datos de usuarios.

1. Ve a **Configuración → Básica**
2. Desplázate hasta encontrar **"URL de devolución de llamada para eliminación de datos de usuarios"**
3. Ingresa:
```
https://polit-priv.vercel.app/elimindatos
```

**O si prefieres manejarlo en tu API**:
```
https://social-metrics-automation.onrender.com/data-deletion
```

**Nota**: Si usas la URL de tu API, asegúrate de tener implementado el endpoint. Ya existe en `tests/test_data_deletion.py` como referencia.

---

### 5️⃣ Obtener Credenciales de la Aplicación

1. Ve a **Configuración → Básica**
2. Busca y copia:

**ID de la aplicación**:
```
Ejemplo: 123456789012345
```

**Clave secreta de la aplicación**:
```
Haz clic en "Mostrar" y copia el valor
Ejemplo: 1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p
```

**⚠️ Importante**: Guarda estos valores de forma segura. Actualizaremos el `.env` más adelante.

---

### 6️⃣ Configurar Webhooks (Opcional pero Recomendado)

Si deseas recibir notificaciones en tiempo real de Meta:

1. Ve a **Webhooks** en el panel de tu producto
2. Configura:

**URL de devolución de llamada**:
```
https://social-metrics-automation.onrender.com/webhooks/meta
```

**Token de verificación**:
```
mi_token_secreto_123_webhook
```
(elige un token secreto y guárdalo en `.env`)

**Campos a suscribir**:
- `feed` (publicaciones)
- `page` (eventos de página)
- `comments` (comentarios)
- `reactions` (reacciones)

---

### 7️⃣ Modo de la Aplicación

#### Durante Desarrollo:
- Tu app está en **Modo de desarrollo**
- Solo tú (y usuarios de prueba que agregues) pueden usarla
- Los tokens generados son válidos pero con acceso limitado

#### Para Producción:
1. Ve a **Configuración → Básica**
2. En la parte superior, verás un switch **"En desarrollo"**
3. Para pasar a producción:
   - Completa todos los detalles requeridos
   - Acepta los términos de Meta
   - Haz clic en el switch para cambiar a **"Activo"**

**⚠️ Requisitos antes de activar**:
- ✅ Política de privacidad publicada
- ✅ Términos de servicio publicados
- ✅ URL de eliminación de datos configurada
- ✅ Icono de la aplicación cargado
- ✅ Categoría seleccionada

---

### 8️⃣ Obtener Tokens de Acceso

#### Para Facebook Page:

1. Ve a **Graph API Explorer**: https://developers.facebook.com/tools/explorer/
2. Selecciona tu aplicación en el dropdown superior derecho
3. Haz clic en **"Generate Access Token"**
4. Selecciona los permisos necesarios:
   - ✅ `pages_show_list`
   - ✅ `pages_read_engagement`
   - ✅ `pages_manage_posts`
   - ✅ `pages_read_user_content`
   - ✅ `instagram_basic`
   - ✅ `instagram_content_publish`
   - ✅ `instagram_manage_insights`
5. Haz clic en **"Generate Access Token"** y autoriza
6. Copia el token generado (User Access Token)

**Ahora obtén el Page Access Token**:
```
GET /me/accounts
```
- Ejecuta esta consulta en Graph API Explorer
- En la respuesta, busca tu página de Facebook
- Copia el `access_token` y el `id` de la página

#### Para Instagram Business:

Con el User Access Token anterior:
```
GET /{TU_PAGE_ID}?fields=instagram_business_account
```
- Reemplaza `{TU_PAGE_ID}` con el ID de tu página de Facebook
- Copia el `instagram_business_account.id`

---

### 9️⃣ Actualizar Archivo .env

Edita tu archivo `.env` con los valores reales:

```env
# Meta App Credentials
FACEBOOK_APP_ID=TU_APP_ID_AQUI
FACEBOOK_APP_SECRET=TU_APP_SECRET_AQUI

# Facebook Page
FACEBOOK_PAGE_ACCESS_TOKEN=NUEVO_PAGE_ACCESS_TOKEN
FACEBOOK_PAGE_ID=TU_PAGE_ID_REAL

# Instagram Business
INSTAGRAM_ACCESS_TOKEN=MISMO_QUE_FACEBOOK_O_ESPECIFICO
INSTAGRAM_BUSINESS_ID=TU_INSTAGRAM_BUSINESS_ID_REAL

# Webhooks (si lo configuraste)
META_WEBHOOK_VERIFY_TOKEN=mi_token_secreto_123_webhook

# URLs (ya configuradas)
PRIVACY_POLICY_URL=https://polit-priv.vercel.app/
TERMS_OF_SERVICE_URL=https://polit-priv.vercel.app/terminos
ELIMINACION_DE_DATOS_URL=https://polit-priv.vercel.app/elimindatos
PUBLIC_BASE_URL=https://social-metrics-automation.onrender.com
SUPPORT_CONTACT_EMAIL=MARIAANDREACASTILLOARREGUI@GMAIL.COM
```

---

### 🔟 Verificar Configuración

1. **Activar el entorno virtual**:
```powershell
.\.venv\Scripts\Activate.ps1
```

2. **Ejecutar script de prueba**:
```bash
python test_meta.py
```

3. **Deberías ver**:
```
✅ Conexión con Meta verificada exitosamente
✅ Facebook Page ID: [tu_id]
✅ Instagram Business ID: [tu_id]
```

4. **Si hay errores**, revisa:
- ✅ Tokens copiados correctamente en `.env`
- ✅ Permisos otorgados en Graph API Explorer
- ✅ App está en modo desarrollo o activo
- ✅ Tu cuenta tiene acceso a la página/Instagram

---

## 📊 Checklist Final

Antes de considerar completado el Punto 1:

- [ ] Aplicación creada en Meta for Developers
- [ ] Nombre, icono y categoría configurados
- [ ] Política de privacidad y términos agregados
- [ ] URL de eliminación de datos configurada
- [ ] Facebook Login agregado y configurado
- [ ] Instagram Graph API agregado
- [ ] App ID y App Secret obtenidos
- [ ] Page Access Token generado y probado
- [ ] Instagram Business Account ID obtenido
- [ ] Archivo `.env` actualizado con valores reales
- [ ] Script `test_meta.py` ejecutado exitosamente
- [ ] API iniciada y endpoints funcionando

---

## 🆘 Resolución de Problemas Comunes

### Error: "Invalid OAuth access token"
- ✅ Regenera el token en Graph API Explorer
- ✅ Verifica que el token no haya expirado
- ✅ Asegúrate de usar el Page Access Token, no el User Access Token

### Error: "Insufficient permissions"
- ✅ Revisa los permisos otorgados al generar el token
- ✅ Ve a **Roles → Roles de prueba** y agrega tu usuario
- ✅ En modo desarrollo, solo usuarios agregados pueden usar la app

### Error: "Invalid Instagram Business ID"
- ✅ Verifica que tu página de Facebook esté conectada a una cuenta de Instagram Business
- ✅ Instagram personal no funciona, debe ser Business o Creator
- ✅ Convierte tu cuenta en: Configuración → Cuenta → Cambiar a cuenta profesional

### No encuentro mi Instagram Business ID
1. Ve a tu página de Facebook
2. Configuración de la página → Instagram
3. Conecta tu cuenta de Instagram Business
4. Usa Graph API Explorer: `GET /{page_id}?fields=instagram_business_account`

---

## 🔗 Enlaces Útiles

- **Meta for Developers**: https://developers.facebook.com/
- **Graph API Explorer**: https://developers.facebook.com/tools/explorer/
- **Access Token Debugger**: https://developers.facebook.com/tools/debug/accesstoken/
- **Permisos de Facebook**: https://developers.facebook.com/docs/permissions/reference
- **Instagram Graph API**: https://developers.facebook.com/docs/instagram-api
- **Documentación de tu API**: http://localhost:8000/docs

---

## ✅ Próximos Pasos

Una vez completado el Punto 1:
- **Punto 2**: Implementar renovación automática de tokens
- **Punto 3**: Configurar webhooks para eventos en tiempo real
- **Punto 4**: Pasar la app a modo producción
- **Punto 5**: Agregar integración con TikTok y WhatsApp

---

**Última actualización**: Enero 2026
**Estado**: 📝 Guía lista para usar
