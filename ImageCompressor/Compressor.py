#coding: utf-8
from PIL import Image
import os
import sys
from .Processor import Graphics

class Compressor:
    # 定义压缩比，数值越大，压缩越小
    __SIZE_normal = 1.0
    __SIZE_small = 1.5
    __SIZE_more_small = 2.0
    __SIZE_more_small_small = 3.0

    def __init__(self):
        pass

    def __del_dir_tree(self, path):
        ''' 递归删除目录及其子目录,　子文件'''
        if os.path.isfile(path):
            try:
                os.remove(path)
            except Exception as e:
                #pass
                print(e)
        elif os.path.isdir(path):
            for item in os.listdir(path):
                itempath = os.path.join(path, item)
                self.__del_dir_tree(itempath)
                try:
                    os.rmdir(path) # 删除空目录
                except Exception as e:
                    #pass
                    print(e)

    def __make_directory(self, directory):
        """创建目录"""
        os.makedirs(directory)

    def __directory_exists(self, directory):
        """判断目录是否存在"""
        if os.path.exists(directory):
            return True
        else:
            return False

    def __list_img_file(self, directory):
        """列出目录下所有文件，并筛选出图片文件列表返回"""
        old_list = os.listdir(directory)
        # print old_list
        new_list = []
        for filename in old_list:
            if not str(filename).endswith('.txt'):
                try:
                    name,fileformat = filename.split(".")
                    if fileformat.lower() == "jpg" or fileformat.lower() == "png" or fileformat.lower() == "gif":
                        new_list.append(filename)
                except:
                    print("文件名格式错误 " + filename)
        #print new_list
        return new_list


    def __help(self):
        print("""图片压缩，现只支持jpg、png、gif
        
        Arguments:
            src_dir {string} -- 源图片目录
            des_dir {string} -- 压缩后的图片输出目录
        
        Keyword Arguments:
            mode {int:1,2,3,4} -- 压缩比，取值有1、2、3、4，值越大，生成的图片越小 (default: {4})
        """)

    def __compress(self, choose, des_dir, src_dir, file_list):
        """压缩算法，img.thumbnail对图片进行压缩，
        参数
        -----------
        choose: str
                选择压缩的比例，有4个选项，越大压缩后的图片越小
        """
        if choose == '1':
            scale = self.__SIZE_normal
        elif choose == '2':
            scale = self.__SIZE_small
        elif choose == '3':
            scale = self.__SIZE_more_small
        elif choose == '4':
            scale = self.__SIZE_more_small_small
        else:
            scale = self.__SIZE_more_small_small

        for infile in file_list:
            img = Image.open(src_dir+infile)
            # size_of_file = os.path.getsize(infile)
            w, h = img.size
            img.thumbnail((int(w/scale), int(h/scale)))
            img.save(des_dir + infile)

    def compress(self, src_dir, des_dir, mode=4):
        """图片压缩，现只支持jpg、png、gif
        
        Arguments:
            src_dir {string} -- 源图片目录
            des_dir {string} -- 压缩后的图片输出目录
        
        Keyword Arguments:
            mode {int:1,2,3,4} -- 压缩比，取值有1、2、3、4，值越大，生成的图片越小 (default: {4})
        """

        try:
            file_list_src = []
            if self.__directory_exists(src_dir):
                if not self.__directory_exists(des_dir):
                    self.__make_directory(des_dir)
                else:
                    self.__del_dir_tree(des_dir)
                    #self.__make_directory(des_dir)
                # business logic
                file_list_src = self.__list_img_file(src_dir)
            else:
                print("找不到源图片目录")
                return
            if self.__directory_exists(des_dir):
                if not self.__directory_exists(des_dir):
                    self.__make_directory(des_dir)
                file_list_des = self.__list_img_file(des_dir)
                # print file_list
            '''如果已经压缩了，就不再压缩'''
            for i in range(len(file_list_des)):
                if file_list_des[i] in file_list_src:
                    file_list_src.remove(file_list_des[i])
            self.__compress(mode, des_dir, src_dir, file_list_src)
        except Exception as e:
            self.__help()