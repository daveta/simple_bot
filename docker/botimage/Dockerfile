FROM local/cent7-latest

# File Author / Maintainer
MAINTAINER fuselabs

# Update yum to get python3.6 repo
RUN  yum -y install https://centos7.iuscommunity.org/ius-release.rpm; yum clean all; yum update -y
# Install python3.6 (and associated pip)
RUN yum -y install python36u; yum -y install python36u-pip
# Install dependencies
RUN pip3.6 install --upgrade pip; pip3.6 install botframework-connector; 

# Copy sample application
ADD python/simple_bot/simple_bot /simple_bot

# Get pip to download and install requirements:
RUN pip3.6 install -r /simple_bot/requirements.txt

EXPOSE 8080
ENTRYPOINT ["python3.6", "/simple_bot/service_host.py"]
