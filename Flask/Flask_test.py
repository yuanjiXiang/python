# 1.导入 Flask 扩展
from flask import Flask

# 2.创建Flask 应用程序实例
# 需要传入__name__, 作用是为了确定资源所在的路径
app = Flask(__name__)


# 3.定义路由及视图函数
# Flask 中定义路由是通过装饰器实现的
# 路由默认只支持 GET, 如果需要增加，需要自行指定
@app.route('/', methods=['GET', 'POST'])
def index():
    return 'hello flask'

# 使用同一个视图函数，来显示不同用户的订单信息
# <>定义路由的参数，<>内需要起个名字
@app.route('/orders/<int:order_id>')
def get_order_id(order_id):

    # 参数类型，默认是字符串，unicode

    # 有的时候，需要对路由进行访问优化，订单 ID 应该是 int 类型，则在参数前面加 int:

    # 需要在视图函数的()内填入参数名，后面的代码才能去使用
    return 'order_id %s' % order_id


# 4.启动程序
if __name__ == '__main__':
    # 执行了 app.run 就会将 Flask 程序运行在一个简易的服务器（Flask 提供的，用于测试的）
    app.run()
