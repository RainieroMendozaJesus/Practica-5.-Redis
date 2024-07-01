import redis

# Configuración de Redis
redis_host = 'example'
redis_port = 00000
redis_password = 'example'

# Conexión a Redis
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

# Suscriptor
def subscriber():
    try:
        redis_client.ping()
        print("Conexión a Redis exitosa.")
    except redis.ConnectionError:
        print("Error al conectar con Redis.")
        return

    pubsub = redis_client.pubsub()
    pubsub.subscribe('canal_prueba')
    
    print("Esperando mensajes...")
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Recibido: {message['data']}")

if __name__ == "__main__":
    subscriber()
