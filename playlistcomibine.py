import os
import timeit
from glob import glob
from datetime import datetime

from pydub import AudioSegment
path =r'C:/Users/Sam/Box Sync/05 Track- 5/'
foldername= path.split('/')[-2]

#can use alternate between \\ or / for path
destdir = r'C:/Users/Sam/Documents/python/playgrond/'
# use this for whole directory
dirlist = [s for s in os.listdir(path)]
# use this for selected folders
# dirlist =['CD-3','CD-4','CD-5','CD-6', 'CD-7', 'CD-8','CD-9']
# dirlist =['CD-3']
# print(os.getcwd())
print("starting combining files")
starttime = datetime.now()
# print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
for dir in dirlist:
    srcdir = path + dir +'\\'
    # srcdir = dir
    print(srcdir)
    os.chdir(srcdir)
    if not os.path.isdir(srcdir):    
        print("%sthis is not Directory", srcdir)
        continue
    filelist = [f for f in os.listdir(srcdir)]
    if  len(filelist) <=0:
        continue
    
    for f in os.listdir(srcdir):
        print(f)

    start = timeit.timeit()
    playlist_songs = [AudioSegment.from_mp3(mp3_file) for mp3_file in glob("*Track*.mp3")]
    first_song = playlist_songs.pop(0)
    beginning_of_song = first_song
    playlist = beginning_of_song
    for song in playlist_songs:
        playlist = playlist.append(song, crossfade=(1 * 1000))
    playlist = playlist.fade_out(30)
    playlist_length = len(playlist) / (1000*60)
   
    os.chdir(destdir)
    print(destdir)
    if not os.path.isdir(foldername):
        os.mkdir(foldername)
    os.chdir(foldername)
    fout= "%sminute_playlist.mp3" % str(playlist_length)[:5]
    with open(fout,"wb") as outfile:
        playlist.export(outfile, format='mp3')
    os.rename(fout, dir+".mp3")
    end = timeit.timeit()
    elapsed = start - end 
    print("time Taken>>" + str(elapsed))
print("Done")
print("Total Time taken:{}".format(str(datetime.now()- starttime)))

