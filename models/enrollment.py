from odoo import models, fields

class Enrollment(models.Model):
    _name = 'student.management.enrollment'
    _description = 'Enrollment'

    student_id = fields.Many2one('student.management.student', string='Student', required=True)
    class_id = fields.Many2one('student.management.class', string='Class', required=True)
    enrollment_date = fields.Date(string='Enrollment Date', required=True)

