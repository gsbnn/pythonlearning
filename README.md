# python学习  

1. 学习git的用法，特别是远程仓库跟踪以及本地工作流。  
2. 学习python基础语法，并完成一个项目。
3. 以下将记录使用git中所碰到的问题及解决方案。 
4. 学习`matplotlib`可以参考[快速指南](https://matplotlib.org/stable/users/explain/quick_start.html)，一个`Figure`所包含的属性参考![绘图属性](https://matplotlib.org/stable/_images/anatomy.png) 
5. 了解python虚拟环境相关信息参考[链接](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)  
6. 了解`Pygal`可以参考[指南](https://www.pygal.org/en/stable/documentation/index.html)
7. 了解`Request`可以参考[快速指南](https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls)  
8. HTTP命令格式  
    - 请求命令格式  
    > 1.请求首行：请求方法 + URL + HTTP协议版本  
    > 2.请求头：请求报文的属性，冒号分隔的键值对，每组属性各占一行  
    > 3.空行  
    > 4.请求体：如果请求体存在，请求头中会有一个 Content-Length 属性来表示请求体的长度  

    以下是一个例子![HTTP请求命令格式](https://i-blog.csdnimg.cn/blog_migrate/d86a0e70b9768d620ce0f1cd015d468a.png)  

    - 响应命令格式  
    > 1.响应首行：HTTP 协议版本 + 响应状态码 + 状态码解释短句  
    > 2.响应头：响应报文的属性，冒号分隔的键值对，每组属性各占一行  
    > 3.空行  
    > 4.响应体：如果响应体存在，响应头中就会有一个 Content-Length 属性来表示响应体长度，如果服务器返回一个 html 页面，那么 html 页面内容就出现在响应体中  

    以下是一个例子![HTTP响应命令格式](https://i-blog.csdnimg.cn/blog_migrate/853c6d2ef7d905e0589f5f711a960be6.png)  
    
9. 了解HTTP常见请求可以参考以下链接：  
    > https://developer.aliyun.com/article/1476820  
    > https://blog.csdn.net/lsoxvxe/article/details/132147475  
10. 学习`Pygame`可以参考[快速指南](https://www.pygame.org/docs/)  

11. 关于类的基本内容  
类包含两个基本内容：方法和属性。  
方法包括3类：instance_method（实例方法）, class_method（类方法）, static_method（静态方法）。  
属性包括2类：类属性和实例属性 。 

12. 类本身是否可以调用自己的方法？  
答：可以，类本身可以调用class_method（默认第一个传入参数为类本身，而不是类的实例）和static_method（只是定义在类中的一个函数），而instance_method必须先创建类的实例才可调用，`__init__(self, ...)`是一个特殊的instance_method，用来创建一个实例，包括实例及实例属性等。  

13. instance_method和类的实例及实例属性的关系是什么？  
类的实例和实例属性依赖于instance_method而存在，如果instance_method中没有定义某个实例属性，则类的实例也就没有这个实例属性。  

14. 关于class_method的具体应用参照[链接](https://geek-docs.com/python/python-ask-answer/211_hk_1710454843.html#google_vignette)

15. 对Python中`继承`的理解  
    - 对于`class Son(Father):`而言Son到底继承了Father的什么？  
    答：继承的是`所有方法`和`类属性`,如果Son中没有重写Father的方法，那么Son将继承Father的方法；反之，使用Son自己的方法，丢弃Father的同名方法。  
    - 那么属性是如何被继承的？  
    答：实例属性一般定义在`__init__(self, ...)`方法中，因此如果Son没有重写`__init__(self, ...)`方法，则Father的实例属性也将被继承；反之，Father的实例属性将全部丢弃。  
    - 如果在Son中重写了方法，如何再次调用父类方法？  
    答：使用`super()`函数,例如在Son类的`__init__(self, ...)`方法中写入`super().__init__(self, ...)`,可调用Father方法，重新继承Father的实例属性。