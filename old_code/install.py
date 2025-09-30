"""
Installation script for SDRT app
"""
import frappe
from frappe import _
from frappe.utils import cint


def before_install():
	"""Runs before installation"""
	pass


def after_install():
	"""Runs after installation"""
	# Set up default settings
	setup_default_settings()
	
	# Create default data if needed
	create_default_data()
	
	# Set up permissions
	setup_permissions()
	
	frappe.db.commit()


def setup_default_settings():
	"""Set up default settings for SDRT"""
	try:
		# Create SDRT Settings if it doesn't exist
		if not frappe.db.exists("SDRT Settings", "SDRT Settings"):
			settings = frappe.new_doc("SDRT Settings")
			settings.app_title = "SDRT"
			settings.app_description = "SDRT Management System"
			settings.app_version = "1.0.0"
			settings.enable_budget_control = 1
			settings.default_budget_year = 2025
			settings.budget_approval_required = 0
			settings.enable_workflow = 1
			settings.auto_approve_limit = 1000
			settings.insert(ignore_permissions=True)
			frappe.db.commit()
			
		frappe.msgprint(_("SDRT Settings created successfully"))
	except Exception as e:
		frappe.log_error(f"Error creating SDRT Settings: {str(e)}")


def create_default_data():
	"""Create default data for SDRT"""
	try:
		# Create default Direction if none exists
		if not frappe.db.exists("Direction", {"name": "Default Direction"}):
			direction = frappe.new_doc("Direction")
			direction.direction_name = "Default Direction"
			direction.code_direction = "DEFAULT"
			direction.insert(ignore_permissions=True)
			
		# Create default Programme if none exists
		if not frappe.db.exists("Programme", {"name": "Default Programme"}):
			programme = frappe.new_doc("Programme")
			programme.programme_name = "Default Programme"
			programme.code_programme = "DEFAULT"
			programme.insert(ignore_permissions=True)
			
		frappe.msgprint(_("Default data created successfully"))
	except Exception as e:
		frappe.log_error(f"Error creating default data: {str(e)}")


def setup_permissions():
	"""Set up default permissions for SDRT"""
	try:
		# Ensure SDRT module permissions are set
		roles = ["System Manager", "Purchase Manager", "Stock Manager"]
		
		for role in roles:
			if frappe.db.exists("Role", role):
				# Set module permissions for SDRT
				module_permission = frappe.get_doc({
					"doctype": "Module Def",
					"module_name": "Sdrt",
					"custom": 1
				})
				
				# Add role permissions
				role_permission = frappe.get_doc({
					"doctype": "Role Permission",
					"role": role,
					"module": "Sdrt",
					"if_owner": 0,
					"apply_user_permissions": 0
				})
				
		frappe.msgprint(_("Permissions set up successfully"))
	except Exception as e:
		frappe.log_error(f"Error setting up permissions: {str(e)}")


def before_tests():
	"""Runs before tests"""
	pass
