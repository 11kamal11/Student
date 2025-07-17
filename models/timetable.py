from odoo import models, fields, api

class Timetable(models.Model):
    _name = 'student.timetable'
    _description = 'Timetable'

    course_id = fields.Many2one('student.management.course', string='Course', required=True)
    day = fields.Selection([
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ], string='Day', required=True)
    start_time = fields.Float(string='Start Time', required=True)
    end_time = fields.Float(string='End Time', required=True)
    classroom = fields.Char(string='Classroom')
