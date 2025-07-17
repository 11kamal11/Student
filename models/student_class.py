from odoo import models, fields

class StudentClass(models.Model):
    _name = 'student.management.class'
    _description = 'Class'

    name = fields.Char(string='Class Name', required=True)
    code = fields.Char(string='Class Code', required=True)
