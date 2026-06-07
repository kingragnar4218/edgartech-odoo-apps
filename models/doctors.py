from odoo import models, fields

class HospitalDoctors(models.Model):
    _name = 'poa_hospital_managementital.doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital doctor'

    name = fields.Char(string='doctor Name', tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True)
    contact = fields.Char(string="Phone Number", tracking=True)
    doctor_id = fields.Integer(string='doctor identifier code')
    budge_number = fields.Integer(string="Budge Number", required=True)
    category = fields.Selection([
        ('doctor', 'Doctor'),
        ('surgeon', 'Surgeon'),
        ('nurse', 'Nurse'),
    ], string="Category")
    specialization = fields.Char(string='Specialization', tracking=True)
    years_of_experience = fields.Integer(string='Years of Experience', tracking=True)
    working_hours = fields.Char(string='Working Hours', tracking=True)
