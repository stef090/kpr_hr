from osv import fields, osv
import datetime



class wizz_pj_sel(osv.osv_memory):
    _name='wizz.pj.sel'
    
    def _get_jedinice(self, cr, uid, context=None):
        if context is None:
            context = {}
        res = []
        pj_obj = self.pool.get('obrt.pj')
        for pj in pj_obj.browse(cr, uid, pj_obj.search(cr, uid, [])):
            res.append((pj.id, pj.name))
        return res
    
    _columns = {
                'naziv':fields.selection(_get_jedinice,'Odabir poslovne jedinice'),
               # 'date_start':fields.date('Pocetni datum'),
               # 'date_end':fields.date('Zavrsni datum'),
               # 'kpr_ids':fields.one2many('obrt.kpr','id')
                }
    
    def open_selected(self, cr, uid, ids,  context=None):
        if context is None:
            context = {}
        
        view_ref = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'obrt_kpr', 'knjiga_prometa_form_view_pj')
        view_id = view_ref and view_ref[1] or False
        res_id=int(self.read(cr, uid, ids[0])['naziv'])
        return {
                'type': 'ir.actions.act_window',
                'name': 'KPR / PJ',
                'res_model': 'obrt.pj',
                'res_id': res_id,
                'view_type': 'form,tree',
                'view_mode': 'form',
                'view_id': view_id,
                'target': 'current',
                'nodestroy': False,
                }
        
wizz_pj_sel()
        