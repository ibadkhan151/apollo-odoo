# -*- coding: utf-8 -*-


from odoo import fields, models,tools,api

class pos_config(models.Model):
    _inherit = 'pos.config' 
    
    allow_pos_fake_report = fields.Boolean("Allow Pos Fake Report")
    pos_fake_report_percentage = fields.Float("Understated Percentage")
    pos_fake_report_days = fields.Selection([('Monday', 'Monday'),
                                             ('Tuesday', 'Tuesday'),
                                             ('Wednesday', 'Wednesday'),
                                             ('Thursday', 'Thursday'),
                                             ('Friday', 'Friday'),
                                             ('Saturday', 'Saturday'),
                                             ('Sunday', 'Sunday')], string='Fake Report Days')

    


