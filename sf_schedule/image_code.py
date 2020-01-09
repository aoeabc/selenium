from PIL import Image
from PIL import ImageGrab
import pytesseract
import re

class ImageCode(object):

    def __init__(self,ima_file):

        self.ima_file=ima_file
        # self.ima_file = 'h:\\Image\\capture.png'

    def get_p_code(self,ima_file):
        img = Image.open(ima_file)
        code = pytesseract.image_to_string(img)
        re.sub('\W+', '', code)
        code.replace('\s','')
        code.replace(' ','')
        return code

#  打印所有像素的值
        # pixels = im.load()
        # for x in range(im.width):
        #     str = []
        #     for y in range(im.height):
        #         str.append(pixels[x, y])
        #     print(str)

    def convert_Image(self, pic_file, standard=100):
        img = Image.open(pic_file)
        img = img.convert('L')
        pixels = img.load()
        for x in range(img.width):
            for y in range(img.height):
                #  不是很黑的点（大于100）都改成白色（255）
                if pixels[x, y] > standard:
                    pixels[x, y] = 255
        img.save(pic_file)

    def get_login_code(self):
        # self.get_login_image(self.ima_file)
        self.convert_Image(self.ima_file)
        code=self.get_p_code(self.ima_file)
        return code

if __name__ == '__main__':
    c=ImageCode()
    print(c.get_login_code())

    # ima_file = 'h:\\Image\\capture_kt m3.png'
    # img = Image.open(ima_file)
    # code = pytesseract.image_to_string(img)
    # print(code)