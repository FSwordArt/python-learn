import os

path = 'F:/J-Learn/Mask_RCNN-master/datasets/set/annotations/'  # path为json文件存放的路径
json_file = os.listdir(path)
os.system("activate labelme")
for file in json_file: 
    os.system("labelme_json_to_dataset.exe %s"%(path + '/' + file))
