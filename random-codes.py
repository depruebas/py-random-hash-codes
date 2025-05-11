import secrets
import sys
import uuid
import base64


def generateRandomCode(n):
    alpha_num = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'  # sin caracteres ambiguos
    return ''.join(secrets.choice(alpha_num) for _ in range(n))


def generateUUIDCode(n):
    u = uuid.uuid4()
    b64 = base64.urlsafe_b64encode(u.bytes).decode('utf-8').rstrip('=')
    return b64[:n]


if __name__ == "__main__":

    long_code = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    print(f"Código ({long_code}): {generateRandomCode(long_code)}")
    print(f"Código ({long_code}): {generateUUIDCode(long_code)} \n")
