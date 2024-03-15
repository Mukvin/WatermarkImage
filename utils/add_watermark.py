from PIL import Image, ImageDraw, ImageFont


def add_watermark(image_path, text, output_path, font_file, font_size, opacity=0.5):
    try:
        # open image
        img = Image.open(image_path)

        # create a opacity layer
        layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(layer)

        # get the size of image
        width, height = img.size

        # set the marked text
        font = ImageFont.truetype(font_file, font_size)

        # compute the marked text size
        text_width, text_height = draw.textsize(text, font)

        # fill the all images
        x_positions = [x for x in range(0, width, text_width)]
        y_positions = [y for y in range(0, height, text_height)]

        for x in x_positions:
            for y in y_positions:
                draw.text((x, y), text, fill=(255, 255, 255, int(255 * opacity)), font=font)

        watermarked_img = Image.alpha_composite(img.convert("RGBA"), layer)

        # save the image to be `png`
        watermarked_img.save(output_path, "TIFF")
        watermarked_img.show()
    except Exception as e:
        print(f"Error: {e}")
