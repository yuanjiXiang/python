import file_manage

src_path = '/Users/xiang/kaggle/data/train'
des_path = '/Users/xiang/kaggle/data/preprocessing_train'

# file_manage.copy_file(src_path, des_path)
print(len(file_manage.read_file_dictionary(src_path)))
# print(file_manage.read_file_dictionary(src_path))
print(len(file_manage.read_file_dictionary(des_path)))
