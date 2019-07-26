from flask import Flask, render_template

app = Flask(__name__)

# 1.如何返回一个网页（模板）
# 2.如何给模板填充数据
@app.route('/')
def index():

    # 比如需要传入网址

    url_str = 'www.baidu.com'

    my_list = [1, 2, 3]

    my_dict = {
        'url': 'abc.com',
        'name': 'abc'
    }

    your_int = 12

    # 通常，模板中使用的变量名和要传递的数据名保持一致
    return render_template('index.html',
                           url_str=url_str,
                           my_list=my_list,
                           my_dict=my_dict,
                           your_int=your_int)


if __name__ == '__main__':
    app.run()
