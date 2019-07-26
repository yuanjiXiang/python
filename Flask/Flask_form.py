from flask import Flask, render_template, request, flash


app = Flask(__name__)

app.secret_key = 'abc'

'''
目的：实现一个简单的登录的逻辑处理
1. 路由需要 get 和 post 两种请求方式 --> 需要判断请求方式
2. 判断请求的参数
3. 判断参数是否填写&密码是否相同
4. 如果判断都没问题，返回一个 success
'''

'''
给模板传递消息
flash --> 需要对内容加密，因此需要设置 secret_key,做加密消息的混淆
模板中需要便利消息
'''


@app.route('/', methods=['GET', 'POST'])
def index():
    # request:请求对象 --> 获取请求方式、数据

    # 1.判断请求方式
    if request.method == 'POST':

        # 2. 获取请求参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        # 3.判断参数是否填写&密码是否相同
        if not all([username, password, password2]):
            # print('参数不完整')
            flash('参数不完整')
        elif password2 != password:
            # print('密码不一致')
            flash('密码不一致')
        else:
            return 'success'

    return render_template('form.html')


if __name__ == '__main__':
    app.run()
