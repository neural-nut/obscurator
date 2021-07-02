from random import *
import moviepy.editor as mp
from moviepy.editor import *
from sys import argv


def cut_up(videofile, segment_length):
    original_video = mp.VideoFileClip(videofile)
    original_video = original_video.subclip(t_start=0, t_end=300)
    duration = original_video.duration

    clips = []
    clip_start = 0
    while clip_start < duration:
        clip_end = clip_start + segment_length

        if clip_end > duration:
            clip_end = duration

        clip = original_video.subclip(clip_start, clip_end)
        clips.append(clip)

        clip_start = clip_end
    #print(clips)
    return clips


def shuffle_in_place(clips, segment_length, divisor):
    """Take Clips [🥩 🏳️ 🚘] split [🥓🍖🍗 🚩🏁🏴 🚕🚒🚑] into claps 👏👏🏿👏🏻
    and shuffle them in place 👏[🍗🥓🍖], 👏🏿[🏴🚩🏁], 👏🏻[🚒🚑🚕]"""

    sub_segment = segment_length / divisor

    ordered_clips = []
    for c in clips:
        duration = c.duration

        claps = []
        clip_start = 0
        while clip_start < duration:
            clip_end = clip_start + sub_segment

            if clip_end > duration:
                clip_end = duration

            clip = c.subclip(clip_start, clip_end)
            claps.append(clip)

            clip_start = clip_end

        shuffle(claps)
        print('shuffling claps 👏👏🏻👏🏼👏🏽👏🏾👏🏿\nshufflingclaps👏🏿👏🏾👏👏🏻👏🏼')

        for clap in claps:
            ordered_clips.append(clap)
            print ('appended clap' + clap)

    return ordered_clips
    print('~~~~~~~~~~~~~~~~~~~~~\n'
          '~~~~ORDERED CLIPS~~~~\n'
          '~~~~~~~~~~~~~~~~~~~~~\n' + ordered_clips)


def the_lottery(ordered_clips, frisk, divisor):

    clumps = []
    n = 0

    for rc in ordered_clips:
        lotto = randint(0, int(frisk))
        duration = rc.duration

        n += 1
        print('Cleeping Clump #' + str(n) + ' out of ' + str(len(ordered_clips)) + ' Clorps 🤹🏻‍♀️')
        print('Your lucky lotto number is #' + str(lotto))

        if lotto == 0:
            low = duration / 100
            high = duration / 2

            d_off = uniform(low, high)
            d_on = uniform(low, high)

            try:
                rc = vfx.blink(rc, d_on, d_off)
            except:
                pass
                print('Computer did a #1 whoopsies... 😅 👋 😬 🤖')

        elif lotto == 1:
            '''Time_Mirror Clip'''

            try:
                rc = vfx.time_mirror(rc)
            except:
                pass
                print('Computer did a #1 whoopsies... 😅 👋 😬 🤖')

        elif lotto == 2:
            '''SuperSample Clip'''

            dividend = randint(1, int(divisor))
            if dividend == 0:
                dividend = 1

            d = divisor / dividend
            frames = randint(0, 20)*d

            try:
                rc = vfx.supersample(rc, d, int(frames))
            except:
                pass
                print('Computer did a #2 whoopsies... 😅 👋 😬 🤖')

        elif lotto == 3:
            '''Accelerate and Decelerate Clip'''
            limit = (8/(duration**2) + (1/divisor))
            multiplier = uniform(1/limit, limit)
            new = duration*multiplier

            abrupt = uniform(-4, 4)

            try:
                rc = vfx.accel_decel(rc, new, abrupt)
            except:
                pass
                print('Computer did a #3 whoopsies... 😅 👋 😬 🤖')
        elif lotto == 4:
            '''Paint Clip'''
            sat = uniform(0.1, 10)
            lines = uniform(0.0001, 1)
            try:
                rc = vfx.painting(rc, sat, lines)
            except:
                pass
                print('Computer did a #4 whoopsies... 😅 👋 😬 🤖')
        elif lotto == 5:
            '''Time-Symmetrize Clip'''
            try:
                rc = vfx.time_symmetrize(rc)
            except:
                pass
                print('Computer did #5 a whoopsies... 😅 👋 😬 🤖')
        elif lotto == 6:
            '''Normalcy'''
            x = ordered_clips.index(rc)
            try:
                rc = []
                for i in range(x, x + 6):
                    rd = ordered_clips[i]
                    rc.append(rd)
            except:
                pass
                print('Computer did #6 a whoopsies... 😅 👋 😬 🤖')
        elif lotto == 7:
            '''Foresight'''
            x = ordered_clips.index(rc)
            i = x + randint(20, 100)
            try:
                try:
                    rc = ordered_clips[i]
                except:
                    rc = ordered_clips[i-10]
                else:
                    rc = ordered_clips[i - 20]
                finally:
                    rc = ordered_clips[-1]
            except:
                pass
                print('Computer did #7 a whoopsies... 😅 👋 😬 🤖')

        elif lotto > 7:
            '''Clip goes unchanged'''
            pass
        try:
            clumps.append(rc)
        except:
            for r in rc:
                clumps.append(r)

        return clumps

def main(clumps):
    n = 0
    for c in clumps:
        n += 1
        print(str(n) + ' - ' + str(c))
    numba = randint(1, 1000)
    output = str(numba) + ' - random.mp4'
    print(str(len(clumps)) + ' Klormps in the end\n\n\n\nNice job kid.')
    print('Sticking the clumps together 🍡🍢🍡🍢🍡')
    final_video = mp.concatenate_videoclips(clumps)
    print('They stuck!! 🎉 🥳 🎈 🎊 🎁 🍾 👯‍ ️👯 👯‍ ️🪅')
    final_video.write_videofile(output, codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True,
                                audio_codec='aac')


if __name__ == '__main__':
    videofile = argv[1]
    segment_length = int(argv[2])
    divisor = int(argv[3])
    frisk = int(argv[4])
    clips = cut_up(videofile, segment_length)
    ordered_clips = shuffle_in_place(clips, segment_length, divisor)
    clumps = the_lottery(ordered_clips, frisk, divisor)
    main(clumps)


    #randomize_video(sys.argv[1], float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
