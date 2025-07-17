from odoo import models, fields

class Student(models.Model):
    _name = 'student.management.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)

    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    email = fields.Char(string='Email')
