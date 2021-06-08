# 根据PID杀死进程

1. 查看进程PID

   ​    `netstat -ano | findstr "端口号"`

       ```powershell
   C:\Users\John>netstat -ano | findstr 6942
     TCP    127.0.0.1:6942       0.0.0.0:0        LISTENING     7636
       ```

   

2. `tskill PID`

       ```powershell
   C:\Users\John>tskill 7636
       ```



