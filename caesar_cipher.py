"""
Caesar Cipher - Text Encryption & Decryption Tool
Task 1 | AVIP 2026 CyberSecurity Internship

Usage:
    python caesar_cipher.py
"""


def caesar_shift(text: str, shift: int, mode: str) -> str:
    """
    Shift every alphabet character in `text` by `shift` positions.
    Non-alphabet characters (spaces, numbers, punctuation) are left unchanged.
    mode: "encrypt" or "decrypt"
    """
    if mode == "decrypt":
        shift = -shift

    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # (position - base + shift) mod 26, then back to a character
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        else:
            # leave digits, spaces, punctuation untouched
            result.append(char)

    return "".join(result)


def encrypt(plaintext: str, shift: int) -> str:
    return caesar_shift(plaintext, shift, "encrypt")


def decrypt(ciphertext: str, shift: int) -> str:
    return caesar_shift(ciphertext, shift, "decrypt")


def run_demo():
    print("=" * 50)
    print("       CAESAR CIPHER - Encrypt / Decrypt")
    print("=" * 50)

    while True:
        print("\n1. Encrypt text")
        print("2. Decrypt text")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            text = input("Enter the text to encrypt: ")
            shift = int(input("Enter shift value (e.g. 3): "))
            result = encrypt(text, shift)
            print(f"\nOriginal : {text}")
            print(f"Shift    : {shift}")
            print(f"Encrypted: {result}")

        elif choice == "2":
            text = input("Enter the text to decrypt: ")
            shift = int(input("Enter shift value used for encryption: "))
            result = decrypt(text, shift)
            print(f"\nCiphertext: {text}")
            print(f"Shift     : {shift}")
            print(f"Decrypted : {result}")

        elif choice == "3":
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice, please select 1, 2, or 3.")


if __name__ == "__main__":
    run_demo()
