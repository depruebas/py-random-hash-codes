import sys
from random_modul import generateRandomCode, generateUUIDCode

if __name__ == "__main__":

    longitud = int(sys.argv[1]) if len(sys.argv) > 1 else 10

    print(f"Código aleatorio seguro  ({longitud}): {generateRandomCode(longitud)}")
    print(f"Código basado en UUID    ({longitud}): {generateUUIDCode(longitud)}")