# 秒表自动计时

import time

print('按回车开始计时，按ctrl + c结束计时')
while True:
    try:
        input()
        start_time = time.time()   
        print('开始')
        while True:
            print('计时', round(time.time() - start_time, 0), '秒', end = '\n')
            time.sleep(1)
    except KeyboardInterrupt:
        print('结束')
        break
