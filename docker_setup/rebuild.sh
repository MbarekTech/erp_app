#!/bin/bash

echo "Stopping all containers..."
docker-compose down --volumes --remove-orphans 2>/dev/null || true

echo "Removing old images..."
docker rmi erpnext-hrms-custom:latest 2>/dev/null || true
docker rmi erpnext-hrms-custom:v2 2>/dev/null || true

echo "Cleaning up Docker system..."
docker system prune -f 2>/dev/null || true

echo "Building fresh containers with no cache..."
CACHE_BUST=$(date +%s) docker-compose build --no-cache

echo "Starting the services..."
docker-compose up

