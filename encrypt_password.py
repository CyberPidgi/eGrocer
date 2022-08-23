import hashlib

def encrypt_password(password):
    return str(hashlib.sha512(password.encode()).hexdigest())


if __name__ == "__main__":
    print(str(encrypt_password("password")))