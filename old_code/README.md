# SDRT - Système de Demande et de Réception de Travaux

A comprehensive ERPNext app for managing purchase requests, budget control, and procurement workflows in French organizations.

## Features

### 🏢 Organizational Management
- **Direction Management**: Organize departments and directions
- **Programme Management**: Track programs and projects
- **Convention Management**: Manage agreements and contracts

### 💰 Budget Control
- **SDR Budget**: Comprehensive budget management
- **Analytical Codes**: Track expenses by analytical dimensions
- **Budget Monitoring**: Real-time budget vs actual tracking
- **Commitment Management**: Track committed vs available amounts

### 📋 Procurement Workflow
- **Enhanced Material Requests**: Custom fields for French procurement
- **Purchase Order Integration**: Seamless integration with ERPNext PO
- **Purchase Receipt Tracking**: Enhanced receipt management
- **Budget Validation**: Automatic budget checks during procurement

### 🔧 Custom Features
- **Custom Fields**: Extended ERPNext with French-specific fields
- **Workflow Integration**: Approval workflows for procurement
- **Multi-language Support**: French interface and terminology
- **Reporting**: Custom reports for budget and procurement analysis

## Installation

### Prerequisites
- Frappe Framework v15+
- ERPNext v15+
- Python 3.10+
- MySQL/MariaDB

### Quick Install
```bash
# Using bench
bench get-app https://github.com/your-repo/sdrt.git
bench install-app sdrt
bench migrate
bench restart
```

### Manual Install
```bash
# Clone the repository
git clone https://github.com/your-repo/sdrt.git
cd sdrt

# Copy to bench apps directory
cp -r . /path/to/bench/apps/sdrt

# Install the app
bench install-app sdrt
```

## Configuration

### 1. Initial Setup
After installation, configure the following:

1. **SDRT Settings**: Navigate to SDRT > SDRT Settings
2. **Directions**: Create organizational directions
3. **Programmes**: Set up programs and projects
4. **Conventions**: Configure agreements

### 2. User Permissions
Ensure users have appropriate roles:
- **System Manager**: Full access
- **Purchase Manager**: Procurement access
- **Stock Manager**: Inventory access

### 3. Budget Setup
1. Create SDR Budget entries
2. Set analytical codes
3. Configure budget limits
4. Set up approval workflows

## Usage

### Material Request Workflow
1. Create a Material Request
2. Add items to "Demande d'achat" table
3. Set analytical codes and budget constraints
4. Submit for approval

### Budget Management
1. Create SDR Budget entries
2. Monitor committed vs available amounts
3. Track budget utilization
4. Generate budget reports

### Purchase Integration
1. Create Purchase Orders from Material Requests
2. Budget amounts are automatically committed
3. Track procurement against budget
4. Monitor delivery and receipt

## Customization

### Custom Fields
The app adds custom fields to:
- **Address**: Tax Category, Company Address
- **Contact**: Billing Contact
- **Company**: HR & Payroll settings

### Document Types
Custom doctypes include:
- **Direction**: Organizational directions
- **Programme**: Program management
- **Convention**: Convention management
- **SDR Budget**: Budget management
- **Enhanced Material Request**: Extended functionality

## API Integration

### REST API
```python
# Get budget information
GET /api/resource/SDR Budget

# Create material request
POST /api/resource/Material Request
```

### Python API
```python
import frappe

# Get SDRT settings
settings = frappe.get_doc("SDRT Settings", "SDRT Settings")

# Create budget entry
budget = frappe.new_doc("SDR Budget")
budget.direction = "Direction 1"
budget.programme = "Programme 1"
budget.montant = 10000
budget.insert()
```

## Troubleshooting

### Common Issues

1. **Installation fails**:
   - Check ERPNext installation
   - Verify Python/Node.js versions
   - Ensure database connectivity

2. **Custom fields not appearing**:
   - Run `bench migrate`
   - Clear browser cache
   - Check user permissions

3. **Budget calculations incorrect**:
   - Verify analytical codes
   - Check budget entries
   - Review commitment logic

### Debug Mode
```bash
bench --site your-site set-config developer_mode 1
bench restart
```

## Development

### Setup Development Environment
```bash
# Clone repository
git clone https://github.com/your-repo/sdrt.git
cd sdrt

# Install dependencies
pip install -e .

# Run tests
bench --site your-site run-tests
```

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Support

- **Documentation**: [Installation Guide](INSTALLATION_GUIDE.md)
- **Issues**: [GitHub Issues](https://github.com/your-repo/sdrt/issues)
- **Email**: ouchgoutmohamed@gmail.com

## License

MIT License - see [LICENSE](license.txt) for details.

## Changelog

### v1.0.0
- Initial release
- Basic SDRT functionality
- Budget management
- Material request enhancements

### v1.1.0
- Added workflow integration
- Enhanced budget controls
- Improved reporting

### v1.2.0
- Added convention management
- Enhanced procurement workflow
- Improved user interface