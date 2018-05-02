# simple_bot

************
Introduction
************
simple_bot is a Tornado-based Microsoft bot-framework sample in Docker.
- Tornado-based service which responds to Bot Framework requests
- Dockerfile which builds container (CentOS base image).
- Container when run will execute the sample
- Container exposes port 8080

- Note: On Windows, port is most likely mapped - to use Emulator, look at 
  "docker ps" to see where port was mapped to.

Note: The bot framework currently supports only Python 3.6+.  Most likely this
  could be ported to Python 2.7, but haven't attempted. 


**********************************************
# Setup Python & Sample (Fedora/Redhat/CentOS)
**********************************************
```sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm 
sudo yum clean all
sudo yum update -y
sudo yum -y install python36u
sudo yum -y install python36u-pip
sudo yum -y install git
sudo yum -y install docker
sudo pip3.6 install --upgrade pip
sudo pip3.6 install botframework-connector;

sudo systemctl start docker
```
# Install Sample
```cd ~
git clone https://github.com/daveta/simple_bot.git
```

# Build sample

```cd ~/simple_bot/docker/baseimage
sudo docker build --rm -t local/cent7-latest .
cd ~/simple_bot
sudo docker build --rm -t local/simple_bot -f docker/botimage/Dockerfile .
```

# Run bot
```sudo docker run -d local/simple_bot```


## Example: See container running.  Note: Port 8080 exposed
```$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS               NAMES
4c73cde9a306        local/simple_bot    "python3.6 /simple..."   2 minutes ago       Up 2 minutes        8080/tcp            quirky_raman
```
## Example: Get ip address

```$ docker inspect 
 docker inspect 4c73cde9a306
[
 …
        "NetworkSettings": {
            "IPAddress": "172.17.0.2",


## Example: Test Tornado connection
```

```$ wget 172.17.0.2:8080
--2018-05-02 16:56:17--  http://172.17.0.2:8080/
Connecting to 172.17.0.2:8080... connected.
HTTP request sent, awaiting response... 200 All good
…

$ cat index.html
Hello, world
```
