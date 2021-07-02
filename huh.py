import sys
import glob
import os
import moviepy.editor as mp
import random

def random_choice():

   vtts = glob.glob('/Volumes/BigBoiDrive/videos/newsarchive/*.vtt')

   files = []
   for vtt in vtts:
      file = vtt.split('.')
      mp4 = file[0,


   videofile = random.choice(files)
   #videofile = os.path.join('"' + videofile + '"')
   print(videofile)

   videofile2 = random.choice(files)
   #videofile2 = os.path.join('"' + videofile2 + '"')
   print(videofile2)
   
   segment_length1 = random.uniform(0.01, 10)
   segment_length2 = random.uniform(0.01, 10)
   
   print('Segment length #1:' + str(segment_length1))
   print('Segment length #2:' + str(segment_length2))

   lengths = [segment_length1, segment_length2]

   original_video = mp.VideoFileClip(videofile)
   duration = original_video.duration

   print('Cutting video #1')

   clips = []

   start = 0
   while start < duration:
       segment_length = random.choice(lengths)
       end = start + segment_length

       if end > duration:
           end = duration

       clip = original_video.subclip(start, end)

       clip = clip.resize((1280, 720))
       clips.append(clip)

       start = end


   original_video = mp.VideoFileClip(videofile2)
   duration = original_video.duration

   print('Cutting video #2')

   clips1 = []

   start = 0
   while start < duration:
       segment_length = random.choice(lengths)
       end = start + segment_length

       if end > duration:
           end = duration

       clip = original_video.subclip(start, end)

       clip = clip.resize((1280, 720))
       clips1.append(clip)

       start = end

   lt = list(zip(clips, clips1))
   out = [item for t in lt for item in t]

   zipper = random.randint(1,1000)

   final_video = mp.concatenate_videoclips(out)

   final_video.write_videofile(str(zipper) + 'zip.mp4', codec="libx264", temp_audiofile='temp-audio.m4a',
                               remove_temp=True, audio_codec='aac')


if __name__ == '__main__':
   random_choice()

