# SDRT Installation Guide

This guide explains how to install the SDRT app in your Frappe/ERPNext Docker setup.

## Overview

The Docker setup is configured to install the base system (Frappe, ERPNext, HRMS, Print Designer) automatically. The SDRT app is then installed manually after the base system is running.

## Step 1: Start the Base System

1. Make sure Docker Desktop is running
2. Navigate to the `docker_setup` directory
3. Start the base system:

```bash
docker-compose up --build
```

Wait for the installation to complete. You should see:
```
Base system installed successfully. SDRT app can be installed manually after the system is running.
```

## Step 2: Install SDRT App

Once the base system is running, install SDRT using one of these methods:

### Option A: Using the Installation Script (Recommended)

**Windows:**
```cmd
install_sdrt.bat
```

**Linux/Mac:**
```bash
chmod +x install_sdrt.sh
./install_sdrt.sh
```

### Option B: Manual Installation

1. Find the backend container ID:
```bash
docker-compose ps -q backend
```

2. Install the app:
```bash
# Replace CONTAINER_ID with the actual container ID
docker exec -it CONTAINER_ID bench get-app --branch main https://github.com/MbarekTech/erp_app.git
docker exec -it CONTAINER_ID bench --site frontend install-app sdrt
```

3. Restart services:
```bash
docker-compose restart backend frontend
```

## Step 3: Access Your Site

- **URL:** http://localhost:8080
- **Username:** Administrator
- **Password:** 123456@info

## Troubleshooting

### If SDRT installation fails:

1. Check the logs:
```bash
docker-compose logs backend
```

2. Enter the container to debug:
```bash
docker exec -it $(docker-compose ps -q backend) bash
```

3. Inside the container, you can run:
```bash
bench get-app --branch main https://github.com/MbarekTech/erp_app.git
bench --site frontend install-app sdrt --force
```

### If the base system fails to start:

1. Clean up and rebuild:
```bash
docker-compose down --volumes
docker-compose up --build
```

2. Check if Docker Desktop is running and has enough resources allocated

## Benefits of This Approach

1. **Faster debugging** - Base system installs first, SDRT issues are isolated
2. **No cache issues** - SDRT is installed fresh each time
3. **Better error visibility** - Can see exactly where SDRT installation fails
4. **Flexible** - Can reinstall just SDRT without rebuilding everything

## Files Modified

- `Dockerfile` - Removed SDRT installation
- `docker-compose.yml` - Removed SDRT from site creation
- `install_sdrt.bat/sh` - New installation scripts

