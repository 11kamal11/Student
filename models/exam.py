from odoo import fields, models

class StudentExam(models.Model):
    _name = 'student.exam'
    _description = 'Student Exam'

    name = fields.Char(string='Exam Name', required=True)
    course_id = fields.Many2one('course', string='Course')
    exam_date = fields.Date(string='Exam Date')

class StudentExamResult(models.Model):
    _name = 'student.exam.result'
    _description = 'Student Exam Result'

    exam_id = fields.Many2one('student.exam', string='Exam')
    student_id = fields.Many2one('res.partner', string='Student')
    marks_obtained = fields.Float(string='Marks Obtained')
    max_marks = fields.Float(string='Maximum Marks')