from PIL import Image
import random


# ---------------------------------------
# Convert secret key string into a number
# ---------------------------------------
def generate_seed(secret_key):
    seed_value = 0
    for char in secret_key:
        seed_value += ord(char)   # Convert character to ASCII value
    return seed_value


# ---------------------------------------
# Encrypt Image (Shuffle Pixels)
# ---------------------------------------
def encrypt_image(input_path, output_path, secret_key):

    # Open image
    image = Image.open(input_path)
    image = image.convert("RGB")

    width, height = image.size

    # Convert image pixels into list
    pixel_list = list(image.getdata())

    # Generate seed from secret key
    seed_value = generate_seed(secret_key)

    # Set random seed
    random.seed(seed_value)

    # Shuffle pixels randomly
    random.shuffle(pixel_list)

    # Create new image with shuffled pixels
    encrypted_image = Image.new("RGB", (width, height))
    encrypted_image.putdata(pixel_list)

    encrypted_image.save(output_path)
    print("✅ Image Encrypted Successfully!")


# ---------------------------------------
# Decrypt Image (Reverse Shuffle)
# ---------------------------------------
def decrypt_image(input_path, output_path, secret_key):

    image = Image.open(input_path)
    image = image.convert("RGB")

    width, height = image.size
    pixel_list = list(image.getdata())

    seed_value = generate_seed(secret_key)
    random.seed(seed_value)

    # Create same shuffled index order
    indices = list(range(len(pixel_list)))
    random.shuffle(indices)

    # Create empty list for original pixels
    original_pixels = [None] * len(pixel_list)

    # Reverse shuffle
    for shuffled_position, original_position in enumerate(indices):
        original_pixels[original_position] = pixel_list[shuffled_position]

    decrypted_image = Image.new("RGB", (width, height))
    decrypted_image.putdata(original_pixels)

    decrypted_image.save(output_path)
    print("✅ Image Decrypted Successfully!")


# ---------------------------------------
# Main Program
# ---------------------------------------
print("🔐 Random Pixel Shuffling Tool")
print("--------------------------------")

image_path = input("Enter image path: ")
secret_key = input("Enter secret key: ")

print("\n1. Encrypt")
print("2. Decrypt")

choice = input("Choose option (1/2): ")

if choice == "1":
    encrypt_image(image_path, "encrypted_image.png", secret_key)

elif choice == "2":
    decrypt_image(image_path, "decrypted_image.png", secret_key)

else:
    print("Invalid choice!")