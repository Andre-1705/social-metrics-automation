"""
Script de prueba para la integración con Meta (Facebook/Instagram).
Ejecuta: python test_meta.py
"""
import asyncio
import sys
from pathlib import Path

# Agregar el directorio raíz al path
sys.path.insert(0, str(Path(__file__).parent))

from app.config import get_settings
from app.publisher import verify_connections, publish_message
from app.metrics import collect_metrics


async def main():
    print("=" * 60)
    print("🧪 PRUEBA DE INTEGRACIÓN CON META")
    print("=" * 60)
    
    settings = get_settings()
    
    # 1. Verificar conexiones
    print("\n📡 1. Verificando conexiones...")
    connections = await verify_connections(settings)
    
    for conn in connections:
        platform = conn.get("platform", "unknown")
        status = conn.get("status", "unknown")
        
        if status == "valid":
            print(f"✅ {platform.upper()}: Conectado correctamente")
            if platform == "facebook":
                print(f"   - Página: {conn.get('page_name')}")
                print(f"   - Seguidores: {conn.get('fan_count')}")
            elif platform == "instagram":
                print(f"   - Usuario: @{conn.get('username')}")
                print(f"   - Seguidores: {conn.get('followers_count')}")
        else:
            print(f"❌ {platform.upper()}: Error")
            print(f"   - Razón: {conn.get('reason', conn.get('detail', 'Unknown'))}")
    
    # 2. Obtener métricas
    print("\n📊 2. Obteniendo métricas...")
    metrics = await collect_metrics(settings)
    
    for metric in metrics:
        platform = metric.get("platform", "unknown")
        status = metric.get("status", "unknown")
        
        if status == "ok":
            print(f"✅ {platform.upper()}: Métricas obtenidas")
            
            if platform == "facebook" and "page_info" in metric:
                page_info = metric["page_info"]
                print(f"   - Fans: {page_info.get('fan_count', 'N/A')}")
                print(f"   - Followers: {page_info.get('followers_count', 'N/A')}")
            
            elif platform == "instagram" and "account_info" in metric:
                account_info = metric["account_info"]
                print(f"   - @{account_info.get('username', 'N/A')}")
                print(f"   - Seguidores: {account_info.get('followers_count', 'N/A')}")
                print(f"   - Posts: {account_info.get('media_count', 'N/A')}")
        else:
            print(f"⚠️  {platform.upper()}: {status}")
    
    # 3. Prueba de publicación (comentada por seguridad)
    print("\n📝 3. Prueba de publicación (DESHABILITADA)")
    print("   Para habilitar, descomenta el código en test_meta.py")
    
    # Descomenta esto para probar publicación real:
    # print("\n📝 Publicando en Facebook...")
    # results = await publish_message(
    #     message="🧪 Post de prueba desde Social Metrics Automation API",
    #     settings=settings,
    #     platforms=["facebook"]
    # )
    # 
    # for result in results:
    #     platform = result.get("platform", "unknown")
    #     status = result.get("status", "unknown")
    #     if status == "posted":
    #         print(f"✅ {platform.upper()}: Publicado con éxito")
    #         print(f"   - Post ID: {result.get('post_id')}")
    #     else:
    #         print(f"❌ {platform.upper()}: Error - {result.get('reason', result.get('detail'))}")
    
    print("\n" + "=" * 60)
    print("✅ Prueba completada")
    print("=" * 60)
    print("\n💡 Próximos pasos:")
    print("   1. Verifica que las conexiones estén OK")
    print("   2. Descomenta el código de publicación para probar")
    print("   3. Revisa CONFIGURACION_META.md para más detalles")
    print("   4. Accede a http://localhost:8000/docs para ver la documentación Swagger")


if __name__ == "__main__":
    asyncio.run(main())
