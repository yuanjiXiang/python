import require_root_file
import re
pattern = '<a href="(\\S+)" '

room_url_li = re.findall(pattern, require_root_file.web_info)
length = len(room_url_li)
for i in range(int(length / 2)):
    room_url_li.pop(i)
room_url_li.pop(0)
room_url_li.pop(len(room_url_li) - 1)
room_url_li.pop(len(room_url_li) - 2)
print(len(room_url_li))






