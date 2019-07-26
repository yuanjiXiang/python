from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


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

'''
使用 WTF 实现表单
自定义表单类
'''


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    password2 = PasswordField('确认密码', validators=[DataRequired(), EqualTo(password)])
    submit = SubmitField('提交')


@app.route('/', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    # 1.判断请求方式
    if request.method == 'POST':

        # 2. 获取请求参数
        # username = request.form.get('username')
        # password = request.form.get('password')
        # password2 = request.form.get('password2')

        # 3. 验证参数，WTF可以一句话实现所有的校验
        if login_form.validate_on_submit():
            return 'success'
        else:
            flash('wrong')
    return render_template('wtf_test.html', local_form=login_form)


if __name__ == '__main__':
    app.run()
