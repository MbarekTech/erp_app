# Copyright (c) 2025, SDRT and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class SDRTSettings(Document):
	"""SDRT Settings DocType"""
	
	def validate(self):
		"""Validate SDRT Settings"""
		self.validate_budget_year()
		self.validate_approver()
	
	def validate_budget_year(self):
		"""Validate budget year"""
		if self.default_budget_year and self.default_budget_year < 2020:
			frappe.throw("Budget year must be 2020 or later")
	
	def validate_approver(self):
		"""Validate default approver"""
		if self.default_approver and not frappe.db.exists("User", self.default_approver):
			frappe.throw("Default approver must be a valid user")
	
	def get_budget_control_status(self):
		"""Get budget control status"""
		return self.enable_budget_control
	
	def get_workflow_status(self):
		"""Get workflow status"""
		return self.enable_workflow
	
	def get_auto_approve_limit(self):
		"""Get auto approve limit"""
		return self.auto_approve_limit or 0
