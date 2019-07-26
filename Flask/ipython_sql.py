"""
In [1]: from Flask_SQL import *                                                                     

In [2]: role = Role()                                                                               

添加

In [3]: role.name = 'admin'                                                                         

In [4]: db.session.add(role)                                                                        

In [5]: db.session.commit()                                                                         

In [8]: user = Users(name = 'baima', role_id = role.id)                                             

In [9]: db.session.add(user)                                                                        

In [10]: db.session.commit()

修改

In [11]: user.name = 'chengxuyuan'                                   

In [12]: db.session.commit()

删除

In [13]: db.session.delete(user)                                     

In [14]: db.session.commit() 
"""

"""
添加一个角色，两个用户

In [3]: from Flask_SQL import *                                      

In [4]: role = Role()                                                

In [5]: role.name='admin'                                            

In [6]: db.session.add(role)                                         

In [7]: db.session.commit()                                          

In [9]: user1 = Users(name='zs', role_id=role.id)                    

In [10]: user2 = Users(name='ls', role_id=role.id)                   

In [12]:  db.session.add_all([user1, user2])                         

In [13]: db.session.commit() 

实现关系引用查询                                        

In [14]: role.users                                                  
Out[14]: [<User: zs 1 None None>, <User: ls 2 None None>]

In [15]: user1.role                                                  
Out[15]: <Role admin 1>

In [16]: user2.role                                                  
Out[16]: <Role admin 1>

In [17]: user2.role.name                                             
Out[17]: 'admin'

"""

"""

In [2]: from Flask_SQL import *                                                                        

In [3]: Users.query.all()                                                                              
Out[3]: 
[<User: wang 1 wang@163.com 123456>,
 <User: zhang 2 zhang@189.com 201512>,
 <User: chen 3 chen@126.com 987654>,
 <User: zhou 4 zhou@163.com 456789>,
 <User: tang 5 tang@itheima.com 158104>,
 <User: wu 6 wu@gmail.com 5623514>,
 <User: qian 7 qian@gmail.com 1543567>,
 <User: liu 8 liu@itheima.com 867322>,
 <User: li 9 li@163.com 4526342>,
 <User: sun 10 sun@163.com 235523>]

In [4]: Users.query.count                                                                              
Out[4]: <bound method Query.count of <flask_sqlalchemy.BaseQuery object at 0x106193860>>

In [5]: Users.query.count()                                                                            
Out[5]: 10

In [6]: Users.query.first()                                                                            
Out[6]: <User: wang 1 wang@163.com 123456>

In [7]: Users.query.get(4)                                                                             
Out[7]: <User: zhou 4 zhou@163.com 456789>

In [8]: Users.query.filter_by(id=4).first()                                                            
Out[8]: <User: zhou 4 zhou@163.com 456789>

In [9]: Users.query.filter(Users.id==4).first()                                                        
Out[9]: <User: zhou 4 zhou@163.com 456789>

filter_by:属性=
filter:对象，属性==
filter功能更强大，可以实现更多的一些查询，支持比较运算符
"""