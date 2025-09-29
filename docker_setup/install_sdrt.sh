#!/bin/bash

echo "Installing SDRT app..."

# Get the container ID for the backend service
CONTAINER_ID=$(docker-compose ps -q backend)

if [ -z "$CONTAINER_ID" ]; then
    echo "Error: Backend container not found. Make sure the Docker setup is running."
    exit 1
fi

echo "Found backend container: $CONTAINER_ID"

# Install the SDRT app
echo "Step 1: Getting SDRT app from GitHub..."
docker exec -it $CONTAINER_ID bench get-app --branch main https://github.com/MbarekTech/erp_app.git

echo "Step 2: Installing SDRT app on the site..."
docker exec -it $CONTAINER_ID bench --site frontend install-app sdrt

echo "Step 3: Restarting services..."
docker-compose restart backend frontend

echo "SDRT app installation completed!"
echo "You can now access your site at http://localhost:8080"
echo "Login with: Administrator / 123456@info"

