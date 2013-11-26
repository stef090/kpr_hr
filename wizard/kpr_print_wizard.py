from osv import fields, osv
import datetime

'''
class obrt_pj_wiz(osv.osv_memory):
    _inherit = "obrt.pj"
    _name = "obrt.pj.wiz"
    _columns = {
                'kpr_id':fields.many2one('kpr.obrt.pj')
                }
'''
class kpr_obrt_pj(osv.osv_memory):
    
    #_inherit="obrt.pj"
    _name="kpr.obrt.pj"
    
    def _get_pj(self, cr, uid, context=None):
        
        res = []
        pj_obj = self.pool.get('obrt.pj')
        for pj in pj_obj.browse(cr,uid,pj_obj.search(cr, uid, [])):
            res.append((pj.id, pj.name))
        return res
    
    _columns = {
                'date_start':fields.date('Pocetni datum'),
                'date_end':fields.date('Zavrsni datum'),
                #'pj_ids':fields.selection(_get_pj, 'Poslovne jedinice')
                }
    
    def kpr_print(self, cr, uid, date_start, date_end, pj_ids=None, context=None):
        if pj_ids == None:
            pj_ids = self.pool.get('obrt.pj').search(cr, uid, [])
        if isinstance(pj_ids,int):
            pj_ids = [pj_ids]
        
        return True
    
        
        