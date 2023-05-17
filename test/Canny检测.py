import cv2
import time
from playsound import playsound
import threading
from timeit import default_timer as timer

def audition(filepath):
    '''
        filepath:音频文件地址
    '''
    playsound(filepath)

def vidio(filepath):
    '''
        filepath:视频文件地址
    '''
    cap = cv2.VideoCapture(filepath)
    curr_fps = 0  # 当前帧数
    last_time = 0
    stratTime = time.time()
    lastFPS = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            nowTime = cap.get(0)/1000   #获取当前位置，单位为毫秒
            frame = cv2.resize(frame,(1080,640))    #修改分辨率
            codeTime = time.time() - stratTime
            sleepTime = nowTime - codeTime   #计算等待时间
            if sleepTime > 0:
                time.sleep(sleepTime)
                curr_fps = curr_fps + 1
                frame = cv2.GaussianBlur(frame, (3,3), 0)
                frame = cv2.Canny(frame, 10, 50)
                frame = cv2.putText(frame,"now:{:.2f}s".format(nowTime), (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1.0, (100, 200, 200), 5)
                frame = cv2.putText(frame,"fps:{}".format(lastFPS), (10, 100), cv2.FONT_HERSHEY_COMPLEX, 1.0, (100, 200, 200), 5)
                cv2.imshow('frame',255 - frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break 
                if int(codeTime) != last_time:
                    last_time = int(codeTime)   #记录时间
                if int(nowTime) - last_time >= 1:
                    lastFPS = curr_fps  #记录下上一秒的帧数
                    curr_fps = 0
    cap.release()
    cv2.destroyAllWindows()

if __name__ =='__main__':
    vidio_path = r"神女劈观.mp4"
    audition_path = r"44100.mp3"
    vd = threading.Thread(target=vidio,args=(vidio_path,))        #arg传入的参数为元组，因此传入单个参数的时候需要在后面加个逗号
    au = threading.Thread(target=audition,args=(audition_path,))
    vd.start()
    au.start()
    vd.join()
    au.join()   #等待进程结束
    print("程序运行结束")
    