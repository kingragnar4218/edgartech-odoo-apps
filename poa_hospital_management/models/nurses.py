from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class HospitalNurse(models.Model):
    _name = 'poa_hospital_managementital.nurse'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital nurses'

    name = fields.Char(string='Nurse Name', tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', tracking=True)
    contact = fields.Char(string="Phone Number", tracking=True)
    doctor_id = fields.Integer(string='doctor identifier code')
    budge_number = fields.Integer(string='Budge Number') 
