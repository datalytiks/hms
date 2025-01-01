# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    # _inherit = ['mail.thread']
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Patient Record'
    
    name = fields.Char(string='Patient Name', required=True)
    patient_age = fields.Integer(string='Age')
    age_group = fields.Selection([('major', 'Major'),('minor', 'Minor'),], string="Age Group", compute='set_age_group', store=True)
    notes = fields.Text(string="Notes")
    image = fields.Binary(string="Image")
    phone_number = fields.Char(string="Contact Number", required=True)
    email_id = fields.Char(string="Email")
    patient_id = fields.Integer(string='Patient ID', readonly=True, required=True, default=lambda self: self._get_next_patient_id())
    gender = fields.Selection([('male', 'Male'),('fe_male', 'Female'),], default='male', string="Gender")
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user.id, readonly=True)

    @api.model
    def _get_next_patient_id(self):
        # Fetch the next sequence value or the next integer value
        last_patient = self.search([], order='patient_id desc', limit=1)
        return (last_patient.patient_id or 0) + 1
    
    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age:
                if rec.patient_age < 18:
                    rec.age_group = 'minor'
                else:
                    rec.age_group = 'major'

    @api.constrains('phone_number')
    def _check_phone_number(self):
        """
        Enforce validation for phone numbers to ensure correctness.
        Adjust the regex based on the preferred format.
        """
        phone_regex = re.compile(r'^\+?1?\d{8,12}$')
        for record in self:
            if record.phone_number and not phone_regex.match(record.phone_number):
                raise ValidationError("Please enter a valid phone number (8-12 digits, optionally prefixed with +).")
    
    


