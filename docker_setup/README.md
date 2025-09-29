# Docker Setup for ERPNext with SDRT App

## Overview
This Docker setup provides a complete ERPNext environment with the custom SDRT app pre-installed.

## Services Included
- **Backend**: ERPNext application server
- **Frontend**: Nginx reverse proxy
- **Database**: MariaDB 10.6
- **Redis**: Cache and queue management
- **Workers**: Background job processors
- **Scheduler**: Cron job scheduler
- **WebSocket**: Real-time communication

## Apps Installed
- ERPNext (core)
- HRMS
- Print Designer
- SDRT (custom app)

## Quick Start

1. **Create network** (if not exists):
   ```bash
   docker network create shared-web-network
   ```

2. **Build and start services**:
   ```bash
   docker-compose up -d
   ```

3. **Access ERPNext**:
   - URL: http://localhost:8080
   - Username: Administrator
   - Password: 123456@info

## Security Recommendations

⚠️ **IMPORTANT**: Change default passwords before production use!

1. Update passwords in `docker-compose.yml`:
   - `MYSQL_ROOT_PASSWORD`
   - `MARIADB_ROOT_PASSWORD` 
   - Admin password in create-site command

2. Use environment variables for sensitive data

## Troubleshooting

- Check logs: `docker-compose logs [service-name]`
- Restart services: `docker-compose restart`
- Rebuild: `docker-compose up --build`

## Custom App Development

The SDRT app is automatically installed during container build. To update:

1. Push changes to GitHub repository
2. Rebuild Docker image: `docker-compose build --no-cache`
3. Restart services: `docker-compose up -d`

..
