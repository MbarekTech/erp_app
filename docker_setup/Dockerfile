# Use the same base image specified in your docker-compose.yml
FROM frappe/erpnext:v15.77.0

# Switch to the frappe user to run bench commands
USER frappe

# Navigate to the bench directory
WORKDIR /home/frappe/frappe-bench

# Get the standard apps from their repositories
RUN bench get-app hrms --skip-assets
RUN bench get-app print_designer --skip-assets

# Get your custom app from its repository
RUN bench get-app https://github.com/MbarekTech/erp_app.git --skip-assets