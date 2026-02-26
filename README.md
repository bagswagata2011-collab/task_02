# 🔐 Task_02 : Random Pixel Shuffling Image Encryption and Decryption Tool










A deterministic image encryption and decryption tool built in Python using pixel-level manipulation.
This project implements a secret key–based random pixel shuffling algorithm to securely scramble and restore images.

## 📌 Project Overview

This project demonstrates how deterministic randomness can be applied to image encryption.

Instead of modifying RGB values, the algorithm:

Extracts pixel data from the image

Uses a secret key to generate a reproducible random seed

Shuffles pixel positions during encryption

Reverses the shuffle during decryption

Correct key → Original image restored
Wrong key → Image remains scrambled

## 🛠 Tech Stack

Language: Python 3.x

Library: Pillow (PIL)

Core Concepts:

Pixel Manipulation

Random Seed Generation

Deterministic Shuffling

Reversible Mapping Algorithm



## 2️⃣ Install Required Library
pip install pillow
## ▶ Usage

Run the program:

python main.py

You will be prompted to:

Enter image path

Enter secret key

Choose:

1 → Encrypt

2 → Decrypt

Output files generated:

encrypted_image.png

decrypted_image.png

🧠 Algorithm Explanation
🔑 Secret Key to Seed Conversion

The secret key entered by the user is converted into a numeric seed by summing the ASCII values of its characters.

Example:

Key: abc
ASCII: 97 + 98 + 99
Seed: 294

This ensures:

Same key → Same shuffle order

Different key → Different encryption

## 🔄 Encryption Process

Load image using Pillow

Convert image to RGB format

Extract pixel data using getdata()

Convert pixels to a list

Generate seed from secret key

Set random seed

Shuffle pixel list

Reconstruct and save encrypted image

The image structure becomes visually scrambled while pixel values remain unchanged.

## 🔁 Decryption Process

Regenerate seed using the same key

Recreate the same shuffled index order

Reverse the pixel mapping

Restore original pixel arrangement

Save decrypted image

Because the random generator is seeded, the shuffle is reproducible and reversible.



## 🚀 Future Improvements

Multi-layer encryption (Shuffle + XOR)

Block-wise pixel scrambling

Chaotic map–based encryption

GUI version

Password strength validation

Performance optimization for large images

## 🎓 Learning Outcomes

By completing this project, you gain understanding of:

Image processing fundamentals

Deterministic randomness

Reversible algorithm design

Seed-based encryption logic

Practical implementation of cryptographic concepts
