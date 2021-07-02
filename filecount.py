import os
import glob
import re
import sys


def filecount(directory):
    os.chdir(directory)

    srt = glob.glob('*.srt')
    print('.srt count:' + str(len(srt)))

    ensrt = glob.glob('*.en.srt')
    print('.en.srt count:' + str(len(ensrt)))

    vtts = glob.glob('*.vtt')
    print('.vtt count:' + str(len(vtts)))

    fails = []
    for f in directory:
        filename = f.split('.')

        filename = '.'.join(filename[0:-1])
        vtt = glob.glob(filename + '*.vtt')

        if len(vtt) == 0:
            fails.append({'vtt': vtt[0], 'video': f})

    print(fails)
   

    envtt = glob.glob('*.en.vtt')
    print('.en.vtt count:' + str(len(envtt)))

    mp5 = glob.glob('*.mp4')
    print('.mp4 count:' + str(len(mp5)))

    part = glob.glob('*.mp4.part')
    print('.mp4.part count:' + str(len(part)))


def getids(directory):
    os.chdir(directory)
    mp5 = glob.glob('*.mp4')
    for f in mp5:
        f = os.path.join(directory + '/' + f)
        print(f)
    ids = []
    for f in mp5:
        id = re.findall('([a-zA-Z0-9_-]{11})(?=\.|(\s\-\s))', f)
        if len(id) > 0:
            ids.append(id)
    ids = (str(ids))
    myds = re.findall('\w{11}', ids)
    for id in myds:
        print(id)

    length = len(myds)
    print('ids count:' + str(length))


if __name__ == '__main__':
    filecount(sys.argv[1])
    getids(sys.argv[1])
