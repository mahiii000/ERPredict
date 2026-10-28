from odoo import fields, models


class ErpredictSales(models.Model):
    _name = "erpredict.sales"
    _description = "ERPredict Sales"

    name = fields.Char(required=True)
