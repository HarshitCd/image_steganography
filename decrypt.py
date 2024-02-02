import utils as ut


def main():
    out_img = ut.load_image(path="local/output.png")
    print(ut.decoding(ut.decode_img(out_img)).decode(encoding="utf-8"))


if __name__ == "__main__":
    main()
