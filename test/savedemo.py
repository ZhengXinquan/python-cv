import cv2
from timeit import default_timer as timer


def process_video(filename=0, func=None, output='result.mp4', verbose=0):
    """处理视频

    :param filename: 视频源，默认为摄像头
    :param func: 处理每一帧的函数名
    :param output: 保存的文件名
    :param verbose: 可视化，0不可视化，1显示处理后的结果，2显示对比结果
    """
    cap = cv2.VideoCapture(filename)  # 打开摄像头
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # 视频编解码器
    fps = cap.get(cv2.CAP_PROP_FPS)  # 帧数
    width, height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 宽高
    out = cv2.VideoWriter(output, fourcc, fps, (width, height))  # 写入视频

    if verbose > 0 or filename == 0:
        print('英文下输入q停止')

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
            result = func(frame) if func else frame
            out.write(result)  # 写入帧
            if verbose > 0 or filename == 0:
                cv2.imshow('after', result)
                if verbose == 2:
                    cv2.imshow('before', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):  # q退出
                    break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    process_video("神女劈观.mp4")
