from odoo import fields, models
from datetime import date

class Installment(models.Model):
    _name = 'installment.installment'

    name = fields.Char("Name")
    reference = fields.Char("Reference")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('paid', 'Paid')
    ], string="State", default='draft')
    date = fields.Date(string='Date', default=date.today())
    customer = fields.Many2one(string='Customer', required=True)
    journal = fields.Many2one(string='Journal', required=True)
    account = fields.Many2one(string='Account', required=True)
    analytic_account = fields.Many2one(string='Analytic account')
    analytic_tags = fields.Many2one(string='Analytic tags')
    amount = fields.Float(string='Amount', required=True, positive=True)
    note = fields.Text(string='Note')


