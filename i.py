# coding=UTF-8

# 安装cv2 指令： pip install --user opencv-python -i https://pypi.douban.com/simple/
from mimetypes import init
from tkinter import image_names
import cv2
import sys
import random
import numpy as np
# https://blog.csdn.net/m0_38106923/article/details/105930886


# 镜像： 左右翻转 
def to_flip(image):
    # 0 = 上下翻转； 1 = 左右翻转； -1 = 对角线翻转
    return cv2.flip(image,1)

# 贴图操作 https://www.thinbug.com/q/46617801
def to_add(image,logo):
    width = 50

    # image = cv2.add(image,tmp) # cv中的加法
    # image = image+tmp # 直接相加

    w1, h1, c1 = image.shape
   
    w2, h2, c2 = logo.shape

    height =int( h2 *  width / w2 )
    # print(width,height)


    # cv2.imshow('logo', logo)
    # cv2.waitKey(0)

    logo = cv2.resize(logo,(width,height),interpolation=cv2.INTER_CUBIC)


    # 右上角
    roi = image[0:width, h1-height:h1]


    # 扣图： 白底 透明底
    # 灰度化
    gray_logo = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
    # 黑化
    _, black_logo = cv2.threshold(gray_logo, 170, 255, cv2.THRESH_BINARY)  # 如果颜色值大于170转化为255
    img1 = cv2.bitwise_and(roi, roi, mask=black_logo)
    # 白化
    _, white_logo = cv2.threshold(gray_logo, 170, 255, cv2.THRESH_BINARY_INV)  # 如果颜色值大于170转化为255
    img2 = cv2.bitwise_and(logo, logo, mask=white_logo)

    img3 = cv2.add(img1, img2)


    # 扣图： 黑底的图
    # 参数1：src1，第一个原数组.
    # 参数2：alpha，第一个数组元素权重
    # 参数3：src2第二个原数组
    # 参数4：beta，第二个数组元素权重
    # 参数5：gamma，图1与图2作和后添加的数值。不要太大，不然图片一片白。总和等于255以上就是纯白色了
    # img3 = cv2.addWeighted(roi, 1, logo, 1, 0)



    roi[:] = img3



    return image

# 高斯模糊
def to_gs(image):
    return cv2.GaussianBlur(image, (3, 3), 0) 

# 灰度
def to_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

# 反转
def to_bitwise_not(image):
    return cv2.bitwise_not(image) 

# RGB通道分离
def to_channels_split(image):
    b,g,r = cv2.split(image)
    return g

def op_one_img(image,i):
    # 消除噪声  高斯滤波是应用于图像处理，对图像进行滤波操作（平滑操作、过滤操作，去噪操作）
    #  cv2.GaussianBlur(image, （blur1，blur2）, 0) 
    # （blur1，blur2）是高斯核的大小，blur1和blur2的选取一般是奇数，blur1和blur2的值可以不同。参数0表示标准差取0。
    # image =to_gs(image)

    # image =to_gray(image)

    # image =to_bitwise_not(image)

    # image = to_channels_split(image)

    # 贴图
    logo = cv2.imread('logo/1.png')
    image = to_add(image,logo)

    # 翻转
    # image = to_flip(image)


    # 提取图像边缘的函数 https://blog.csdn.net/weixin_42272768/article/details/111244896
    # image = cv2.Canny(image, 50, 150) # 黑底 白线

    # 文字水印
    #cv.putText(img,text,station, font, fontsize,color,thickness,cv.LINE_AA)
    cv2.putText(image,'OpenCV',(10,100+i), cv2.FONT_HERSHEY_SIMPLEX, 2,(255,255,255),2,cv2.LINE_AA)

    return image

def readTest():
    inPath =   sys.path[0]+'/input/761.mp4'
    outPath =   sys.path[0]+'/output/out.mp4'




    cap = cv2.VideoCapture(inPath)

    fps = cap.get(cv2.CAP_PROP_FPS)  # 获得视频文件的帧率
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 获得视频文件的帧宽
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 获得视频文件的帧高
    print(fps,width,height)

    # 黑色背景图
    blackBackGround=np.zeros((int(height),int(width),3), np.uint8)
    # blackBackGround.fill(255)
    # cv2.imshow('blackBackGround', blackBackGround)
    # cv2.waitKey(0)

    
    # VideoWriter_fourcc为视频编解码器
    # fourcc意为四字符代码（Four-Character Codes），顾名思义，该编码由四个字符组成,下面是VideoWriter_fourcc对象一些常用的参数,注意：字符顺序不能弄混
    # cv2.VideoWriter_fourcc('I', '4', '2', '0'),该参数是YUV编码类型，文件名后缀为.avi 
    # cv2.VideoWriter_fourcc('P', 'I', 'M', 'I'),该参数是MPEG-1编码类型，文件名后缀为.avi 
    # cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'),该参数是MPEG-4编码类型，文件名后缀为.avi 
    # cv2.VideoWriter_fourcc('T', 'H', 'E', 'O'),该参数是Ogg Vorbis,文件名后缀为.ogv 
    # cv2.VideoWriter_fourcc('F', 'L', 'V', '1'),该参数是Flash视频，文件名后缀为.flv
    # cv2.VideoWriter_fourcc('m', 'p', '4', 'v')    文件名后缀为.mp4
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # 创建保存视频文件类对象
    # 参数1 即将保存的文件路径
    # 参数2 VideoWriter_fourcc为视频编解码器
    # 参数3 为帧播放速率
    # 参数4 (width,height)为视频帧大小
    video = cv2.VideoWriter(outPath,fourcc,fps,(int(width), int(height)),True)

    if cap.isOpened():
        i = 0
        while True:
            i = i + 1
           
            #  cap.read()按帧读取视频，ret,frame是获cap.read()方法的两个返回值。
            # 其中ret是布尔值，如果读取帧是正确的则返回True，如果文件读取到结尾，
            # 它的返回值就为False。frame就是每一帧的图像，是个三维矩阵。
            ret,img_src=cap.read()
            # cv2.imshow('Show', name)
            if not ret:break # 当获取完最后一帧就结束
            img_out = op_one_img(img_src,i)

            # 1秒抽1帧
            if i%fps !=15:
                video.write(img_out) # 保存帧
            else:
                video.write(blackBackGround) # 补了空白帧，或者应该补转场？
    else:
        print('video open fail')
    cap.release()

    print(outPath, 'done')

  



if __name__ == '__main__':
    path =   sys.path[0]+"/movie.mp4"
 
    readTest()

