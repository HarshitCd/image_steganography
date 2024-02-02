import utils as ut


def main():
    img_path = "local/tmp.jpg"
    img = ut.load_image(path=img_path)

    msg = ""
    with open("local/message.txt", "r") as f:
        msg = f.read()

    steg_img = ut.process_img_data(message=msg, img_data=img)
    ut.create_image("local/output.png", steg_img)


if __name__ == "__main__":
    main()
