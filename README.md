# RSA and Its Homomorphic Property

## 📚 Assignment
**Course:** Cryptography Lab  
**Instructor:** Dr. Mukti Padhya  
**Date:** 21 Feb (Edited 26 Feb)  
**Points:** 100  
**Due Date:** 26 Feb, 23:59  

---

## **Objective**
Implement a two-party socket communication system (User A and User B) and demonstrate:
1. **Scenario 1** — RSA encryption and decryption between User A and User B.
2. **Scenario 2** — Demonstration of RSA's **multiplicative homomorphic property** involving User A, User B, and User C.

---

## **Scenarios**

### **Scenario 1**
1. **User A** generates a key pair (p and q at least 6-bit primes), shares the public key with User B.
2. **User B** generates a random plaintext (≥4-bit), encrypts it with User A’s public key.
3. **User B** sends the ciphertext to User A.
4. **User A** decrypts using the private key.
5. Public parameters, private key, plaintext, ciphertext, and decrypted text are displayed.

---

### **Scenario 2**
1. **User B** encrypts plaintext `M1` → ciphertext `C1` using User A’s public key, sends `C1` to **User C**.
2. **User C** encrypts plaintext `M2` → ciphertext `C2` using the same public key.
3. **User C** multiplies `C1 * C2` → final ciphertext `C`.
4. **User C** sends `C` to **User A**.
5. **User A** decrypts `C` to obtain `(M1 * M2) mod n`, demonstrating RSA's **multiplicative property**.

---

## **How It Works**
- **RSA Key Generation:**  
  - Random 6-bit prime numbers for `p` and `q`  
  - `n = p * q`  
  - `phi(n) = (p-1)*(q-1)`  
  - Choose public exponent `e` (coprime with phi)  
  - Compute private exponent `d` (modular inverse of `e` mod phi)  
- **Communication:**  
  - Implemented via Python sockets (`socket` library)  
  - JSON format for data exchange  
  - Role identification for User A, B, C  
- **Homomorphic Demonstration:**  
  - Uses property:  
    ```
    RSA(m1) * RSA(m2) mod n = RSA(m1 * m2 mod n)
    ```

---

## **Folder Structure**

rsa-homomorphic-assignment/
│
├── user_a.py # User A (server) – key generation, decryption, relay
├── user_b.py # User B (client) – encryption, send ciphertext
├── user_c.py # User C (client) – encryption, multiplication
├── README.md # Documentation
└── LICENSE # License file




---

## **Running the Programs**
1. **Start User A (Server):**


   `bash`
  ` python3 user_a.py`<br>
  
2.**Run User B (Client):**


`python3 user_b.py`<br>

3.**Run User C (Client) (Scenario 2 only):**


`python3 user_c.py`


## Example Output
[A] RSA keys generated: <br>
    p = 67, q = 71 <br>
    n = 4757, e = 5, d = 1865 <br>
[A] Listening on 127.0.0.1:9000 ... <br>

[B][Scenario1] Plaintext m=15, ciphertext c=759 <br>
[A][Scenario1] Decrypted message: 15 <br>

[A][Scenario2] Decrypted product (m1*m2 mod n): 315<br>






