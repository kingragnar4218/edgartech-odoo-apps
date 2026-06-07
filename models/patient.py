from odoo import models, fields, api

class HospitalPatient(models.Model):
    _name = 'poa_hospital_managementital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'

    # Basic Information
    name = fields.Char(string='Patient Name', required=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender', tracking=True)
    contact = fields.Char(string="Phone Number", tracking=True)
    email = fields.Char(string="Email Address")
    address = fields.Text(string="Address")
    date_of_birth = fields.Date(string="Date of Birth")
    blood_group = fields.Selection([
        ('A+', 'A+'), ('A-', 'A-'), 
        ('B+', 'B+'), ('B-', 'B-'), 
        ('O+', 'O+'), ('O-', 'O-'), 
        ('AB+', 'AB+'), ('AB-', 'AB-')
    ], string='Blood Group')

    # Next of Kin
    next_of_kin_name = fields.Char(string="Next of Kin", tracking=True)
    next_of_kin_contact = fields.Char(string="Next of Kin Phone Number", tracking=True)
    relationship_with_next_of_kin = fields.Char(string="Relationship with Next of Kin")
    next_appointment_date = fields.Date(string='Next Appointment Date')
    
    # Identification and Insurance
    identification_number = fields.Char(string="National ID")
    passport_number = fields.Char(string="Passport Number")
    insurance = fields.Selection([('yes', 'Yes'), ('no', 'No')], string='Are you insured?', tracking=True)
    insurance_provider = fields.Char(string="Insurance Provider")
    insurance_number = fields.Char(string="Insurance Number")

    # Medical Information
    weight = fields.Float(string="Weight (kg)", tracking=True)
    height = fields.Float(string="Height (cm)")
    body_mass_index = fields.Float(string="BMI", compute='_compute_bmi')
    blood_pressure = fields.Char(string="Blood Pressure")
    allergies = fields.Text(string="Allergies")
    chronic_diseases = fields.Text(string="Chronic Diseases")
    medical_history = fields.Text(string="Medical History")
    medications = fields.Text(string="Current Medications")
    last_visit_date = fields.Date(string="Last Visit Date")

    # Additional Fields
    emergency_contact_name = fields.Char(string="Emergency Contact Name")
    emergency_contact_number = fields.Char(string="Emergency Contact Number")
    emergency_relationship = fields.Char(string="Emergency Relationship")
    marital_status = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed')
    ], string='Marital Status')
    occupation = fields.Char(string="Occupation")
    payment_method = fields.Selection([
        ('cash', 'Cash'),
        ('insurance', 'Insurance'),
        ('credit_card', 'Credit Card')
    ], string='Payment Method')

    # System Fields
    ref = fields.Char(string="Reference", required=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)
    date_registered = fields.Datetime(string="Date Registered", default=fields.Datetime.now)

    # Computed Fields
    @api.depends('weight', 'height')
    def _compute_bmi(self):
        for record in self:
            if record.weight and record.height and record.height > 0:
                record.body_mass_index = record.weight / ((record.height / 100) ** 2)
            else:
                record.body_mass_index = 0.0