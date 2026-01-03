# Guía de Configuración con Meta (Facebook/Instagram)

Esta guía te ayudará a configurar tu aplicación con Meta para publicar y obtener métricas de Facebook e Instagram.

## 📋 Requisitos Previos

1. ✅ Cuenta de Facebook personal
2. ✅ Página de Facebook creada
3. ✅ Cuenta de Instagram Business vinculada a tu página de Facebook
4. ✅ Políticas de privacidad publicadas: https://polit-priv.vercel.app/

## 🚀 Paso 1: Crear una Aplicación en Meta

1. Ve a [Meta for Developers](https://developers.facebook.com/)
2. Haz clic en **"Mis Aplicaciones"** → **"Crear Aplicación"**
3. Selecciona el tipo: **"Empresa"** (Business)
4. Completa la información:
   - **Nombre de la aplicación**: Social Metrics Automation
   - **Correo de contacto**: tu correo
   - **Cuenta de empresa**: crea una nueva o selecciona existente

## 🔑 Paso 2: Configurar Productos de Meta

### Agregar Productos en tu Aplicación

1. Entra a [Meta for Developers](https://developers.facebook.com/)
2. Ve a **"Mis Aplicaciones"** y selecciona tu app
3. En el panel izquierdo, busca la sección **"Agregar productos"** o **"Products"**

### Para Facebook Pages:

4. En la lista de productos disponibles, busca **"Facebook Login"**
   - Haz clic en **"Configurar"** o **"Set up"**
   - Se agregará automáticamente al menú lateral

5. Busca **"Facebook Pages"** en la lista de productos
   - Haz clic en **"Configurar"** o **"Set up"**  
   - Acepta los términos si aparece un diálogo
   - Verás que se agrega al menú lateral

6. Configura las URLs básicas:
   - En el menú lateral, ve a **Configuración → Básica** (Settings → Basic)
   - Llena estos campos:
     - **URL de política de privacidad**: `https://polit-priv.vercel.app/`
     - **URL de términos de servicio**: `https://polit-priv.vercel.app/` (o tu URL específica)
     - **Dominio de la aplicación**: (opcional, para producción)
     - **URL de Eliminación de Datos**: `https://tu-dominio.com/data-deletion` (para producción) o `http://localhost:8000/data-deletion` (para desarrollo)

### Para Instagram:

7. En **"Agregar productos"**, busca **"Instagram"** o **"Instagram Graph API"**
   - Haz clic en **"Configurar"** o **"Set up"**
   - Se agregará al menú lateral como "Instagram Graph API" o "Instagram Basic Display"

8. Si ves **"Instagram Business"** como opción separada, también agrégalo
   - Haz clic en **"Configurar"**
   - Nota: A veces Instagram Business viene incluido con Instagram Graph API

### Verificar que los productos estén activos:

9. En el panel lateral izquierdo, deberías ver ahora:
   - ✅ **Facebook Login** (con icono de candado)
   - ✅ **Facebook Pages** (con icono de página)
   - ✅ **Instagram** o **Instagram Graph API** (con icono de cámara)

10. Cada producto puede tener su propia sección de **"Configuración"** en el menú lateral

## 🎯 Paso 3: Configurar Permisos

Tu aplicación necesita estos permisos:

### Facebook:
- `pages_show_list` - Ver lista de páginas
- `pages_read_engagement` - Leer métricas de engagement
- `pages_manage_posts` - Publicar en páginas
- `pages_read_user_content` - Leer contenido de páginas

### Instagram:
- `instagram_basic` - Acceso básico
- `instagram_content_publish` - Publicar contenido
- `instagram_manage_insights` - Ver insights/métricas

## 🔐 Paso 4: Obtener Access Token de Página

### Opción A: Graph API Explorer (Desarrollo)

1. Ve a [Graph API Explorer](https://developers.facebook.com/tools/explorer/)
2. Selecciona tu aplicación en el dropdown
3. Haz clic en **"Generar Token de Acceso"**
4. Selecciona los permisos que configuraste
5. Aprueba el acceso
6. En el campo **"Aplicación"**, selecciona tu página
7. Copia el **User Access Token**
8. Ahora obtén el **Page Access Token**:
   ```
   GET /me/accounts
   ```
9. Copia el `access_token` de tu página y el `id`

### Opción B: Con código (Producción)

Usa el flujo de OAuth 2.0 para obtener tokens de larga duración.

## 📝 Paso 5: Configurar Variables de Entorno

Edita tu archivo `.env`:

```env
# Facebook
FACEBOOK_PAGE_ACCESS_TOKEN=tu_page_access_token_aqui
FACEBOOK_PAGE_ID=327186024892712

# Instagram
INSTAGRAM_ACCESS_TOKEN=tu_page_access_token_aqui  # Mismo token de página
INSTAGRAM_BUSINESS_ID=tu_instagram_business_id

# Políticas
PRIVACY_POLICY_URL=https://polit-priv.vercel.app/
TERMS_OF_SERVICE_URL=https://polit-priv.vercel.app/
 
 # Eliminación de datos
 SUPPORT_CONTACT_EMAIL=tu@correo.com
 PUBLIC_BASE_URL=http://localhost:8000
```

Si tienes una URL distinta para Términos de Servicio (por ejemplo, `https://polit-priv.vercel.app/terminos`), configura `TERMS_OF_SERVICE_URL` con ese valor. Si no la defines, la API usará automáticamente la misma URL que `PRIVACY_POLICY_URL`.

### Cómo obtener Instagram Business ID:

```bash
curl -X GET "https://graph.facebook.com/v21.0/me/accounts?access_token=TU_USER_TOKEN"
```

Luego con el ID de tu página:

```bash
curl -X GET "https://graph.facebook.com/v21.0/PAGE_ID?fields=instagram_business_account&access_token=PAGE_TOKEN"
```

## ✅ Paso 6: Verificar Configuración

1. Inicia tu servidor:
   ```bash
   .\.venv\Scripts\Activate.ps1
   uvicorn app.main:app --reload
   ```

2. Verifica la conexión:
   ```bash
   curl http://localhost:8000/verify
   ```

Deberías ver información de tu página de Facebook e Instagram.

3. Verificar endpoint de eliminación de datos:
```bash
curl "http://localhost:8000/data-deletion?platform=facebook&user_id=123"
```
Debería devolver un `confirmation_code` y una `url` de estado.

## 🧪 Paso 7: Probar Publicación

### Publicar solo en Facebook:
```bash
curl -X POST "http://localhost:8000/publish" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "¡Hola desde mi API! 🚀",
    "platforms": ["facebook"]
  }'
```

### Publicar en Facebook con imagen:
```bash
curl -X POST "http://localhost:8000/publish" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Post con imagen 📸",
    "platforms": ["facebook"],
    "image_url": "https://ejemplo.com/imagen.jpg"
  }'
```

### Publicar en Instagram (requiere imagen):
```bash
curl -X POST "http://localhost:8000/publish" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Post en Instagram! #api #automation",
    "platforms": ["instagram"],
    "image_url": "https://ejemplo.com/imagen.jpg"
  }'
```

## 📊 Paso 8: Obtener Métricas

```bash
curl http://localhost:8000/metrics
```

## ⚠️ Notas Importantes

1. **Tokens de desarrollo**: Los tokens del Graph API Explorer expiran en pocas horas
2. **Tokens de producción**: Implementa OAuth 2.0 para tokens de larga duración (60 días)
3. **Instagram requiere imágenes**: No puedes publicar solo texto en Instagram
4. **Revisión de aplicación**: Para usar en producción, Meta debe revisar tu aplicación
5. **Límites de API**: Meta tiene límites de llamadas, revisa la [documentación oficial](https://developers.facebook.com/docs/graph-api/overview/rate-limiting)

## 🔄 Renovar Tokens de Larga Duración

Para obtener un token de 60 días:

```bash
curl -X GET "https://graph.facebook.com/v21.0/oauth/access_token?grant_type=fb_exchange_token&client_id=TU_APP_ID&client_secret=TU_APP_SECRET&fb_exchange_token=SHORT_LIVED_TOKEN"
```

## 📚 Recursos Adicionales

- [Meta for Developers](https://developers.facebook.com/)
- [Graph API Explorer](https://developers.facebook.com/tools/explorer/)
- [Documentación Facebook Pages API](https://developers.facebook.com/docs/pages)
- [Documentación Instagram Graph API](https://developers.facebook.com/docs/instagram-api)
- [Guía de OAuth](https://developers.facebook.com/docs/facebook-login/guides/advanced/manual-flow)

## 🆘 Solución de Problemas

### Error: "Invalid OAuth access token"
- Verifica que el token no haya expirado
- Asegúrate de usar el Page Access Token, no el User Access Token

### Error: "Permissions error"
- Verifica que tu aplicación tenga los permisos necesarios
- Reautoriza la aplicación con los nuevos permisos

### Error: "Instagram requires image_url"
- Instagram no permite posts de solo texto
- Siempre incluye `image_url` al publicar en Instagram

### No se obtienen métricas
- Verifica que tu cuenta sea Instagram Business, no Creator
- Asegúrate de tener datos en el período solicitado
