import os
import sys
import Colour

VideoInput=sys.argv
os.system('ffmpeg -i '+str(VideoInput[1])+' -r 1/1 $filename%d.bmp')
path=os.getcwd()
ImageFiles = [f for f in os.listdir(path) if f.endswith('.bmp')]

for o in ImageFiles:
	g="python3 predict.py -c config.json -w trained_wts.h5 -i "+o
	os.system(g)
	os.remove(o)
	files = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path,i)) and 'Part_' in i]
	for j in files:
		Result = Colour.ColorThreshold(j)
		os.remove(j)
		if Result:
			FileName=os.path.splitext(o)
			os.remove(FileName[0]+'_detected.bmp') 

