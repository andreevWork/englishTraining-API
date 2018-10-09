#!/usr/bin/env bash

echo "docker-compose down" && \
/usr/local/bin/docker-compose down && \
echo "docker-compose rm -f --all" && \
/usr/local/bin/docker-compose rm -f --all && \
echo "docker-compose build --no-cache" && \
/usr/local/bin/docker-compose build --no-cache && \
echo "docker-compose up -d --force-recreate --remove-orphans" && \
/usr/local/bin/docker-compose up -d --force-recreate --remove-orphans