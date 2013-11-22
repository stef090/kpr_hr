# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Module: l10n_hr_obrt
#    Author: Stjepan Lovasic
#    mail:   stjepan.lovasic@gmail.com
#    Copyright (C) 2013- Datacom d.o.o Zagreb
#    Contributions: 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from osv import fields, osv, orm
import time
from tools.translate import _
from lxml import etree


class obrt_kpr(osv.Model):
    _name='obrt.kpr'
    _description='Knjiga prometa'
    
    def _sum_cash_checks(self, cr, uid, ids, field_name, field_values, context=None):
        if len(ids) == 0 :
            return False
        res={}
        for kpr in self.browse(cr, uid, ids):
            res[kpr.id] = kpr.gotovina + kpr.cekovi 
        return res
    '''
    def _get_last_used_pj(self, cr, uid, context=None):
        cr.execute("SELECT MAX(id) FROM obrt_kpr")
        last_pr = cr.fetchone()[0]
        #pj=self.read(cr, uid, last_pr, ['pj_id'])
        #return pj['pj_id'][0]
        #B: skratio i vratio kao default
        return self.read(cr, uid, last_pr, ['pj_id'])['pj_id'][0]
       ''' 
        
    _columns = {
                'rbr':fields.integer('Red. broj'),
                'date':fields.date('Nadnevak',required=1),
                'temeljnica':fields.char('Broj temeljnice', size=64),
                'name':fields.char('Opis isprava o primicima u gotovini', size=64),
                'gotovina':fields.float('Iznos naplacen u gotovini',(16,2)),
                'cekovi':fields.float('Iznos naplacen u cekovima',(16,2)),
                'ukupno':fields.function( _sum_cash_checks, type="float", obj="obrt.kpr", method=True, store=True, string='Ukupno naplacen iznos'),
                'pj_id':fields.many2one('obrt.pj','Poslovna jedinica', required=1, ondelete='restrict'),
                }
    
    
    '''
    _defaults = {
                 'pj_id': _get_last_used_pj
                 }
    '''
    
    """
    def fields_view_get(cr, uid, view_id=None, view_type='form', context=None, toolbar = False, submenu=False):
        if context is None:
            context={}
        res = super(obrt_kpr,self).fields_view_get(cr, uid, view_id, view_type, context, toolbar, submenu)
        if context.get('type', False):
            doc=etree.XML(res['arch'])
            
        return res
    """
    
        
    def create(self, cr, uid, vals, context=None):
        if context is None:
            context = {}
        
        cr.execute("SELECT MAX(rbr) FROM obrt_kpr WHERE pj_id = " + str(vals['pj_id']))
        rbr = cr.fetchone()
        if rbr[0] is None:
            vals['rbr'] = 1
        else:
            vals['rbr'] = rbr[0] + 1
        
        return super(obrt_kpr, self).create(cr, uid, vals, context=context)
    
    def assert_check(self, ids):
        assert len(ids) == 1, "Dozvoljen jedan zapis!"
        return True
    
    def _check_closed_period(self, cr, uid, ids, context=None):
        self.assert_check(ids)
        period_obj = self.pool.get('obrt.period')
        closed_period_ids = period_obj.search(cr, uid, [('closed','=',True)])
        
        check = self.browse(cr, uid, ids[0], context=context)
        for period in period_obj.browse(cr, uid, closed_period_ids):
            if period.date_end > check.date : 
                return False
        return True
    
    
    
    def _check_last_date(self, cr, uid, ids, context=None):
        self.assert_check(ids)
        check = self.browse(cr, uid, ids[0], context=context)
        cr.execute("SELECT MAX(date) from obrt_kpr where pj_id = " + str(check.pj_id.id))
        cur_date = cr.fetchone()[0]
        
        return (check.date >= cur_date) or False
    
    def _check_sum(self, cr, uid, ids, context=None):
        self.assert_check(ids)
        check_sum = self.browse(cr, uid, ids[0], context)
        return check_sum.cekovi or check_sum.gotovina or False
    
    _constraints = [
                    (_check_closed_period,'Period za unešeni datum je zatvoren za unose.',['date']),
                    (_check_last_date,'Zapisi za pojedinu poslovnicu moraju biti kronoloski poredani,\n postoji zapis iz datuma kasnije od upisanog.',['date','pj_id']),
                    (_check_sum,'Promet ne može imati iznos 0!',['cekovi','gotovina'])
                    ]
    