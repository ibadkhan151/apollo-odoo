# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PosDetails(models.TransientModel):
    _name = 'pos.details.wizard.fake'
    _description = 'Point of Sale Details Report Fake'

    def _default_start_date(self):
        """ Find the earliest start_date of the latests sessions """
        # restrict to configs available to the user
        config_ids = self.env['pos.config'].search([]).ids
        # exclude configs has not been opened for 2 days
        self.env.cr.execute("""
            SELECT
            max(start_at) as start,
            config_id
            FROM pos_session
            WHERE config_id = ANY(%s)
            AND start_at > (NOW() - INTERVAL '2 DAYS')
            GROUP BY config_id
        """, (config_ids,))
        latest_start_dates = [res['start'] for res in self.env.cr.dictfetchall()]
        # earliest of the latest sessions
        return latest_start_dates and min(latest_start_dates) or fields.Datetime.now()

    start_date = fields.Datetime(required=True, default=_default_start_date)
    end_date = fields.Datetime(required=True, default=fields.Datetime.now)
    pos_config_ids = fields.Many2many('pos.config', 'pos_detail_fake_configs',
        default=lambda s: s.env['pos.config'].search([]))

    @api.onchange('start_date')
    def _onchange_start_date(self):
        if self.start_date and self.end_date and self.end_date < self.start_date:
            self.end_date = self.start_date

    @api.onchange('end_date')
    def _onchange_end_date(self):
        if self.end_date and self.end_date < self.start_date:
            self.start_date = self.end_date

    def generate_report(self):
        data = {'date_start': self.start_date, 'date_stop': self.end_date, 'config_ids': self.pos_config_ids.ids}
        return self.env.ref('pos_fake_report.sale_details_report_fake').report_action([], data=data)

class ReportSaleDetails(models.AbstractModel):

    _inherit = 'report.point_of_sale.report_saledetails'
    _description = 'Point of Sale Details Fake'

    @api.model
    def _get_report_values(self, docids, data=None):
        data = super(ReportSaleDetails, self)._get_report_values(docids, data)
        if data['context']['active_model'] == 'pos.details.wizard.fake':
            data = self.understate_sales(data)
        return data

    @staticmethod
    def understate_sales(data):
        payments = []
        for payment in data['payments']:
            total = payment['total'] - payment['total'] * 30 / 100
            payment['total'] = total
            payments.append(payment)
        data['payments'] = payments

        products = []
        for product in data['products']:
            price_unit = product['price_unit'] - product['price_unit'] * 30 / 100
            product['price_unit'] = price_unit
            products.append(product)
        data['products'] = products

        taxes = []
        for tax in data['taxes']:
            base_amount = tax['base_amount'] - tax['base_amount'] * 30 / 100
            tax_amount = tax['tax_amount'] - tax['tax_amount'] * 30 / 100
            tax['base_amount'] = base_amount
            tax['tax_amount'] = tax_amount
            taxes.append(tax)
        data['taxes'] = taxes

        data['total_paid'] = data['total_paid'] - data['total_paid'] * 30 / 100
        return data
