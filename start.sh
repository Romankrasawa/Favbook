#!/bin/bash
ls
folders=(book_forum forum user home)
for i in ${folders[*]}
do
    cd book_forum/$i/static
    scss --watch scss:css &
    echo $i is ready...
    cd ../../..
done

systemctl start docker

echo "docker is ready"

cd ~

sudo docker compose up -d

echo "docker compose is ready"
