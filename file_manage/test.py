import file_manage

src_path = '/Users/xiang/Downloads/predictPics4'
file_manage.change_file_suffix(file_manage.read_file_dictionary(src_path), '.bmp', '.png')
print('done')