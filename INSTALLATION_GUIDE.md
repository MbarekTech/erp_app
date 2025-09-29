# SDRT App Installation Guide

## Prerequisites

- Frappe Framework v15+
- ERPNext v15+
- Python 3.10+
- Node.js 18+
- MySQL/MariaDB

## Installation Methods

### Method 1: Using Bench (Recommended)

1. **Navigate to your bench directory:**
   ```bash
   cd /path/to/your/bench
   ```

2. **Install the SDRT app:**
   ```bash
   bench get-app https://github.com/your-repo/sdrt.git
   bench install-app sdrt
   ```

3. **Migrate the database:**
   ```bash
   bench migrate
   ```

4. **Restart the bench:**
   ```bash
   bench restart
   ```

### Method 2: Manual Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/sdrt.git
   cd sdrt
   ```

2. **Copy to apps directory:**
   ```bash
   cp -r . /path/to/bench/apps/sdrt
   ```

3. **Install the app:**
   ```bash
   bench install-app sdrt
   ```

## Post-Installation Setup

### 1. Create Default Data

After installation, create the following default data:

#### Directions
- Navigate to **SDRT > Direction**
- Create default directions for your organization

#### Programmes
- Navigate to **SDRT > Programme**
- Create default programmes

#### Conventions
- Navigate to **SDRT > Convention**
- Create default conventions

### 2. Configure User Permissions

Ensure users have appropriate roles:
- **System Manager**: Full access to all SDRT features
- **Purchase Manager**: Access to Material Requests and Purchase Orders
- **Stock Manager**: Access to inventory-related features

### 3. Set Up Budget Items

1. Navigate to **SDRT > SDR Budget**
2. Create budget items with proper analytical codes
3. Set up budget amounts and constraints

## Configuration

### Custom Fields

The app adds custom fields to standard ERPNext doctypes:
- **Address**: Tax Category, Company Address
- **Contact**: Billing Contact
- **Company**: HR & Payroll settings

### Document Types

The app creates the following custom doctypes:
- **Direction**: Organizational directions
- **Programme**: Program management
- **Convention**: Convention management
- **SDR Budget**: Budget management
- **Material Request**: Enhanced material requests
- **Purchase Order Item**: Enhanced purchase order items
- **Purchase Receipt Item**: Enhanced purchase receipt items

## Usage

### 1. Material Request Workflow

1. Create a **Material Request**
2. Add items to the **Demande d'achat** table
3. Set analytical codes and budget constraints
4. Submit for approval

### 2. Budget Management

1. Create **SDR Budget** entries
2. Set analytical codes and amounts
3. Monitor committed vs available amounts

### 3. Purchase Order Integration

1. Create **Purchase Orders** from Material Requests
2. Budget amounts are automatically committed
3. Track budget utilization

## Troubleshooting

### Common Issues

1. **Installation fails with dependency error:**
   - Ensure ERPNext is properly installed
   - Check Python and Node.js versions

2. **Custom fields not appearing:**
   - Run `bench migrate`
   - Clear browser cache

3. **Permissions not working:**
   - Check user roles
   - Verify module permissions

### Debug Mode

Enable debug mode for troubleshooting:
```bash
bench --site your-site set-config developer_mode 1
bench restart
```

## Uninstallation

To uninstall the SDRT app:

```bash
bench uninstall-app sdrt
```

**Warning**: This will remove all SDRT data and customizations.

## Support

For support and issues:
- Create an issue on GitHub
- Contact: ouchgoutmohamed@gmail.com

## Version History

- **v1.0.0**: Initial release with basic SDRT functionality
- **v1.1.0**: Added budget management features
- **v1.2.0**: Enhanced Material Request workflow