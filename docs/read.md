登录封装思路
1,创建基类：
    1.1封装基类的方法，request_send ， 请求方法可以直接返回响应体，return resp.json()。方便子类使用
        1.1.1将不变的参数，配置到配置文件.py: （例如ip,）。
        1.1.2将接口的每个模块的path,url，配置在yml文件:（类名：函数名：path,url）
        1.1.3在基类的__init__方法，通过utils层封装的方法读取数据，获得当前类名，以类名为键，获取各自对应的数据self.data = get_yml_data('../configs/apiConfig.yml')[self.__class__.__name__]，
        1.1.4在获得类对应的数据上，取每个类下的每个方法对应的配置参数：methodName = inspect.stack()[1][3]  （## 如果是restful风格的接口，，host和url可能一样，就直接从类里获取就不行，不需要inspect.stack()[1][3]在获得函数名了）
        1.1.5通过method = self.data[methodName]['method'] 方式获得method，url等数据，传入request
    1.2 封装断言：
        创建一个断言的类，
        创建一个方法，可以是类方法， 在测试用例直接用类名取调用
2，创建业务类：
    2.1封装登录的 类：继承基类
        2.1.1 登录方法:
            调用基类的请求方法，传入账号密码，
            功能：
                1，登录
                2，返回token:  传入一个默认的值，true返回token，false返回响应体，
            调试：是否能调用成功
        2.1.2 退出方法
    2.2 店铺封装思路：
    店铺类：
        继承基类 --基类封装增删改查方法
        需要获取token --- 调用登录实例后返回的token
        准备测试数据，店铺实例调用基类方法（请求店铺列表），获得店铺的id
        需要上传文件：
            基类封装上传文件的方法
        调用创传文件的方法后，获得返回值 文件的 realfilename值
        更新方法：
            需要传入三个值，测试用例，shopid,图片信息
            将用例中的shopid更新为参数的shopid，
            将图片信息传入更新文件的的参数中，
            调动父类的更新方法，
    日志操作：
        直接复制loguru.py文件，写好的日志处理，
        配置文件需要 loguru.ini配置


3, 测试文件层： （对应的业务层代码封装完成）（自动化用例完成）
    3.1 登录测试用例：
        3.1.1：准备测试用例
        3.1.2：读取excel中的数据
            思路：excel地址、sheet页(登录、商品、购物等)，测试用例名称(模块下的哪部分用例，登录下的退出用例、商品下的购物用例)、
            测试用例的字段（要用例的哪几个字段，路径、参数、预期结果等）、
            筛选的测试用例字段（只跑某一个或一段）
        可以将所有的参数配置到配置文件--yml读取， 

4,测试用例层:
    登录：调用登录业务层，调用excel数据进行参数化，
            添加allure报告
    商品：
    fixtrue:
        conftest.py文件，
        可以创建登录的fixtrue，先将登录后获得token，将token返回 
        然后在创建商品类的fixtrue，将登录的fixtrue的函数当做返回值传入商品的fixtrue
        在商品用例中每个用例调用 商品的fixtrue就行可以获得的token
        
5，run.sh  /  run.bat 运行
    cd ./test_cases
    pytest -s --alluredir ../outfiles/report --clean-alluredir
    allure serve ../outfiles/report

6，定制用例：
    pytest.mark.xxx  定制
        需要在项目根目录下新建pytest.ini文件
        固定写法：
            [pytest]
            markers = 
            xxx:描述
        在运行时加入参数 '-m'，'xxx'
    pytest.mark.skip(reason=原因) 无条件跳过 ， pytest.mark.skipif(布尔表达式，reason=原因)条件跳过
        直接在用例方法上使用
        可以写成一个变量，在需要的方法调用

编码：
encoding ---属性
encode() --- 编码函数

解码：
decode() --- 解码

装饰器：
在不改变原函数代码的基础上，新增功能
    闭包：
        内函数调用外函数的变量，就是闭包