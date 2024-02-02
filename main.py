import cv2
import numpy as np
from PIL import Image


def get_bytes_array(message: str) -> bytearray:
    return bytearray(message, encoding="utf-8")


def process_img_data(message: str, img_data):
    rows, cols, _ = img_data.shape

    byte_message = encoding(get_bytes_array(message=message))
    n = 0
    for i in range(rows):
        for j in range(cols):
            for id, _ in enumerate(img_data[i, j]):
                if n < len(byte_message):
                    if img_data[i, j][id] % 2 != byte_message[n]:
                        img_data[i, j][id] += 1
                    n += 1
                else:
                    if img_data[i, j][id] % 2 != 0:
                        img_data[i, j][id] += 1

    return img_data


def decode_img(img_data) -> list:
    rows, cols, _ = img_data.shape
    data = list()
    for i in range(rows):
        for j in range(cols):
            for k in img_data[i, j]:
                data.append(k % 2)

    return data


def create_image(out_path: str, img_data):
    pass


def load_image(path: str):
    return cv2.imread(path)


def encoding(b: bytearray) -> list:
    data = list()

    for x in b:
        for _ in range(8):
            data.append(x & 1)
            x >>= 1

    return data


def decoding(data: list) -> bytearray:
    x = 0
    decoded_data = list()
    for i, a in enumerate(data[::-1]):
        x |= a
        if (i + 1) % 8 == 0:
            decoded_data.append(x)
            x = 0
        else:
            x <<= 1

    return bytearray(decoded_data[::-1])


def main():
    img_path = "/Users/harshitcd/Downloads/example.png"
    img = load_image(path=img_path)

    steg_img = process_img_data(message="Hello World", img_data=img)
    width, height, _ = steg_img.shape

    pixels = list()
    for col in steg_img:
        for pixel in col:
            pixels.append(pixel)

    img = Image.new("RGB", (width, height))
    img.putdata(pixels)
    img.save("image.png")
    print(decoding(decode_img(steg_img)).decode(encoding="utf-8"))


if __name__ == "__main__":
    main()
