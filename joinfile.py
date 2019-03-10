import os
from pydub import AudioSegment

print(os.getcwd())
# path = 'C:\\Users\\Sam\\Documents\\python\\playgrond\\'
path ='C:\\Users\\Sam\\Box Sync\\7HabbitsHighlyEffectivePeople\\cd-1\\'
outfilename= 'cd2.mp3'
os.chdir(path)
print(os.getcwd())

directory = os.listdir(path)

# with open(path+outfilename,'w', encoding="utf8") as outfile:
for (i,filename) in enumerate(directory):
    # filename = path + filename
    print(filename)
    exists = os.path.isfile(filename)
    print('File Exists.{}'.format(exists))
    try:
        with open(filename,'r') as readfile:
            # sound = AudioSegment.from_mp3(os.path.join(path, readfile))
            sound = AudioSegment.from_mp3(readfile, )

    except IOError as e:
        print(e)
    
    if i==0:
        continue
    i +=1
        # sound  = sound+i
        # sound.export(path+ outfilename)
        # with open(path+filename,  'r', encoding="utf8") as infile:
        #     outfile.write(infile.read())

    # 
# filenames =['01 Track 1.mp3','02 Track 2.mp3','03 Track 3.mp3']


# with open ('out.mp3'.'w') as outfile:
#     for f in filenames:
#         with open(path +f) as infile:
#             outfile.write(infile.read())

