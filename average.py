from moviepy.editor import VideoFileClip, ImageClip
clip = VideoFileClip("./input/761.mp4")
fps= 1.0 # take one frame per second
nframes = clip.duration*fps # total number of frames used
total_image = sum(clip.iter_frames(fps,dtype=float))
average_image = ImageClip(total_image/ nframes)
average_image.save_frame("./output/average.png")