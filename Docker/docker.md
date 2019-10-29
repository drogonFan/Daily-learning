# Docker

df -h 查看分区大小

默认情况下，docker将运行目录配置在/var/lib/docker

在这里/var配置了30个G

服务器配额

    Filesystem      Size  Used Avail Use% Mounted on
    udev             32G     0   32G   0% /dev
    tmpfs           6.3G  1.4M  6.3G   1% /run
    /dev/sda2        98G   11G   83G  11% /
    tmpfs            32G     0   32G   0% /dev/shm
    tmpfs           5.0M     0  5.0M   0% /run/lock
    tmpfs            32G     0   32G   0% /sys/fs/cgroup
    /dev/sda4       976M  143M  767M  16% /boot
    /dev/sda6       4.9G   21M  4.6G   1% /tmp
    /dev/sda3        63G   53M   60G   1% /swap
    /dev/sda5        30G  625M   28G   3% /var
    /dev/sdb1        15T   20M   14T   1% /home
    /dev/loop0       89M   89M     0 100% /snap/core/7270
    /dev/loop1       91M   91M     0 100% /snap/core/6350
    tmpfs           6.3G     0  6.3G   0% /run/user/1000


使用阿里云提供的镜像加速服务，目前是免费的
配置文件/etc/docker/daemon.json

    {
        "registry-mirrors: ["https://uap92c0j.mirror.aliyuncs.com"],
        "live-restore": true
    }

可配置选型

    {
        "authorization-plugins": [],
        "data-root": "",
        "dns": [],
        "dns-opts": [],
        "dns-search": [],
        "exec-opts": [],
        "experimental": false,
        "features":{},
        "storage-driver": "",
        "storage-opts": [],
        "labels": [],
        "log-driver": "",
        "mtu": 0,
        "pidfile": "",
        "cluster-store": "",
        "cluster-advertise": "",
        "max-concurrent-downloads": 3,
        "max-concurrent-uploads": 5,
        "shutdown-timeout": 15,
        "debug": true,
        "hosts": [],
        "log-level": "",
        "tlsverify": true,
        "tlscacert": "",
        "tlscert": "",
        "tlskey": "",
        "swarm-default-advertise-addr": "",
        "group": "",
        "default-ulimits": {},
        "bridge": "",
        "fixed-cidr": "",
        "raw-logs": false,
        "allow-nondistributable-artifacts": [],
        "registry-mirrors": [],
        "insecure-registries": []
    }

可能会遇到错误，需要查看配置文件设置是否正确，随后重启docker服务

    ● docker.service - Docker Application Container Engine
    Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
    Active: failed (Result: exit-code) since Fri 2019-08-09 12:55:06 UTC; 26s ago
        Docs: https://docs.docker.com
    Process: 3441 ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock (code=exited, status=1/FAILURE)
    Main PID: 3441 (code=exited, status=1/FAILURE)

    Aug 09 12:55:06 dlut_se systemd[1]: docker.service: Service hold-off time over, scheduling restart.
    Aug 09 12:55:06 dlut_se systemd[1]: docker.service: Scheduled restart job, restart counter is at 3.
    Aug 09 12:55:06 dlut_se systemd[1]: Stopped Docker Application Container Engine.
    Aug 09 12:55:06 dlut_se systemd[1]: docker.service: Start request repeated too quickly.
    Aug 09 12:55:06 dlut_se systemd[1]: docker.service: Failed with result 'exit-code'.
    Aug 09 12:55:06 dlut_se systemd[1]: Failed to start Docker Application Container Engine.

配置完成后可以使用docker info查看配置结果

docker启动遇到问题后
使用命令查看

    systemctl status docker.service

配置其他用户可以使用docker

新建docker用户组

sudo groupadd docker
sudo usermod -aG docker ${user}

下载docker镜像

    docker pull gitlab/gitlab-ce:latest

安装Docker Compose

1. 运行此命令以下载Docker Compose的当前稳定版本：

    sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

2. 对二进制文件应用可执行权限：

    sudo chmod +x /usr/local/bin/docker-compose

3. 测试安装

    $ docker-compose --version
    docker-compose version 1.24.1, build 1110ad01

## 安装gitlab的docker镜像

