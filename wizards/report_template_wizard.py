from odoo import models, fields, api, _
import odoo.addons.decimal_precision as dp
from datetime import datetime, timedelta
from odoo.exceptions import UserError


class ReportTemplateWizard(models.TransientModel):
    _name = 'report.template.wizard'

    from_date = fields.Date('Start Date')
    to_date = fields.Date('End Date')
    

    def print_report(self):
        temp_data = self.env['report.template.data'].sudo().search([])
        company_id = self.env.company
        domain = [('company_id','=',company_id.id)]
        if self.from_date:
            domain.append(('create_date','>=',self.from_date))
        if self.to_date:
            domain.append(('create_date','<=',self.to_date))
        
        recs = self.env['my.model.name'].search(domain)
        print("recs",recs)
        
        if len(temp_data) > 0:
            temp_data.unlink()
            
        for rec in recs:
            self.env['report.template.data'].sudo().create({
                'name': rec.name,
            })

        docids = self.env['report.template.data'].search([])
        print("docids",docids)
        if len(docids)>0:
            return self.env.ref('report_template.report_template_sample').report_action(docids)
        else:
            raise UserError("No Record Found")       
