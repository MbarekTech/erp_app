"""
Uninstallation script for SDRT app
"""
import frappe
from frappe import _


def before_uninstall():
	"""Runs before uninstallation"""
	# Clean up any custom data if needed
	cleanup_custom_data()
	
	# Remove custom fields
	remove_custom_fields()
	
	# Remove fixtures
	remove_fixtures()


def after_uninstall():
	"""Runs after uninstallation"""
	# Clean up any remaining data
	cleanup_remaining_data()
	
	frappe.db.commit()


def cleanup_custom_data():
	"""Clean up custom data created by SDRT"""
	try:
		# Remove SDRT Settings
		if frappe.db.exists("SDRT Settings", "SDRT Settings"):
			frappe.delete_doc("SDRT Settings", "SDRT Settings", ignore_permissions=True)
			
		frappe.msgprint(_("Custom data cleaned up"))
	except Exception as e:
		frappe.log_error(f"Error cleaning up custom data: {str(e)}")


def remove_custom_fields():
	"""Remove custom fields added by SDRT"""
	try:
		# List of custom fields to remove
		custom_fields_to_remove = [
			"Address-tax_category",
			"Address-is_your_company_address",
			"Contact-is_billing_contact"
		]
		
		for field_name in custom_fields_to_remove:
			if frappe.db.exists("Custom Field", field_name):
				frappe.delete_doc("Custom Field", field_name, ignore_permissions=True)
				
		frappe.msgprint(_("Custom fields removed"))
	except Exception as e:
		frappe.log_error(f"Error removing custom fields: {str(e)}")


def remove_fixtures():
	"""Remove fixtures installed by SDRT"""
	try:
		# Remove custom docperms
		frappe.db.sql("DELETE FROM `tabCustom DocPerm` WHERE parent IN (SELECT name FROM `tabDocType` WHERE module = 'Sdrt')")
		
		# Remove property setters
		frappe.db.sql("DELETE FROM `tabProperty Setter` WHERE doc_type IN (SELECT name FROM `tabDocType` WHERE module = 'Sdrt')")
		
		frappe.msgprint(_("Fixtures removed"))
	except Exception as e:
		frappe.log_error(f"Error removing fixtures: {str(e)}")


def cleanup_remaining_data():
	"""Clean up any remaining SDRT data"""
	try:
		# Remove any remaining SDRT documents
		doctypes_to_clean = [
			"Material Request",
			"SDR Budget", 
			"Direction",
			"Programme",
			"Convention",
			"Encaissement",
			"Financement du Convention"
		]
		
		for doctype in doctypes_to_clean:
			# Only clean if it's a custom doctype
			if frappe.db.exists("DocType", doctype):
				doc = frappe.get_doc("DocType", doctype)
				if doc.module == "Sdrt":
					# Delete all documents of this doctype
					frappe.db.sql(f"DELETE FROM `tab{doctype}`")
					
		frappe.msgprint(_("Remaining data cleaned up"))
	except Exception as e:
		frappe.log_error(f"Error cleaning up remaining data: {str(e)}")
