from odoo import models, fields, api

class Attendance(models.Model):
    _name = 'student.attendance'
    _description = 'Student Attendance'

    student_id = fields.Many2one('student.management.student', string='Student', required=True)
    course_id = fields.Many2one('student.management.course', string='Course', required=True)
    attendance_date = fields.Date(string='Date', required=True, default=fields.Date.context_today)
    status = fields.Selection([
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('excused', 'Excused'),
    ], string='Status', default='present', required=True)
