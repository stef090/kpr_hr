from osv import fields, osv
import datetime

class period_closure_wizard(osv.TransientModel):
    _name = "period.closure.wizard"
    
    def _get_periods(self, cr, uid, context=None):
        
        res = []
        p_obj = self.pool.get('obrt.period')
        for period in p_obj.browse(cr,uid,p_obj.search(cr, uid, [('closed','!=','True')])):
            res.append((period.id, period.name))
        return res
    
    _columns = {
                'period_ids':fields.selection(_get_periods,'Periodi')
                }
    
    def close_period(self, cr, uid, period, context=None):
        self.pool.get('obrt.period').write(cr, uid, period, {'closed':'true'})
        view_ref = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'obrt_kpr', 'periodi_tree_view')
        view_id = view_ref and view_ref[1] or False
        return {
                'type': 'ir.actions.act_window',
                'name': 'Period knjige prometa',
                'res_model': 'obrt.period',
                'view_type': 'tree',
                'view_mode': 'tree',
                'view_id': view_id,
                'target': 'current',
                'nodestroy': True,
                }
    