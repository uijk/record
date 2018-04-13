1. `wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py`
1. `pip install shadowsocks`
1. `sslocal -s ip -p 443 -k "code" -l 1080 -m aes-256-cfb`
1. `chkconfig shadowsocks on && service shadowsocks start`
1. `curl --socks5 127.0.0.1:1080 ip.cn` 
1. `yum -y install priv oxy`
1. `cp /etc/privoxy/config /etc/privoxy/config_bak`
1. ensure below lines are not commented, line1 usually not, line2 need modify
	```
	listen-address 127.0.0.1:8118 
	forward-socks5t / 127.0.0.1:1080 . 
	```
1. Add belows to .bashrc
	```
	export http_proxy=http://127.0.0.1:8118
	export https_proxy=http://127.0.0.1:8118
	```
1. `chkconfig privoxy on && service privoxy start`
1. `curl ip.cn` 
