echo "echo '192.168.62.11 www-prd.luxairtours.lu' > /etc/hosts"
docker run --rm -it -p 8091:8091 --entrypoint=/bin/bash -v /home/ubuntu/tsung:/root/.tsung prima/tsung
