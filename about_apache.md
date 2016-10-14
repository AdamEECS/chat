# gunicorn、supervisor、apache联合使用

## gunicorn
>（略）

## supervisor
[安装及初始配置通用教程](http://www.restran.net/2015/10/04/supervisord-tutorial/)

>主要参照这篇文章，这里只保留了一个program的样例。

一个进程的配置样例：
```
[program:web]
directory = /home/file/webroot ; 程序的启动目录
command = gunicorn wsgi:app -b 0.0.0.0:3002  ; 启动命令，与手动在命令行启动的命令是一样的
autostart = true     ; 在 supervisord 启动的时候也自动启动
startsecs = 5        ; 启动 5 秒后没有异常退出，就当作已经正常启动了
autorestart = true   ; 程序异常退出后自动重启
startretries = 3     ; 启动失败自动重试次数，默认是 3
user = root          ; 用哪个用户启动
redirect_stderr = true  ; 把 stderr 重定向到 stdout，默认 false
stdout_logfile_maxbytes = 20MB  ; stdout 日志文件大小，默认 50MB
stdout_logfile_backups = 20     ; stdout 日志文件备份数
; stdout 日志文件，需要注意当指定目录不存在时无法正常启动，所以需要手动创建目录（supervisord 会自动创建日志文件）
stdout_logfile = /home/data/logs/web_stdout.log
```
## apache
这里的需求是做反向代理，所以和web1的配置稍有不同。
>web1的配置可以实现直接以apache启动wsgi；

此处的情况是，已经用gunicorn启动了wsgi并运行在不同的端口上，
需要把不同域名通过apache的80端口，映射到gunicorn运行的各个端口。
#### 1，apache安装
同web1配置。

#### 2，依赖模块加载
```
ln -s /etc/apache2/mods-available/proxy.load /etc/apache2/mods-enabled/proxy.load
ln -s /etc/apache2/mods-available/proxy_http.load /etc/apache2/mods-enabled/proxy_http.load
ln -s /etc/apache2/mods-available/proxy_balancer.load /etc/apache2/mods-enabled/proxy_banancer.load
ln -s /etc/apache2/mods-available/slotmem_shm.load /etc/apache2/mods-enabled/slotmem_shm.load
```
#### 3，反向代理配置
配置文件为/etc/apache2/sites-available/proxy.conf
```
<VirtualHost *:80>
    ServerAdmin webmaster@dummy-host.example.com
    ServerName chat.suzumiya.cc
    ProxyRequests Off
    <Proxy *>
        Order deny,allow
        Allow from all
    </Proxy>
    ProxyPass / http://127.0.0.1:3001/
    ProxyPassReverse / http://127.0.0.1:3001/
</VirtualHost>
```
>其中ServerName为子域名，ProxyPass和ProxyPassReverse为相应的gunicorn所在的端口

并将其加载到enabled中
```
ln -s /etc/apache2/sites-available/proxy.conf /etc/apache2/sites-enabled/proxy.conf
```
生效还需重启apache
```
service apache2 restart
```