设置外部的URL并启动容器

    sudo docker run --detach \
    --hostname gitlab.example.com \
    --env GITLAB_OMNIBUS_CONFIG="external_url 'http://my.domain.com/'; gitlab_rails['lfs_enabled'] = true;" \
    --publish 443:443 --publish 80:80 --publish 22:22 \
    --name gitlab \
    --restart always \
    --volume /srv/gitlab/config:/etc/gitlab \
    --volume /srv/gitlab/logs:/var/log/gitlab \
    --volume /srv/gitlab/data:/var/opt/gitlab \
    gitlab/gitlab-ce:latest

初始化过程可能需要很长时间。您可以使用该命令跟踪此过程sudo docker logs -f gitlab

### 升级gitlab到更新版本

1. 停止正在运行的容器

    sudo docker stop gitlab

2. 删除现有容器：

    sudo docker rm gitlab

3. 拉新图片

    sudo docker pull gitlab/gitlab-ce:latest

4. 使用指定的选项再次创建容器
端口转发规则（80：Http 访问端口，443：Https 访问端口，8888：主机的 ssh 访问端口，22：Docker 容器中 ssh 访问端口）

实际使用的配置

    sudo docker run --detach \
    --hostname gitlab.example.com \
    --publish 8443:443 --publish 8888:80 --publish 2222:22 \
    --name gitlab \
    --restart always \
    --volume /home/oscar/gitlab/config:/etc/gitlab \
    --volume /home/oscar/gitlab/logs:/var/log/gitlab \
    --volume /home/oscar/gitlab/data:/var/opt/gitlab \
    gitlab/gitlab-ce:latest

在公共ip上运行gitlab

    sudo docker run --detach \
    --hostname gitlab.example.com \
    --publish 198.51.100.1:443:443 \
    --publish 198.51.100.1:80:80 \
    --publish 198.51.100.1:22:22 \
    --name gitlab \
    --restart always \
    --volume /srv/gitlab/config:/etc/gitlab \
    --volume /srv/gitlab/logs:/var/log/gitlab \
    --volume /srv/gitlab/data:/var/opt/gitlab \
    gitlab/gitlab-ce:latest

在不同的端口上公开gitlab

    sudo docker run --detach \
    --hostname gitlab.example.com \
    --publish 8929:8929 --publish 2289:22 \
    --name gitlab \
    --restart always \
    --volume /srv/gitlab/config:/etc/gitlab \
    --volume /srv/gitlab/logs:/var/log/gitlab \
    --volume /srv/gitlab/data:/var/opt/gitlab \
    gitlab/gitlab-ce:latest


当地的位置	集装箱位置	用法
/srv/gitlab/data	/var/opt/gitlab	用于存储应用数据
/srv/gitlab/logs	/var/log/gitlab	用于存储日志
/srv/gitlab/config	/etc/gitlab	用于存储GitLab配置文件



```
# 配置http协议所使用的访问地址
external_url 'http://10.200.0.100:8080'

# 配置ssh协议所使用的访问地址和端口
gitlab_rails['gitlab_ssh_host'] = '10.200.0.100'
gitlab_rails['gitlab_shell_ssh_port'] = 2222


# nginx['listen_port'] = nil
nginx['listen_port'] = 80

# 这里以新浪的邮箱为例配置smtp服务器
gitlab_rails['smtp_enable'] = true
gitlab_rails['smtp_address'] = "smtp.sina.com"
gitlab_rails['smtp_port'] = 25
gitlab_rails['smtp_user_name'] = "name4mail"
gitlab_rails['smtp_password'] = "passwd4mail"
gitlab_rails['smtp_domain'] = "sina.com"
gitlab_rails['smtp_authentication'] = :login
gitlab_rails['smtp_enable_starttls_auto'] = true


```

## User email confirmation at sign-up

GitLab can be configured to require confirmation of a user’s email address when the user signs up. When this setting is enabled, the user is unable to sign in until they confirm their email address.

In the Admin area under Settings (/admin/application_settings), go to section Sign-up Restrictions and look for the Send confirmation email on sign-up option.


本周工作：
1. 将gitlab服务器公网ip配置完成，完成了smtp的配置(使用163的服务)，给实验室的人分配了账号，现在已经可以正常使用
2. 完善了一下发票报销的小系统，已经可以满足基本使用


看了一下gitlab-ce现在不支持限定项目的大小（gitlab-ee支持，但是要收费），gitlab-ce只支持限制用户上传项目数和附件的大小
