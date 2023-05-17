import cv2
import time
from playsound import playsound
import threading

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
    rate = cap.get(5)   #获取帧率
    # count = 1
    stratTime = time.time()
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            nowTime = cap.get(0)/1000   #获取当前位置，单位为毫秒
            # nowRate = cap.get(1)        #获取当前帧数
            sleepTime = nowTime - time.time() + stratTime   #计算等待时间
            # sleepTime = count/rate - time.time() + stratTime   #计算等待时间
            # sleepTime = nowRate/rate - time.time() + stratTime   #计算等待时间
            if sleepTime > 0:
                time.sleep(sleepTime)
            frame = cv2.putText(frame,"vidio Time:{:.2f}s".format(nowTime), (50, 100), cv2.FONT_HERSHEY_COMPLEX, 2.0, (100, 200, 200), 5)
            frame = cv2.putText(frame,"code Time:{:.2f}s".format(time.time() - stratTime), (50, 200), cv2.FONT_HERSHEY_COMPLEX, 2.0, (100, 200, 200), 5)
            frame = cv2.putText(frame,"Rate:{}".format(rate), (50, 300), cv2.FONT_HERSHEY_COMPLEX, 2.0, (100, 200, 200), 5)
            frame = cv2.resize(frame,(1080,640))    #修改分辨率
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            # count+=1        
    cap.release()
    cv2.destroyAllWindows()

if __name__ =='__main__':
    vidio_path = r"字幕.mp4"
    audition_path = r"44100.mp3"
    vd = threading.Thread(target=vidio,args=(vidio_path,))        #arg传入的参数为元组，因此传入单个参数的时候需要在后面加个逗号
    au = threading.Thread(target=audition,args=(audition_path,))
    vd.start()
    au.start()
    vd.join()
    au.join()   #等待进程结束
    print("程序运行结束")
    