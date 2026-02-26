🔐 Random Pixel Shuffling Image Encryption Decryption Tool

A Python-based Image Encryption and Decryption Tool that uses Random Pixel Shuffling with a user-defined secret key.

This project demonstrates how pixel-level manipulation can be used to encrypt and decrypt images in a reversible way.

📌 Project Overview

This tool works by:

Converting image pixels into a list

Shuffling the pixels using a secret key

Saving the shuffled image as encrypted output

Reversing the shuffle using the same key to decrypt

If the correct secret key is provided during decryption, the original image is restored.

🚀 Features

🔑 Secret key-based encryption

🔄 Fully reversible decryption

🖼 Pixel-level image manipulation

🧠 Deterministic random shuffling using seed

💻 Simple terminal-based interface (No GUI)

📦 Lightweight and easy to use

🛠 Technologies Used

Python

Pillow (PIL)

Random Module

🧠 How It Works
1️⃣ Secret Key to Seed Conversion

The user enters a secret key.

The program converts each character of the key into its ASCII value and adds them together to generate a numeric seed.

Example:

Key: abc
a = 97
b = 98
c = 99
Seed = 294

This seed controls the random shuffle.

Same key → Same seed → Same shuffle order.

2️⃣ Encryption Process

Image pixels are extracted into a list.

Random seed is set using the generated seed value.

Pixels are shuffled randomly.

New encrypted image is saved.

The image becomes visually scrambled.

3️⃣ Decryption Process

Same secret key is entered.

Same random seed is generated.

Same shuffle order is recreated.

Shuffle mapping is reversed.

Original image is restored.

If the wrong key is entered, the image remains scrambled.

📂 Project Structure
random-pixel-encryption/
│
├── main.py
├── input_image.png
├── encrypted_image.png
├── decrypted_image.png
└── README.md
⚙ Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/random-pixel-encryption.git
cd random-pixel-encryption
2️⃣ Install Dependencies
pip install pillow
▶ How to Run
python main.py

Then:

Enter image path

Enter secret key

Choose:

1 → Encrypt

2 → Decrypt

🔐 Security Note

This project is for educational and academic purposes.

It demonstrates:

Deterministic randomness

Reversible transformations

Pixel-level image manipulation

For real-world secure encryption, use:

AES

RSA

Python cryptography libraries

🎓 Learning Outcomes

By completing this project, you understand:

Image processing using Pillow

Pixel extraction and manipulation

Random seeding and reproducibility

Encryption and decryption logic

Reversible mapping algorithms

💡 Future Improvements

Multi-layer encryption (Shuffle + XOR)

Block-wise scrambling

Chaotic map encryption

GUI version

Password strength validation
