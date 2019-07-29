from pathlib import Path
import os, shutil, sys

included_files = []


def read_file_dictionary(file_path):
    """读取 file_path 下所有最底层文件的文件路径"""
    if not os.path.exists(file_path):
        print(file_path + ' is wrong')
        return False
    else:
        files_name = os.listdir(file_path)
        for file in files_name:
            if file.find('.DS_Store') == -1:
                file = file_path + '/' + file
                if os.path.isfile(file):
                    included_files.append(file)
                elif os.path.isdir(file):
                    read_file_dictionary(file)
        return included_files


def judge_file_exit(src_path, des_path):
    """判断源路径和目的路径是否存在"""
    if not os.path.exists(src_path):
        print(src_path + ' is wrong')
        return False
    else:
        if not os.path.exists(des_path):  # 目的路径不存在则创建
            os.makedirs(des_path)
        return True


def move_files(src_path, des_path):
    """移动文件"""
    src_path_list = read_file_dictionary(src_path)
    for file_name in src_path_list:
        if judge_file_exit(file_name, des_path):
            shutil.move(file_name, des_path)


def copy_file(src_path, des_path):
    """复制文件"""
    src_path_list = read_file_dictionary(src_path)
    for file_name in src_path_list:
        if judge_file_exit(file_name, des_path):
            shutil.copy(file_name, des_path)


def change_file_suffix(src_path_list, old_suffix, new_suffix):
    """修改文件后缀名"""
    for file_name in src_path_list:
        if file_name.find(old_suffix) != -1:
            new_file_name = file_name.replace(old_suffix, new_suffix)
            os.rename(file_name, new_file_name)

# src_path, des_path = sys.argv[1], sys.argv[2]
