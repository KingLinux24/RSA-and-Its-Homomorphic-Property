import socket
import random

def request_public_key(host='localhost', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b'REQUEST_PUBLIC_KEY')
        data = s.recv(1024).decode()
        e, n = map(int, data.split(','))
        return e, n

def encrypt(m, e, n):
    return pow(m, e, n)

def generate_plaintext(bits=4):
    return random.randint(2**(bits-1), 2**bits - 1)

def send_ciphertext(ciphertext, host='localhost', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(str(ciphertext).encode())

if __name__ == "__main__":
    e, n = request_public_key()
    plaintext = generate_plaintext()
    ciphertext = encrypt(plaintext, e, n)
    print(f"User B Plaintext: {plaintext}")
    print(f"User B Public Key (e, n): ({e}, {n})")
    print(f"User B Ciphertext: {ciphertext}")

    # Send ciphertext to User A
    send_ciphertext(ciphertext)
