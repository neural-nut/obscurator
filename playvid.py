import random
import glob
import subprocess
import os

def main ():

   files = glob.glob('/Volumes/BigBoiDrive/videos/newsarchive/*.mp4')

   vid = random.choice(files)
   vid = os.path.join('"' + vid + '"')
   os.system('open ' + vid)
   with open('vlog.txt', 'a') as f:
   	  f.write(vid + '\n')

if __name__ == '__main__':
		main()