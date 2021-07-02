import sys
import moviepy.editor as mp
import os

def concat(dir):

    roots = os.listdir(dir)
    paths = []
    for root in roots:
        path = os.path.join(dir + root)
        paths.append(path)
        print(paths)

    videos = []
    for f in paths:
        print(f)
        video = mp.VideoFileClip(f)
        videos.append(video)
    
    out = os.strip(root[1], "."[-1])
    out = (out + '_CAT.mp4')

    final_video = mp.concatenate_videoclips(videos, method="compose")
    final_video.write_videofile(out, codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')

if __name__ == '__main__':
    concat(sys.argv[1])