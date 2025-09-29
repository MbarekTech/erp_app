# SDRT Installation Troubleshooting Guide

## esbuild Error Resolution

If you encounter the following error during installation:

```
TypeError [ERR_INVALID_ARG_TYPE]: The "paths[0]" argument must be of type string. Received undefined
```

This is a known issue with Frappe's esbuild system. Here are several solutions:

## Solution 1: Skip Assets During Installation (Recommended)

```bash
# Remove any failed installation first
rm -rf /home/frappe/frappe-bench/apps/sdrt

# Install with skip-assets flag
bench get-app --skip-assets https://github.com/MbarekTech/erp_app.git
bench install-app sdrt
bench migrate
bench restart
```

## Solution 2: Manual Installation

```bash
# Clone the repository manually
cd /home/frappe/frappe-bench/apps
git clone https://github.com/MbarekTech/erp_app.git sdrt

# Install without building assets
bench install-app sdrt --skip-assets
bench migrate
bench restart
```

## Solution 3: Build Assets Separately

```bash
# Install the app first
bench get-app --skip-assets https://github.com/MbarekTech/erp_app.git
bench install-app sdrt

# Try building assets separately (if needed)
bench build --app sdrt --skip-assets
bench migrate
bench restart
```

## Solution 4: Use Development Mode

```bash
# Install in development mode
bench get-app --skip-assets https://github.com/MbarekTech/erp_app.git
bench install-app sdrt
bench develop
bench migrate
bench restart
```

## Post-Installation Setup

After successful installation:

1. **Access the App:**
   - Navigate to your ERPNext instance
   - The SDRT module should appear in the desk

2. **Create Initial Data:**
   - Go to SDRT > Direction and create organizational directions
   - Go to SDRT > Programme and create programs
   - Go to SDRT > Convention and create conventions
   - Go to SDRT > SDR Budget and create budget items

3. **Configure Permissions:**
   - Assign appropriate roles to users
   - Configure user permissions for SDRT features

## Troubleshooting

### If the app still doesn't install:

1. **Check Frappe Version:**
   ```bash
   bench version
   ```
   Ensure you're using Frappe v15+

2. **Clear Cache:**
   ```bash
   bench clear-cache
   bench clear-website-cache
   ```

3. **Check Node.js Version:**
   ```bash
   node -v
   yarn -v
   ```
   Ensure Node.js 18+ and Yarn are installed

4. **Manual Asset Building:**
   ```bash
   cd /home/frappe/frappe-bench/apps/sdrt
   yarn install
   yarn build
   ```

### If you get permission errors:

```bash
# Fix ownership
sudo chown -R frappe:frappe /home/frappe/frappe-bench/apps/sdrt
```

## Alternative Installation Methods

### Method 1: Docker Installation
```bash
# Use the provided Docker setup
cd docker_setup
docker-compose up -d
```

### Method 2: Manual File Copy
```bash
# Copy files manually
cp -r /path/to/sdrt /home/frappe/frappe-bench/apps/
bench install-app sdrt
```

## Support

If you continue to experience issues:

1. Check the Frappe community forums
2. Review the ERPNext documentation
3. Ensure your system meets all requirements
4. Consider using the Docker setup for a clean environment

## Requirements

- Frappe Framework v15+
- ERPNext v15+
- Python 3.10+
- Node.js 18+
- MySQL/MariaDB
- Yarn package manager
