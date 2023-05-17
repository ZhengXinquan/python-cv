import cv2
from timeit import default_timer as timer

#图片转视频
def image_to_video():
    file = 'p_720/'  # 图片目录
    output = 'ascii_720_equal.mp4'  # 生成视频路径
    num = 10218
    height = 432    #宽高一定要对应
    weight = 768
    fps = 60
    # fourcc = cv.VideoWriter_fourcc('M', 'J', 'P', 'G') 用于avi格式的生成
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # 视频编解码器
    videowriter = cv2.VideoWriter(output, fourcc, fps, (weight, height))  # 创建一个写入视频对象
    for i in range(num):
        path = file + str(i) + '.png'
        # print(path)
        frame = cv2.imread(path)
        #直方图均衡化，可不要
        # b,g,r = cv2.split(frame)
        # bH = cv2.equalizeHist(b)
        # gH = cv2.equalizeHist(g)
        # rH = cv2.equalizeHist(r)
        # frame = cv2.merge((bH, gH, rH))
        cv2.imshow('PV',frame)
        cv2.waitKey(1)
        videowriter.write(frame)

    videowriter.release()
    cv2.destroyAllWindows()
#视频转图片
def vidio2image(filename):
    cap = cv2.VideoCapture(filename)  # 打开视频
    counter = 0

    count = cap.get(cv2.CAP_PROP_FRAME_COUNT)  # 总帧数
    accum_time = 0  # 累计时间
    curr_fps = 0  # 当前帧数
    prev_time = timer()  # 上一段的时间

    while cap.isOpened():
        if count > 0:
            current = cap.get(cv2.CAP_PROP_POS_FRAMES)  # 当前第几帧
            curr_time = timer()  # 当前时间
            exec_time = curr_time - prev_time  # 处理时间
            prev_time = curr_time  # 上一段的时间设为当前时间
            accum_time = accum_time + exec_time  # 累计时间
            curr_fps = curr_fps + 1
            if accum_time >= 1:
                accum_time = accum_time - 1
                print('进度:{:.2f}%\tFPS:{}'.format(current / count * 100, curr_fps))
                curr_fps = 0  # 重置帧数
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.resize(frame,(768,432))
            cv2.imshow('frame',frame)
            cv2.waitKey(1)
            cv2.imwrite('ascii_720/'+ str(counter) + '.png',frame)
            counter += 1
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # vidio2image("神女劈观.mp4")
    image_to_video()
