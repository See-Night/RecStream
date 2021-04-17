#!/bin/bash
# 
# Description: Control Script for RecStream's Document
# Author: SeeNight
# Blog: https://1145141919810.wang
# Github: https://github.com/Dreammer12138
# Gitee: https://gitee.com/Dreammer12138
# Date: 2020-12-31

case $1 in
	'start') 
		echo "Start docker nginx image"
		docker run \
			--name RecStreamDoc \
			-p 80:80 \
			-v $(pwd):/usr/share/nginx/html \
			-d nginx
	;;
	'stop')
		docker stop RecStreamDoc >> /dev/null \
			&& docker rm RecStreamDoc >> /dev/null
	;;
esac

