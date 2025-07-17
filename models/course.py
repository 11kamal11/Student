from odoo import models, fields

class StudentCourse(models.Model):
    _name = 'student.management.course' 
    _description = 'Course'

    name = fields.Char(string='Course Name', required=True)
    code = fields.Char(string='Course Code', required=True)
    description = fields.Text(string='Description')

