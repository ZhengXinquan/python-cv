from moviepy.editor import VideoFileClip, TextClip, clips_array, vfx, concatenate_videoclips, CompositeVideoClip
import sys

'''
切片
'''


def readTest():
    inPath = sys.path[0]+'/input/761.mp4'
    clip = VideoFileClip(inPath)
    t = clip.duration
    print(t)

    i = 1
    while i <= 5:

        clipTemp = clip.subclip(t/5 * (i-1), t/5 * i)

        ii = 1
        while ii <= 5:
            txt = "No." + str(i) + '-' + str(ii)
            txt_clip = TextClip(txt,
                                fontsize=100, color='white')

            txt_clip = txt_clip.set_pos('center').set_duration(t/5)

            video = CompositeVideoClip([clipTemp, txt_clip])
            video.write_videofile("./output/slipt-"+txt+".mp4")
            ii += 1

        i += 1


if __name__ == '__main__':
    readTest()
