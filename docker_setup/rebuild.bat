@echo off

echo Stopping all containers...
docker-compose down --volumes --remove-orphans 2>nul

echo Removing old images...
docker rmi erpnext-hrms-custom:latest 2>nul
docker rmi erpnext-hrms-custom:v2 2>nul

echo Cleaning up Docker system...
docker system prune -f 2>nul

echo Building fresh containers with no cache...
set CACHE_BUST=%date%_%time%
docker-compose build --no-cache

echo Starting the services...
docker-compose up
