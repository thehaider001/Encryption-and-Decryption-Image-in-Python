from PIL import Image
import random

def encrypt_image(image_path, key, output_path):
    image = Image.open(image_path)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    pixels = image.load()

    width, height = image.size
    random.seed(key)

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            r = (r + random.randint(0, 255)) % 256
            g = (g + random.randint(0, 255)) % 256
            b = (b + random.randint(0, 255)) % 256

            pixels[x, y] = (b, g, r)

    image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(image_path, key, output_path):
    image = Image.open(image_path)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    pixels = image.load()

    width, height = image.size
    random.seed(key)

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            r, g, b = b, g, r

            r = (r - random.randint(0, 255)) % 256
            g = (g - random.randint(0, 255)) % 256
            b = (b - random.randint(0, 255)) % 256

            pixels[x, y] = (r, g, b)

    image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

def main():
    operation = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt an image: ").lower()
    image_path = input("Enter the path to the image file: ")
    key = int(input("Enter an encryption/decryption key (integer): "))
    output_path = input("Enter the output path for the new image (include file extension, e.g., '.png'): ")

    if operation == "encrypt":
        encrypt_image(image_path, key, output_path)
    elif operation == "decrypt":
        decrypt_image(image_path, key, output_path)
    else:
        print("Invalid operation. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
