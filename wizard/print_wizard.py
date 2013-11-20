from osv import fields, osv
import datetime

class obrt_pj_wiz(osv.Model):
    _name= 'obrt.pj.wiz'
    _inherit = 'obrt.pj'
    _columns = {
                'kpr_ids':fields.many2many('promet.print.wizard','com_kpr_rel','kpr_ids','pj_ids')
                }

class print_wizard(osv.TransientModel):
    _name = 'promet.print.wizard'
    
    _columns = {'start_date':fields.date('Pocetni datum'),
                'end_date':fields.date('Zavrsni datum'),
                'pj_id':fields.many2one('obrt.pj','Poslovna jedinica'),
                'pj_ids':fields.many2many('obrt.pj.wiz','com_kpr_rel','pj_ids','kpr_ids','Poslovne jedinice za izvjestaj')
                }


    def prepare_data(self, cr, uid, ids, start_date, end_date, pj_ids, context=None):
        kpr = self.pool.get('obrt.kpr')
        kpr_obj = kpr.search(cr,uid,)
        import pdb;pdb.set_trace()
        res = {}
        return res
        
    def print_report(self, cr, uid, ids, start_date, end_date, pj_ids, context=None):
        if context is None:
            context = {}
        res = {}
        return {
                'type' : 'ir.actions.report.xml',
                'report_name' : 'obrt.kpr',
                'res' : res,
                }
        