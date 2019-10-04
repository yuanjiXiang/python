import re
import require_root_file

name_pattern = '<i class="nick" title="(\\S+)">(\\S+)</i>'
num_pattern = '<i class="js-num">(\\S+)</i>'

name = re.findall(name_pattern, require_root_file.web_info)
num = re.findall(num_pattern, require_root_file.web_info)


def constitute_list():
    """根据姓名、数量，组成列表"""
    name_num_list = []
    for item in range(len(name)):
        if num[item].find(',') != -1:
            num[item] = num[item].replace(',', '')
        if num[item].find('万') != -1:
            num[item] = num[item].replace('万', '')
            num[item] = float(num[item]) * 10000

        temp = [name[item][0], num[item]]
        name_num_list.append(temp)
    return name_num_list


"排序"
after_sorted = sorted(constitute_list(), key=lambda item: item[1], reverse=True)

"格式化"
for i in range(len(after_sorted)):
    numb = after_sorted[i][1]
    if numb >= 10000:
        numb /= 10000
        after_sorted[i][1] = str(numb) + '万'

for count in range(len(after_sorted)):
    print(str(count + 1) + "::" + after_sorted[count][0] + ":" + after_sorted[count][1])
