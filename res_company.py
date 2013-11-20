from osv import fields, osv, orm
import time
from tools.translate import _ 

class res_company(osv.Model):
   
    _inherit = "res.company"
    
    _columns = {
                'nkd_id':fields.many2one('obrt.nkd','Naziv i kod djelatnosti'),
                'obrt_pj_ids':fields.one2many('obrt.pj','company_id','Poslovne jedinice')
                }
    

class obrt_nkd(osv.Model):
    _name = 'obrt.nkd'
    _description = 'NKD - Nacionalna klasifikacija djelatnosti'
    _columns = {
        'code': fields.char('Kod', size=16, required=True, select=1),
        'name': fields.char('Naziv', size=128, required=True),
    }
    


class obrt_pj(osv.Model):
    _name = 'obrt.pj'
    _description = 'Poslovna jedinica obrta'
    _columns = {
                'company_id':fields.many2one('res.company','Obrt'),
                'name':fields.char('Naziv'),
                'adresa':fields.char('Adresa'),
                'kpr_ids':fields.one2many('obrt.kpr','pj_ids','Zapisi knjige prometa')
                
            }
    
        
        
