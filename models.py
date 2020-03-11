 # -*- coding: utf-8 -*-

from odoo import models, fields

# class openacademy(models.Model):
#     _name = 'openacademy.openacademy'

#     name = fields.Char()
class MinimalModel(models.Model):
    _name = 'openacademy.course'
    _description = "OpenAcademy Course"
    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    instructor_id = fields.Many2many('res.partner', string="Instructor")
    course_id = fields.Many2one('university', ondelete='cascade', string="Course", required=True)
    # attendees_registration = fields.Many2one('openacademy.course', ondelete='cascade', string="Course", required=True)
    product_status = fields.Selection(
        string='Communication',
        selection=[
            ('created', 'Choise 1'),
            ('inprogress', 'Choise 2'),
            ('done', 'Choise 3'),
        ],
        default='created',
    )


    def prev_status(self):
        if self.product_status == 'created':
            self.product_status = 'inprogress'
        elif self.product_status == 'inprogress':
            self.product_status = 'done'

    def next_status(self):
        if self.product_status == 'inprogress':
            self.product_status = 'created'
        elif self.product_status == 'done':
            self.product_status = 'inprogress'


class University(models.Model):
    _name = 'university'
    description = fields.Text(string="Title", required=True)


class Student(models.Model):
    _name = 'student'
    description = fields.Text(string="Title", required=True)

    def prev_status(self):
        if self.product_status == 'created':
            self.product_status = 'inprogress'
        elif self.product_status == 'inprogress':
            self.product_status = 'done'

    def next_status(self):
        if self.product_status == 'inprogress':
            self.product_status = 'created'
        elif self.product_status == 'done':
            self.product_status = 'inprogress'



class DateNow(models.Model):
    _name = 'datenow'
    name = fields.Char(string="Title", required=True)
    start_date = fields.Datetime(readonly=True)
    # datenow = fields.Datetime()
    calculated_date = fields.Char(readonly=True)
    stop_status = fields.Char(string="дата начала работы", required=True)
    time_id = fields.One2many('job', "time_id", string="Job_now")

    def time_at_this_moment(self):
        if not self.start_date:
            self.start_date = fields.Datetime.now()
        else:
            time = fields.Datetime.now()
            self.calculated_date = time - self.start_date


class Job(models.Model):
    _name = 'job'
    description = fields.Many2one('datenow', string="Job_now")
    time_id = fields.Many2one('datenow',
        ondelete='cascade', string="Time", required=True)


    # def time_stop(self):
    #     if self.start_status == 'created'
    #        self.stop_status = 'inprogress'
    #     else:
    #         self.start_status == 'inprogress'
    #         self.stop_status = 'done'

