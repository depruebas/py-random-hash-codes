import secrets
import uuid
import base64


def generateRandomCode(n):
    alpha_num = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'  
    return ''.join(secrets.choice(alpha_num) for _ in range(n))


def generateUUIDCode(n):
    u = uuid.uuid4()
    b64 = base64.urlsafe_b64encode(u.bytes).decode('utf-8').rstrip('=')
    return b64[:n]