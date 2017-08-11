#python小项目——ATM系统（信用卡）


##需求:
	1、实现ATM的基本功能：套现（5%的手续费）、还
	款、余额查询、账单查询、转账。

	2、实现程序的管理功能：支持账户添加、额度设置、
	冻结账户、解冻账户

	3、实现支付接口：支持第三方程序进行支付

	4、支持多用户登陆，用户认证使用装饰器

	5、实现ATM记录日志

##需求分析：
	该项目只是用于自学python巩固python基础知
	识，此处涉及到的知识点有：
	列表；
	字典；
	文件读写；	
	os和sys的部分应用（python环境变量的添加；
	自定义模块导入；
	装饰器；
	json模块的应用；
	time模块的应用。

	分析后将用户信息以json的格式存储至文件中
	使用json模块进行读写


![](http://i.imgur.com/6GnW42I.png)

	C:.
	│  fileTree.txt 目录树信息文件
	│  getFileTree.bat 获取目录树的bat脚本
	│  Readme.md	
	│  
	├─.idea
	│      .name
	│      ATMWork.iml
	│      encodings.xml
	│      misc.xml
	│      modules.xml
	│      README
	│      workspace.xml
	│      
	├─atm
	│  │  __init__.py
	│  │  
	│  ├─bin
	│  │      atm.py	程序入口
	│  │      manage.py	管理工具
	│  │      __init__.py
	│  │      
	│  ├─conf
	│  │      setting.py	配置文件，暂无内容
	│  │      __init__.py
	│  │      
	│  ├─core
	│  │  │  accounts.py	用于读写json文件信息
	│  │  │  auth.py 用户认证装饰器
	│  │  │  logger.py 日志
	│  │  │  main.py	主函数入口
	│  │  │  transaction.py	程序主要功能的所在
	│  │  │  __init__.py
	│  │  │  
	│  │  └─__pycache__ 		pyc格式文件夹
	│  │          accounts.cpython-36.pyc
	│  │          auth.cpython-36.pyc
	│  │          logger.cpython-36.pyc
	│  │          main.cpython-36.pyc
	│  │          transaction.cpython-36.pyc
	│  │          __init__.cpython-36.pyc
	│  │          
	│  ├─db
	│  │  │  account_sample.py 用于生产admin初始账号
	│  │  │  __init__.py
	│  │  │  
	│  │  ├─accounts
	│  │  │      admin.json
	│  │  │      lyw.json
	│  │  │      sh.json
	│  │  │      wh.json
	│  │  │      zsc.json
	│  │  │      
	│  │  └─__pycache__
	│  │          account_sample.cpython-36.pyc
	│  │          __init__.cpython-36.pyc
	│  │          
	│  └─log	用于存储日志
	│          admin_op.log
	│          zsc_transact.log
	│          __init__.py
	│          
	├─picture	用于存放图片
	│      QQ截图20170811102458.png
	│      
	└─shopping_mall
	        __init__.py
        
	

	
	