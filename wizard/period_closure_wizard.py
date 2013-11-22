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
        pass
        return self.pool.get('obrt.period').write(cr, uid, period, {'closed':'true'})
    