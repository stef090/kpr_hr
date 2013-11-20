from osv import fields, osv
import datetime


class print_wizard(osv.TransientModel):
    _name = 'promet.print.wizard'
    
    _columns = {'start_date':fields.date('Pocetni datum'),
                'end_date':fields.date('Zavrsni datum'),
                'pj_id':fields.many2one('obrt.pj','Poslovna jedinica')
                }


    def prepare_data(self, cr, uid, ids, start_date, end_date, pj_id, context=None):
        kpr = self.pool.get('obrt.kpr')
        import pdb;pdb.set_trace()
        kpr_obj = kpr.browse(self,cr,uid,ids,context)
        res = {}
        for payment in kpr_obj:
            if start_date < payment.date < end_date:
                res['id'] = payment.id
        return res
            
            
        
        
    def print_report(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        res = {}
        return {
                'type' : 'ir.actions.report.xml',
                'report_name' : 'obrt.kpr',
                'res' : res,
                }
        