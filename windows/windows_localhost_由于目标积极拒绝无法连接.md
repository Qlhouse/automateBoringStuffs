# 问题背景

在尝试python socket编程的时候，首先将编写好的客户端给和服务器都部署在本地运行，并且使用同一台宿主机，客户端使用127.0.0.1，服务器端使用0.0.0.0或者127.0.0.1。    

刚开始

刚开始我端口时随意选择的，比如8080，9090， 然后一直出现报错：**由于目标积极拒绝，无法连接**。

`ping 127.0.0.1`也没有问题，这个时候，**telnet你选择的端口**，看看端口是不是开启的。

![](https://img-blog.csdnimg.cn/20200517093415513.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ0NjU0NDk4,size_16,color_FFFFFF,t_70 "telnet选择的端口")



要查看系统开放的端口，使用`netstat -an`命令。
```
活动连接

  协议  本地地址          外部地址        状态
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING
  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING
  TCP    0.0.0.0:1688           0.0.0.0:0              LISTENING
  TCP    0.0.0.0:5040           0.0.0.0:0              LISTENING
  TCP    0.0.0.0:7680           0.0.0.0:0              LISTENING
  TCP    0.0.0.0:49664          0.0.0.0:0              LISTENING
  TCP    0.0.0.0:49665          0.0.0.0:0              LISTENING
  TCP    0.0.0.0:49666          0.0.0.0:0              LISTENING
  TCP    0.0.0.0:49667          0.0.0.0:0              LISTENING
  TCP    0.0.0.0:49668          0.0.0.0:0              LISTENING
  TCP    0.0.0.0:49724          0.0.0.0:0              LISTENING
  TCP    127.0.0.1:10000        0.0.0.0:0              LISTENING
  TCP    127.0.0.1:28317        0.0.0.0:0              LISTENING
  TCP    127.0.0.1:35500        0.0.0.0:0              LISTENING
  TCP    127.0.0.1:35600        0.0.0.0:0              LISTENING
  TCP    127.0.0.1:35600        127.0.0.1:49684        ESTABLISHED
  TCP    127.0.0.1:49684        127.0.0.1:35600        ESTABLISHED
  TCP    127.0.0.1:49747        0.0.0.0:0              LISTENING
  TCP    127.0.0.1:56529        127.0.0.1:35600        TIME_WAIT
  TCP    127.0.0.1:61391        127.0.0.1:49853        SYN_SENT
  TCP    127.0.0.1:61392        127.0.0.1:49853        SYN_SENT
  TCP    127.0.0.1:61393        127.0.0.1:49853        SYN_SENT
  TCP    127.0.0.1:61394        127.0.0.1:49853        SYN_SENT
  TCP    127.0.0.1:61395        127.0.0.1:49853        SYN_SENT
  TCP    127.0.0.1:61397        127.0.0.1:49853        SYN_SENT
  TCP    192.168.1.3:139        0.0.0.0:0              LISTENING
  TCP    192.168.1.3:52614      40.90.189.152:443      ESTABLISHED
  TCP    192.168.1.3:58298      64.233.188.188:443     ESTABLISHED
  TCP    192.168.1.3:58350      106.75.129.46:443      ESTABLISHED
  TCP    192.168.1.3:58543      185.199.111.154:443    ESTABLISHED
  TCP    192.168.1.3:58562      151.101.76.133:443     ESTABLISHED
  TCP    192.168.1.3:58597      151.101.76.133:443     ESTABLISHED
  TCP    192.168.1.3:59747      185.199.111.154:443    ESTABLISHED
  TCP    192.168.1.3:60176      140.82.114.25:443      ESTABLISHED
  TCP    192.168.1.3:60409      202.89.233.101:443     ESTABLISHED
  TCP    192.168.1.3:60441      36.156.131.41:443      ESTABLISHED
  TCP    192.168.1.3:60466      111.3.78.177:443       TIME_WAIT
  TCP    192.168.1.3:60467      111.3.78.177:443       ESTABLISHED
  TCP    192.168.1.3:60468      183.214.166.20:443     TIME_WAIT
  TCP    192.168.1.3:60471      120.253.255.169:443    ESTABLISHED
  TCP    192.168.1.3:60486      120.253.255.166:443    ESTABLISHED
  TCP    192.168.1.3:60491      211.157.2.94:443       ESTABLISHED
  TCP    192.168.1.3:60499      111.48.29.243:443      TIME_WAIT
  TCP    192.168.1.3:60504      151.101.76.133:443     ESTABLISHED
  TCP    192.168.1.3:60817      23.2.16.105:443        ESTABLISHED
  TCP    192.168.1.3:60941      120.253.255.34:443     ESTABLISHED
  TCP    192.168.1.3:60944      111.48.29.244:443      ESTABLISHED
  TCP    192.168.1.3:60945      112.29.219.35:443      TIME_WAIT
  TCP    192.168.1.3:60960      111.48.50.35:443       ESTABLISHED
  TCP    192.168.1.3:60971      103.72.47.242:443      ESTABLISHED
  TCP    192.168.1.3:60975      111.48.50.35:443       ESTABLISHED
  TCP    192.168.1.3:61024      111.48.85.28:443       ESTABLISHED
  TCP    192.168.1.3:61025      111.48.50.41:443       ESTABLISHED
  TCP    192.168.1.3:61033      111.48.50.41:443       ESTABLISHED
  TCP    192.168.1.3:61037      111.48.177.239:443     ESTABLISHED
  TCP    192.168.1.3:61041      103.41.167.234:443     ESTABLISHED
  TCP    192.168.1.3:61042      36.152.44.96:443       ESTABLISHED
  TCP    192.168.1.3:61059      111.48.89.13:443       ESTABLISHED
  ```
  
那些处于listening状态的端口都是可以使用的。

