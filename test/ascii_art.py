from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2

sample_rate = 0.4
count = 1

def ascii_art(file):
    # im = Image.open(file)
    # img = cv2.imread(file)
    im = Image.fromarray(cv2.cvtColor(file,cv2.COLOR_BGR2RGB))

    # Compute letter aspect ratio
    font = ImageFont.load_default()
    # font = ImageFont.truetype("SourceCodePro-Bold.ttf", size=12)
    aspect_ratio = font.getsize("x")[0] / font.getsize("x")[1]
    new_im_size = np.array(
        [im.size[0] * sample_rate, im.size[1] * sample_rate * aspect_ratio]
    ).astype(int)

    # Downsample the image
    im = im.resize(new_im_size)

    # Keep a copy of image for color sampling
    im_color = np.array(im)

    # Convert to gray scale image
    im = im.convert("L")

    # Convert to numpy array for image manipulation
    im = np.array(im)

    # Defines all the symbols in ascending order that will form the final ascii
    symbols = np.array(list(" .-vM"))

    # Normalize minimum and maximum to [0, max_symbol_index)
    im = (im - im.min()) / (im.max() - im.min()) * (symbols.size - 1)

    # Generate the ascii art
    ascii = symbols[im.astype(int)]

    # Create an output image for drawing ascii text
    letter_size = font.getsize("x")
    im_out_size = new_im_size * letter_size
    bg_color = "black"
    im_out = Image.new("RGB", tuple(im_out_size), bg_color)
    draw = ImageDraw.Draw(im_out)

    # Draw text
    y = 0
    for i, line in enumerate(ascii):
        for j, ch in enumerate(line):
            color = tuple(im_color[i, j])  # sample color from original image
            draw.text((letter_size[0] * j, y), ch[0], fill=color, font=font)
        y += letter_size[1]  # increase y by letter height

    # Save image file
    return cv2.cvtColor(np.asarray(im_out),cv2.COLOR_RGB2BGR)

#转化过程中，遇到完全黑色的图片会报错，所以这里选择忽略黑色图片
def try_ascii(img,count):
    try:
        image = ascii_art(img)
        image = cv2.resize(image,(768,432))
    except:
        image = img
    # cv2.imshow('PV',image)
    # cv2.waitKey(1)
    #写入地址
    cv2.imwrite('p_720/'+ str(count) + '.png',image)

#将视频转化为字符图片保存
def readPic():
    count = 0
    while count<=10218:
        #读取图片的地址，可自行改为视频格式
        img = cv2.imread('ascii_720/'+str(count)+'.png')
        # cv2.imshow('PV',img)
        # cv2.waitKey(1)
        try_ascii(img,count)
        print("进度：{:.2f}%,当前帧：{}".format((count/10218.)*100,count))
        count+=1



if __name__ == "__main__":
    readPic()