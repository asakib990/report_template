from odoo import models, fields, api, _
import odoo.addons.decimal_precision as dp
from datetime import datetime, timedelta
from odoo.exceptions import UserError


class ReportTemplateData(models.TransientModel):
    _name = 'report.template.data'
    _description = 'Report Template Data'

    name = fields.Char('Name')