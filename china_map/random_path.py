import re
import matplotlib.pyplot as plt
import math
import numpy as np
import time

p_time1 = time.process_time()

pattern_num = '\d+\\.*\d+'
pattern_ch = '[\u4e00-\u9fa5]+'

fo = open('/Users/xiang/PycharmProjects/china_map/china_cities.txt')


def re_dict(file):
    city_dict = {}
    for line in file.readlines():
        line = line.strip().replace(' ', '')
        city_dict[re.findall(pattern_ch, line)[0]] = re.findall(pattern_num, line)
    file.seek(0)
    return city_dict


def draw_pic(file, x, y):
    draw_city_dict = re_dict(file)

    plt.rcParams['font.family'] = ['Arial Unicode MS']  # 用来正常显示中文标签

    for key, value in draw_city_dict.items():
        # plt.scatter(float(value[0]), float(value[1]), color='b')
        plt.annotate(key, (float(value[0]), float(value[1])))
    plt.plot(x, y, '->')
    plt.text(90, 25, '起点：' + begin_city + '\n' +
             '终点：' + end_city + '\n' + '距离:' + distance)
    plt.show()


def re_list(file):
    city_list = []
    for line in file.readlines():
        line = line.strip().replace(' ', '')
        city_list.append(re.findall(pattern_ch, line))
        city_list.append(re.findall(pattern_num, line))
    file.seek(0)
    return city_list


def re_distance(location1, location2):
    return math.sqrt((float(location1[0]) - float(location2[0])) ** 2 + \
                     (float(location1[1]) - float(location2[1])) ** 2)


def re_cities_distances():
    cities_distances1 = {}
    cities_distances2 = {}
    cities = re_list(fo)
    i = 0
    while i < len(cities) - 3:
        j = i + 2
        while j < len(cities) - 1:
            cities_distances1[cities[i][0] + '-' + cities[j][0]] = \
                re_distance(cities[i + 1], cities[j + 1])
            cities_distances2[cities[j][0] + '-' + cities[i][0]] = \
                re_distance(cities[i + 1], cities[j + 1])
            j += 2
        i += 2
    return cities_distances1, cities_distances2


cities_distances1, cities_distances2 = re_cities_distances()
cities_distances = dict(cities_distances1, **cities_distances2)


def re_cities_name():
    cities = re_list(fo)
    cities_name = []
    for city_num in range(len(cities)):
        if city_num % 2 == 0:
            cities_name.append(cities[city_num][0])
    return cities_name


cities_name = re_cities_name()


def calculate(epochs):
    epoch = 0
    info = []
    while epoch < epochs:
        total_distance = 0.0
        cities_list = []
        random_list = np.random.permutation(34)
        for num in range(len(random_list) - 1):
            cities_list.append(cities_name[random_list[num]])

            two_cities = cities_name[random_list[num]] + '-' + \
                         cities_name[random_list[num + 1]]

            total_distance += round(cities_distances[two_cities] / 2, 2)

        total_distance += round(cities_distances[cities_name[random_list[0]] \
                                                 + '-' + cities_name[random_list[33]]], 2)
        cities_list.append(cities_name[len(random_list) - 1])

        info.append(total_distance)
        info.append(cities_list)
        epoch += 1
    return info


def sort_data(epochs):
    calculate_result = calculate(epochs)
    i = 0
    transform1 = []
    while i < len(calculate_result):
        temp = [round(calculate_result[i], 2), calculate_result[i + 1]]
        transform1.append(temp)
        i += 2

    transform2 = sorted(transform1, key=lambda line: line[0])

    return transform2


test1 = sort_data(4000)

# for t1 in test1:
#     print(t1)
# print('------')
print(test1[0])

print('------')
di = re_dict(fo)
test1_name_list = test1[0][1]

begin_city = test1_name_list[0]
end_city = test1_name_list[33]
distance = str(test1[0][0])

def draw_path(test_name_list):
    test1_cor_list = []
    for name in test_name_list:
        test1_cor_list.append(di[name])
    x = []
    y = []
    for cor in test1_cor_list:
        x.append(float(cor[0]))
        y.append(float(cor[1]))
    x.append(x[0])
    y.append(y[0])
    draw_pic(fo, x, y)

p_time2 = time.process_time()

draw_path(test1_name_list)
print('Running time: %s Seconds' % round((p_time2 - p_time1), 3))
