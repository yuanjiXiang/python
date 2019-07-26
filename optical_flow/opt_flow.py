import numpy as np
import cv2 as cv
import os

"函数传参数依次是，用于计算流的第一张图路径（包括文件名），用于计算流的第二张图路径（包括文件名），\
输出文件夹名，预测图片数量（默认一张），输出图片顺序标志（已设置好，不用传！！！）"


def opt_flow_pic(source_pic1, source_pic2, predict_pic_path, predict_pic_num=1, count=1):
    if predict_pic_num != 0:
        """判断源图片source_pic1, source_pic2，以及预测图片输出路径是否合法"""
        assert os.path.isfile(source_pic1), 'source_pic1路径错误'
        assert os.path.isfile(source_pic2), 'source_pic2路径错误'
        assert os.path.isdir(predict_pic_path), 'predict_pic_path路径错误'

        prev = cv.imread(source_pic1)  # 读取一张图片
        prevgray = cv.cvtColor(prev, cv.COLOR_BGR2GRAY)  # 预处理第一张图片

        pres = cv.imread(source_pic2)  # 读取第二张图片
        presgray = cv.cvtColor(pres, cv.COLOR_BGR2GRAY)  # 预处理第二张图片

        "计算流"
        flow = cv.calcOpticalFlowFarneback(prevgray, presgray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

        cur_glitch = pres.copy()  # 复制第二张图片，用来根据flow预测图片

        cur_glitch = warp_flow(cur_glitch, flow)  # 生成预测图片

        predict_pic = predict_pic_path + '/predict_pic' + str(count) + '.png'  # 存储路径
        cv.imwrite(predict_pic, cur_glitch)  # 写入文件夹

        print('predict_pic' + str(count) + '.png Done')

        '如果需要预测多张图片，把预测出来的图片当作源图片进行处理'
        source_pic1 = source_pic2  # 把原来的第二张图片用作第一张图片
        source_pic2 = predict_pic  # 把预测图片当作第二张图片
        predict_pic_num -= 1  # 预测数量-1
        count += 1  # 输出图片顺序计数
        "递归调用"
        opt_flow_pic(source_pic1, source_pic2, predict_pic_path, predict_pic_num, count)


"根据流生成预测图像，参数1计算流的第二张图像，参数2为计算出的流"


def warp_flow(img, flow):
    h, w = flow.shape[:2]
    flow = -flow
    flow[:, :, 0] += np.arange(w)
    flow[:, :, 1] += np.arange(h)[:, np.newaxis]
    res = cv.remap(img, flow, None, cv.INTER_LINEAR)
    return res


prev_path = '/Users/xiang/PycharmProjects/optical_flow/radar_pics/1.png'
pres_path = '/Users/xiang/PycharmProjects/optical_flow/radar_pics/2.png'
predict_path = '/Users/xiang/PycharmProjects/optical_flow/radar_pics'
opt_flow_pic(prev_path, pres_path, predict_path, predict_pic_num=1)

# prev_path = '/Users/xiang/PycharmProjects/optical_flow/line9_layer2_1th.png'
# pres_path = '/Users/xiang/PycharmProjects/optical_flow/line9_layer2_2th.png'
#
# prev = cv.imread(prev_path)  # 读取一张图片
# prevgray = cv.cvtColor(prev, cv.COLOR_BGR2GRAY)  # 预处理第一张图片
#
# pres = cv.imread(pres_path)  # 读取第二张图片
# presgray = cv.cvtColor(pres, cv.COLOR_BGR2GRAY)  # 预处理第二张图片
#
# "计算流"
# flow = cv.calcOpticalFlowFarneback(prevgray, presgray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
#
# cur_glitch = pres.copy()  # 复制第二张图片，用来预测
# cur_glitch = warp_flow(cur_glitch, flow)  # 生成预测图片
# cv.imwrite('/Users/xiang/desktop/predict_pic2.png', cur_glitch)  # 写入文件夹
#
# print('Done')
#
