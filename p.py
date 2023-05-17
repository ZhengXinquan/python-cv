# coding=UTF-8

# `python -m pip install --upgrade pip`

# `pip install moviepy`
# 或 清华的镜像
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple moviepy

from moviepy.editor import VideoFileClip, TextClip, clips_array, vfx, concatenate_videoclips, CompositeVideoClip

animal = VideoFileClip("./input/movie.mp4")

clip1 = VideoFileClip("./input/761.mp4").margin(0)

# clip.subclip(t_start,t_end)，截取两个时间点之间的clip片 负数倒数

# 倍速、慢放
# finalClip =clip1.speedx(0.5).write_videofile("./output/慢放0.5.mp4")

# 变暗
finalClip = clip1.fx(vfx.colorx, 0.1).write_videofile("./output/变暗.mp4")

# 前15秒 淡入
# finalClip = clip1.fx(vfx.fadein,15).write_videofile ("./output/前15秒淡入.mp4")

# # 拼接
# finalClip = concatenate_videoclips([clip1,animal]).write_videofile("./output/m.mp4")


# clip2 = clip1.fx(vfx.mirror_x)#x轴镜像
# clip3 = clip1.fx(vfx.mirror_y)#y轴镜像
# clip4 = clip1.resize(0.6)#尺寸等比缩放0.6


# #  排版
# final_clip = clips_array([
#                             [clip1, clip2],
#                             [clip3, clip4]
#                         ]).resize(width=480).write_videofile("./output/n.mp4")
# # 覆盖
# video = CompositeVideoClip([
#     clip1,
#     clip2.set_start(5), #在第5秒开始
#     clip3
#     ], size=(720,480))
# video = CompositeVideoClip([ clip1,  animal  ])
# video.write_videofile("./output/覆盖.mp4")

# Reduce the audio volume (volume x 0.8)
# clip = clip.volumex(0.8)


# 文字
# # Generate a text clip. You can customize the font, color, etc.
# txt_clip = TextClip("My Holidays 2013", fontsize=100, color='white')

# # Say that you want it to appear 10s at the center of the screen
# txt_clip = txt_clip.set_pos('center').set_duration(15)

# # Overlay the text clip on the first video clip
# video = CompositeVideoClip([clip1, txt_clip])

# # Write the result to a file (many options available !)
# video.write_videofile("./output/文字.mp4")
