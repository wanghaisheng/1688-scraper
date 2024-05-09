

店铺商品爬取

## Docker部署

```shell
docker build -t 1688-scraper-app . --network host 
docker run -itd -p 5000:5000 1688-scraper-app
docker logs -f 1688-scraper-app
docker stop 
docker start -i
```

```text
# 安装node,保证环境中有JS环境
RUN wget https://nodejs.org/dist/v14.21.3/node-v14.21.3-linux-x64.tar.xz
RUN xz -d node-v14.21.3-linux-x64.tar.xz
RUN tar -xvf node-v14.21.3-linux-x64.tar
 
# 添加软链接 /usr/local/bin/node /usr/bin/node 
RUN ln -s /node-v14.21.3-linux-x64/bin/node /usr/bin/node 
RUN ln -s /node-v14.21.3-linux-x64/bin/npm /usr/bin/npm 
```

```text
# 安装Node.js
RUN curl -sL https://rpm.nodesource.com/setup_16.x | bash - \
&& yum install -y nodejs
```

## Docker常用命令

构建镜像: (在项目根目录执行) 

> - `docker build`：这是Docker用来构建镜像的命令。
> - `-t tiktok-service-app`：这个选项用来给构建的镜像设置一个标签（tag），在这个例子中标签是tiktok-service-app。标签可以帮助你更容易地识别和管理你的Docker镜像。
> - `.`：这个点代表当前目录，Docker会在这个目录下查找Dockerfile文件，该文件包含了构建镜像所需的指令。
```shell
docker build -t tiktok-service-app .
```

查看镜像:

`````shell
docker images
`````

启动容器:

> - `docker run`：这是Docker用来创建并启动新容器的命令。
> - `-itd`：这是三个选项的组合：
>   - `-i`：交互式，允许你与容器进行交互。
>   - `-t`：分配一个伪终端，这样你就可以在命令行中与容器进行交互。
>   - `-d`：以分离模式运行容器，即在后台运行。
> - `-p 8888:8080`：这个选项用于端口映射，格式为`<主机端口>:<容器端口>`。在这个例子中，它将主机的8888端口映射到容器的8080端口。
> - `tiktok-service-app`：这是要运行的Docker镜像的名称。Docker会根据这个名称查找本地的镜像库，如果找到匹配的镜像，就会用它来创建一个新的容器。

```shell
 docker run -itd -p 8888:8080 tiktok-service-app 
```

查看正在运行的容器(添加`-a`参数查看全部容器):

```shell
docker ps
```

进入容器:

> - `docker exec`：这是Docker用来在已经运行的容器中执行命令的命令。
> - `-it`：这是两个选项的组合：
>   - `-i`：交互式，允许你与容器进行交互。
>   - `-t`：分配一个伪终端，这样你就可以在命令行中与容器进行交互。
> - `<容器名称或ID>`：这是要进入的容器的名称或者ID。
> - `/bin/bash`：这是要在容器中运行的命令，这里是启动bash shell。

```shell
docker exec -it <容器名称或ID> /bin/bash
```

查看运行日志:

> - `docker logs`：这是Docker用来获取容器日志的命令。
> - `-f` 或 `--follow`：这个选项会让日志输出变成实时的，即你可以即时看到最新的日志输出。
> - `58cda55c3cd4`：这是容器的ID。Docker会根据这个ID查找正在运行的容器，并输出该容器的日志。

```shell
docker logs -f <容器名称或ID>
```



停止容器

```shell
docker stop <容器名称或ID>
```

删除容器

```shell
docker rm <容器名称或ID>
```

删除镜像

```shell
docker rmi <镜像名称或ID>
```
