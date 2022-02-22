from PIL import Image
import pathlib
maxsize = (180, 272) #(width, height)
for input_img_path in pathlib.Path("sienna").iterdir():
    output_img_path = str(input_img_path).replace("sienna","edited") #old folder, new folder
    with Image.open(input_img_path) as im:
        im.thumbnail(maxsize, Image.ANTIALIAS)
        # im = im.rotate(90, expand = 1) #sometimes you need it, sometimes you don't
        im.save(output_img_path, "JPEG", dpi=(300,300))
        print(f"processing file {input_img_path} done...")