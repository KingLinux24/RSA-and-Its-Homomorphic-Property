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
    plaintext_m2 = generate_plaintext()
    ciphertext_c2 = encrypt(plaintext_m2, e, n)
    print(f"User C Plaintext M2: {plaintext_m2}")
    print(f"User C Ciphertext C2: {ciphertext_c2}")

    # For demonstration, we assume ciphertext C1 is provided by User B manually or via other means
    ciphertext_c1 = int(input("Enter ciphertext C1 received from User B: "))

    # Multiply ciphertexts modulo n
    ciphertext_c = (ciphertext_c1 * ciphertext_c2) % n
    print(f"User C multiplied ciphertext C = C1 * C2 mod n: {ciphertext_c}")

    # Send the multiplied ciphertext to User A
    send_ciphertext(ciphertext_c)
