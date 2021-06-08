1. 在文件导航处输入`%AppData%`，回车，即进入目录`C:\Users\John\AppData\Roaming\pip`
2. 在该目录新建文件`pip`，并进入`pip`文件夹
3. 在`pip`目录新建文件`pip.ini`，在文件中输入以下内容，然后存档保存：

```ini
[global]
timeout = 6000
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
```

> 常见国内镜像源
>
> （1）阿里云 http://mirrors.aliyun.com/pypi/simple/
> （2）豆瓣http://pypi.douban.com/simple/
> （3）清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
> （4）中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
> （5）华中科技大学http://pypi.hustunique.com/