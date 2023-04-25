
import os
import cv2

def get_content_list(path):
    return os.listdir(path)

#save the videos in the path in folder
pathIn="/Users/janu/Documents/UCM/Spring_2023/NeuralNetworks/project/Videos"
pathOut = "/Users/janu/Documents/UCM/Spring_2023/NeuralNetworks/project/Frames"

file_list = get_content_list(pathIn)
file_list.sort(reverse=True)

f = open("Youtube_VideoIds1.txt", "w")
for file in file_list:
    count = 0
    file_mod = file[:-4]
    efile = os.path.join(pathOut, file_mod)
    print(efile)
    if os.path.exists(efile):
        print(f"{file} already converted to frames")
    else:
        pathfile = os.path.join(pathIn, file)
        vidcap = cv2.VideoCapture(pathfile)
        success,image = vidcap.read()
        success = True
        f.write(file_mod)
        f.write("\n")
        if not os.path.exists(f"{pathOut}/{file_mod}"):
            os.mkdir(f"{pathOut}/{file_mod}")
        framepath = os.path.join(pathOut,file_mod)    
        while success:
            vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))
            success,image = vidcap.read()
            try:
                cv2.imwrite(framepath + "/frame%d.jpg" % count, image)
                count = count + 1
            except:
                continue

