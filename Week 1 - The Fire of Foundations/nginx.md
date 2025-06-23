# Install nginx and curl localhost

### 1 : Install nginx 

```bash
  sudo apt install nginx 
```
```shell

hariprasad@LAPTOP-IV2TBVVU:~$ sudo apt install nginx
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
nginx is already the newest version (1.18.0-6ubuntu14.6).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```
### 2 : Start nginx service 

If ``systemd`` is enabled:
```bash
  sudo systemctl start nginx
```

If ``systemd`` is not enabled:
```bash
  sudo service nginx start
```

### 3 : nginx service status

```bash
  sudo systemctl status nginx
```

```shell
hariprasad@LAPTOP-IV2TBVVU:~$ sudo systemctl status nginx
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Tue 2025-06-24 00:32:38 IST; 10s ago
       Docs: man:nginx(8)
    Process: 108417 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
    Process: 108418 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
   Main PID: 108419 (nginx)
      Tasks: 5 (limit: 4561)
     Memory: 4.7M
     CGroup: /system.slice/nginx.service
             ├─108419 "nginx: master process /usr/sbin/nginx -g daemon on; master_process on;"
             ├─108420 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""
             ├─108421 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""
             ├─108422 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""
             └─108423 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""

Jun 24 00:32:38 LAPTOP-IV2TBVVU systemd[1]: Starting A high performance web server and a reverse proxy server...
Jun 24 00:32:38 LAPTOP-IV2TBVVU systemd[1]: Started A high performance web server and a reverse proxy server.
```
### 4 : curl localhost

To verify that NGINX is running and serving content correctly, we use the `curl` command:

```html
hariprasad@LAPTOP-IV2TBVVU:~$ curl localhost
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

### 5 : Stop nginx service

To stop the NGINX service, we use either `systemctl` or `service` depending on the setup.

If ``systemd`` is enabled:
```bash
  sudo systemctl stop nginx
```

If ``systemd`` is not enabled:
```bash
  sudo service nginx stop
```
