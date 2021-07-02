import sys

import moviepy.editor as mp


def randomize_videos(videofile, videofile2, segment_length):
    original_video = mp.VideoFileClip(videofile)
    duration = original_video.duration

    clips = []

    start = 0
    while start < duration:
        end = start + segment_length

        if end > duration:
            end = duration

        clip = original_video.subclip(start, end)

        clip = clip.resize((1280, 720))
        clips.append(clip)

        start = end


    original_video = mp.VideoFileClip(videofile2)
    duration = original_video.duration

    clips1 = []

    start = 0
    while start < duration:
        end = start + segment_length

        if end > duration:
            end = duration

        clip = original_video.subclip(start, end)

        clip = clip.resize((1280, 720))
        clips1.append(clip)

        start = end

    lt = list(zip(clips, clips1))
    out = [item for t in lt for item in t]

    final_video = mp.concatenate_videoclips(out)

    final_video.write_videofile('vidzip.mp4', codec="libx264", temp_audiofile='temp-audio.m4a',
                                remove_temp=True, audio_codec='aac')


if __name__ == '__main__':
    randomize_videos(sys.argv[1], sys.argv[2], float(sys.argv[3]))
