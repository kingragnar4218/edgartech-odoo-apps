from odoo import models, fields, api

class HospitalAppointment(models.Model):
    _name = 'poa_hospital_managementital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'

    patient_id = fields.Many2one('poa_hospital_managementital.patient', string='Hospital Patient', required=True)
    booking_time = fields.Datetime(string="Booking Time", default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)
    age = fields.Integer(string='Age', related='patient_id.age')
    description = fields.Text(string='Description')
    appointment_type = fields.Selection([
        ('checkup', 'Check-up'),
        ('emergency', 'Emergency'),
        ('consultation', 'Consultation')
    ], string='Appointment Type', default='checkup')
    is_urgent = fields.Boolean(string='Is Urgent?')
    fees = fields.Float(string='Appointment Fees')
    doctor_notes = fields.Html(string='Doctor Notes')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft', tracking=True)

    # Related fields for patient details
    gender = fields.Selection(related='patient_id.gender', string='Gender')
    contact = fields.Char(related='patient_id.contact', string="Phone Number")
    weight = fields.Float(related='patient_id.weight', string="Weight")
    active = fields.Boolean(related='patient_id.active', string="Active")
    blood_group = fields.Selection(related='patient_id.blood_group', string="Blood Group")
    medical_history = fields.Text(related='patient_id.medical_history', string="Medical History")
    chronic_diseases = fields.Text(related='patient_id.chronic_diseases', string="Chronic Diseases")
    allergies = fields.Text(related='patient_id.allergies', string="Allergies")
    last_visit_date = fields.Date(related='patient_id.last_visit_date', string="Last Visit Date")

    ref = fields.Char(string="Reference", required=True)
    next_appointment_date = fields.Date(string="Next Appointment Date")
    medical_history = fields.Text(related='patient_id.medical_history', string="Medical History")

    @api.onchange('patient_id')
    def _onchange_patient_id(self):
        if self.patient_id:
            self.ref = self.patient_id.ref or ''
        else:
            self.ref = ''
