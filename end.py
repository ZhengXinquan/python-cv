from moviepy.editor import *
from moviepy.video.tools.drawing import circle

clip = VideoFileClip("./input/761.mp4", audio=False).subclip(0, 10).add_mask()

w, h = clip.size

print(w, h)

# 这里的mask是一个半径按照 r(t) = 800-200*t  根据时间变化消失的圆
# clip.mask.get_frame = lambda t: circle(screensize=(clip.w, clip.h),
#                                        center=(clip.w/2, clip.h/4),
#                                        radius=max(0, int(400-20*t)),
#                                        col1=1, col2=0, blur=4)

img = clip.to_ImageClip(6)

circle(screensize=(400, 500), center=(200, 120), radius=100,
       col1=(0, 0, 0), col2=(255, 255, 0), blur=4)
print(img)
print(clip)

# 搞一个TextClip来放The End
# the_end = TextClip("The End",  color="white",
#                    fontsize=70).set_duration(clip.duration)

final = CompositeVideoClip([img.set_duration(clip.duration).set_pos('center'), clip],
                           size=clip.size)


final.write_videofile("./output/end.mp4")
