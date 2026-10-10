# Caesar Cipher — Text Encryption & Decryption

**AVIP 2026 | CyberSecurity Internship | Task 1**

A simple command-line tool that encrypts and decrypts text using the
classic Caesar Cipher technique, with a configurable shift value.

## How the Caesar Cipher works

Each letter in the plaintext is shifted a fixed number of positions
down (or up) the alphabet. For example, with a shift of `3`:

- `A` → `D`
- `B` → `E`
- `Z` → `C` (wraps around)

Non-alphabet characters (spaces, numbers, punctuation) are left
unchanged. Uppercase and lowercase letters are both supported and
preserve their case.

## Requirements

- Python 3.x (no external libraries needed)

## How to run

```bash
python caesar_cipher.py
```

You'll see a menu to choose Encrypt, Decrypt, or Exit.

## Usage Examples

### Example 1 — Encryption

```
Enter the text to encrypt: Hello, World! 123
Enter shift value (e.g. 3): 3

Original : Hello, World! 123
Shift    : 3
Encrypted: Khoor, Zruog! 123
```

### Example 2 — Decryption

```
Enter the text to decrypt: Khoor, Zruog! 123
Enter shift value used for encryption: 3

Ciphertext: Khoor, Zruog! 123
Shift     : 3
Decrypted : Hello, World! 123
```

## Sample Execution Transcript

See [`sample_io.txt`](./sample_io.txt) for a full recorded run
covering both encryption and decryption, including edge cases
(numbers, punctuation, mixed case).

## Project Structure

```
CS_1_CaesarCipher_byte/
├── caesar_cipher.py   # main program
├── README.md          # this file
└── sample_io.txt      # sample input/output transcript
```

## Author

Built as part of the Arithmatrix Virtual Internship Program (AVIP) 2026,
CyberSecurity track.
