from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

# # 配置数据库的地址
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://Mysql@127.0.0.1/flask_sql'
#
# # 跟踪数据的修改 --> 不建议开启 未来的版本中会移除
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


'''
两张表
角色（管理员/普通用户）
用户（角色 ID）
'''


# 数据的模型，需要继承 db.Model
class Role(db.Model):
    # 定义表
    __tablename__ = 'roles'

    # 定义字段
    # db.Column表示一个字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)

    # 在一的一方，写关联
    # users = db.relationship('Users'):表示和 Users模型发生了关联，增加了 users属性
    # backref='role':表示role是Users 要用的属性
    users = db.relationship('Users', backref='role')

    # repr()方法显示一个可读字符串
    def __repr__(self):
        return '<Role %s %s>' % (self.name, self.id)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    email = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))
    # db.ForeignKey('roles.id')表示外键，对方的表名.id
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    # User希望有role 属性，但是这个属性的定义，需要在另一个模型中定义

    def __repr__(self):
        return '<User: %s %s %s %s>' % (self.name, self.id, self.email, self.password)


# 删除表
db.drop_all()
#
# # 创建表
db.create_all()

# 创建测试数据
ro1 = Role(name='admin')
db.session.add(ro1)
db.session.commit()
# 再次插入一条数据
ro2 = Role(name='users')
db.session.add(ro2)
db.session.commit()

# 多条用户数据
us1 = Users(name='wang', email='wang@163.com', password='123456', role_id=ro1.id)
us2 = Users(name='zhang', email='zhang@189.com', password='201512', role_id=ro2.id)
us3 = Users(name='chen', email='chen@126.com', password='987654', role_id=ro2.id)
us4 = Users(name='zhou', email='zhou@163.com', password='456789', role_id=ro1.id)
us5 = Users(name='tang', email='tang@itheima.com', password='158104', role_id=ro2.id)
us6 = Users(name='wu', email='wu@gmail.com', password='5623514', role_id=ro2.id)
us7 = Users(name='qian', email='qian@gmail.com', password='1543567', role_id=ro1.id)
us8 = Users(name='liu', email='liu@itheima.com', password='867322', role_id=ro1.id)
us9 = Users(name='li', email='li@163.com', password='4526342', role_id=ro2.id)
us10 = Users(name='sun', email='sun@163.com', password='235523', role_id=ro2.id)
db.session.add_all([us1, us2, us3, us4, us5, us6, us7, us8, us9, us10])
db.session.commit()
@app.route('/')
def index():
    return 'Hello flask'


if __name__ == '__main__':

    app.run(debug=True)
