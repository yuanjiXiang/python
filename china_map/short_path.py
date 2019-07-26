import re
import matplotlib.pyplot as plt
import random
import math

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
    plt.text(90, 20, '起点：' + begin_city + '\n' +
             '终点：' + end_city+ '\n' + '距离：' + distance)
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
                round(re_distance(cities[i + 1], cities[j + 1]), 2)
            cities_distances2[cities[j][0] + '-' + cities[i][0]] = \
                round(re_distance(cities[i + 1], cities[j + 1]), 2)
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


def special_city_dict(city):
    city_dict = {}
    for key, value in cities_distances1.items():
        if key.find(city) != -1:
            city_dict[key] = value
    return city_dict


def special_city_list(city):
    city_list1 = []
    for key, value in cities_distances1.items():
        if key.find(city) != -1:
            city_list1.append(key)
            city_list1.append(value)
    i = 0
    city_list2 = [[[]] * 2] * 33
    while i < len(city_list1):
        city_list2[int(i / 2)] = [city_list1[i], city_list1[i + 1]]
        i += 2
    return city_list2


def nearest_city_list(city):
    city_list1 = special_city_list(city)
    city_list2 = sorted(city_list1, key=lambda item: item[1])
    return city_list2


def connect_city(city1, city2):
    return city1 + '-' + city2


def nearest_num_city(city, num):
    near_city = nearest_city_list(city)[num - 1][0]
    return near_city.replace(city, '').replace('-', '')


begin_city = cities_name[random.randint(0, 33)]
end_city = nearest_num_city(begin_city, 1)

print('起点城市:' + begin_city)
print('结尾城市:' + end_city)


# print(nearest_city_list(begin_city))
# print(nearest_city_list(nearest_city(begin_city)))


def search_path(begin_city):
    cities = []
    cities.append(begin_city)
    cities.append(nearest_num_city(begin_city, 2))
    cities.append(end_city)
    third_city = nearest_num_city(begin_city, 2)
    j = 0
    while True:
        city = nearest_num_city(third_city, 1)
        cities_list = nearest_city_list(city)
        if city in cities:
            i = 2
            while i < 33:
                city = nearest_num_city(third_city, i)
                if city not in cities:
                    break
                else:
                    i += 1
            cities.insert(j + 2, city)
        else:
            cities.insert(j + 2, city)
        j += 1

        third_city = city

        if len(cities) >= 34:
            break
    return cities


cities = search_path(begin_city)
print(cities)


def calculate_distance(cities):
    distance = 0.0
    for i in range(len(cities) - 1):
        distance += cities_distances[connect_city(cities[i], cities[i + 1])]
    return round(distance, 2)

distance = str(calculate_distance(cities))
print('距离:' + distance)

di = re_dict(fo)


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


draw_path(cities)
