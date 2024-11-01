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