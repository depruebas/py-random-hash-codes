import secrets
import sys
import uuid
import base64


def generateUUIDCodeLongVersion(n):
    # 1. Genera un UUID versión 4 (completamente aleatorio)
    u = uuid.uuid4()
    print("UUID generado:", u)

    # 2. Obtiene la representación binaria (bytes) del UUID
    uuid_bytes = u.bytes
    print("Bytes del UUID:", uuid_bytes)

    # 3. Codifica esos bytes en base64 segura para URLs
    b64_bytes = base64.urlsafe_b64encode(uuid_bytes)
    print("Base64 crudo:", b64_bytes)

    # 4. Convierte los bytes codificados a string UTF-8
    b64_str = b64_bytes.decode('utf-8')
    print("Base64 en string:", b64_str)

    # 5. Quita los signos de igual '=' del final (relleno del base64)
    b64_str_sin_padding = b64_str.rstrip('=')
    print("Base64 sin '=':", b64_str_sin_padding)

    # 6. Devuelve los primeros 'k' caracteres del string
    codigo_final = b64_str_sin_padding[:n]
    print("Código final:", codigo_final)

    return codigo_final

def generateRandomCodeLongVersion(n):
    # 1. Definimos el conjunto de caracteres permitidos (alfanuméricos sin ambiguos)
    alpha_num = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz123456789'
    
    # 2. Creamos una lista vacía para almacenar los caracteres aleatorios
    caracteres = []
    
    # 3. Bucle que se repite 'n' veces para generar 'n' caracteres
    for i in range(n):
        # Elegimos un carácter aleatorio del conjunto
        caracter = secrets.choice(alpha_num)
        # Lo añadimos a la lista
        caracteres.append(caracter)
    
    print("Caracteres generados:", caracteres)
    # 4. Unimos todos los caracteres en una sola cadena
    codigo = ''.join(caracteres)

    # 5. Devolvemos el resultado
    return codigo


if __name__ == "__main__":

    long_code = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    print(f"Código ({long_code}): {generateRandomCodeLongVersion(long_code)} \n")
    print(f"Código ({long_code}): {generateUUIDCodeLongVersion(long_code)} \n")
    