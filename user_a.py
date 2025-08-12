import socket
import random
from sympy import isprime
from math import gcd

def generate_prime(bits=6):
    while True:
        num = random.getrandbits(bits)
        if num >= 2**(bits-1) and isprime(num):
            return num

def modinv(a, m):
    # Extended Euclidean Algorithm for modular inverse
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

class RSA:
    def __init__(self, bits=6):
        self.p = generate_prime(bits)
        self.q = generate_prime(bits)
        while self.q == self.p:
            self.q = generate_prime(bits)
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = 3
        while gcd(self.e, self.phi) != 1:
            self.e += 2
        self.d = modinv(self.e, self.phi)

    def encrypt(self, m):
        return pow(m, self.e, self.n)

    def decrypt(self, c):
        return pow(c, self.d, self.n)

def start_server(host='localhost', port=65432):
    rsa = RSA(bits=6)
    print(f"User A RSA Key Generation:")
    print(f"Public Key (e, n): ({rsa.e}, {rsa.n})")
    print(f"Private Key (d, n): ({rsa.d}, {rsa.n})")
    print(f"Primes p: {rsa.p}, q: {rsa.q}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"User A listening on {host}:{port}...")

        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            # Receive public key request or ciphertext
            data = conn.recv(1024).decode()
            if data == 'REQUEST_PUBLIC_KEY':
                # Send public key to client
                pubkey_str = f"{rsa.e},{rsa.n}"
                conn.sendall(pubkey_str.encode())
                print("Sent public key to client.")
                # Receive ciphertext
                ciphertext_data = conn.recv(1024).decode()
                ciphertext = int(ciphertext_data)
                print(f"Received ciphertext: {ciphertext}")
                decrypted = rsa.decrypt(ciphertext)
                print(f"Decrypted plaintext: {decrypted}")
            else:
                print("Unexpected data received.")

if __name__ == "__main__":
    start_server()
