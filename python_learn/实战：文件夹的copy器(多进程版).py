# -*- coding: utf-8 -*

import os
import multiprocessing


def copy_file(queue, old_folder_name, new_folder_name, file):

    old_f = open(old_folder_name + "/" + file, "rb")
    content = old_f
    old_f.close()

    new_f = open(new_folder_name + "/" + file, "wb")
    new_f.write(content)
    new_f.close()

    queue.put(file)

def main():

    #获取要拷贝的文件夹的名字
    old_folder_name = "G:/program_from_server/pro_2"

    #创建新的文件夹
    try:
        new_folder_name = "E:/program_github/python/python_learn/test/" + "test1"
        os.mkdir(new_folder_name)

    except:
        pass

    #获取要拷贝文件的名字
    file_names = os.listdir(old_folder_name)
    print(file_names)

    #创建进程池
    po = multiprocessing.Pool(3)

    #创建一个队列
    queue = multiprocessing.Manager().Queue()

    #拷贝文件
    for file in file_names:
        po.apply_async(copy_file, args = (queue, old_folder_name, new_folder_name, file))

    po.close()
    # po.join()
    all_file_num = len(file_names)
    copy_complete = 0

    while True:
        file_name = queue.get()
        print(file_name)

        copy_complete += 1

        print("\r当前进度完成:%.2f%%" % (copy_complete*100 / all_file_num), end = " ")

        if copy_complete >= all_file_num:
            break

    print()

if __name__ == '__main__':
    main()