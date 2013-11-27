from osv import fields, osv, orm
import time
from tools.translate import _ 
from lxml import etree


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
                'kpr_ids':fields.one2many('obrt.kpr','pj_id','Zapisi knjige prometa')
                }
    
    #_sql_constraints = [
    #                    ('name_uniq', 'unique (name)', """Naziv mora biti jedinstven!"""),
    #                    ]
    def get_all_pj(self, cr,  uid, context):
        res=[]
        pj_obj=self.pool.get('obrt.pj')
        for p in pj_obj.browse(cr, uid, pj_obj.search(cr, uid, [])):
            dic = {}
            dic['id']=p.id
            dic['name']=p.name
            res.append(dic)
        return res
    
    
    
    
    def add_search_pj(self, cr, uid, pj_name, pj_id, context=None):
        pj_list = self.get_all_pj(cr, uid, context)
        
        view_obj = self.pool.get('ir.ui.view')
        filter_id = view_obj.search(cr, uid, [('type','=','search'),('model','=','obrt.kpr')], context=context)
        filter_view = view_obj.read(cr, uid, filter_id,['arch'])
        doc=etree.XML(filter_view[0]['arch'])
        nova_pj = etree.Element("field", filter_domain="[('pj_id','='," + str(pj_id) + ")]", name=pj_name)
        doc.insert(0,nova_pj)
        doc_root= doc.getroottree()
        view_obj.write(cr, uid, filter_id, {'arch':etree.tostring(doc_root)})
        return True
    
    def construct_new_search_xml(self, cr, uid, context=None):
        if context is None:
            context={}
        xml_form = etree.Element('search', {'string': 'Pretraga knjige prometa'})
        
        xml_group= etree.SubElement(xml_form, 'field', 
                            {'name':'name', 'filter_domain':"['|',('name','ilike',self),('pj_id','ilike',self)]"})
         
        for pos_jed in self.get_all_pj(cr, uid, context) :
            xml_group= etree.SubElement(xml_form, 'field', {'name':pos_jed['name'],
                             'filter_domain':"[('pj_id','='," + str(pos_jed['id']) + ")]"})
        
        xml_groupby = etree.SubElement(xml_form,'group',
                            {'string':'Group by...', 'expand':"0"})
        # BOLE Mozda da dodamo i group by period?
        etree.SubElement(xml_groupby, 'filter',
                            {'string':'Poslovna jedinica',
                             'context':"{'group_by':'pj_id'}"})
        root = xml_form.getroottree()
        res = etree.tostring(root)
        return res
    '''
    def create(self, cr, uid, vals, context=None):
        if context == None : 
            context={}
        res = super(obrt_pj, self).create(cr, uid, vals, context=context)
        #new_search_xml = self.construct_new_search_xml(cr, uid, context)
        #self.add_search_pj(cr, uid, vals['name'], res)
        #view_obj = self.pool.get('ir.ui.view')
        #filter_id = view_obj.search(cr, uid, [('type','=','search'),('model','=','obrt.kpr')], context=context)
        #new_search_xml= '<?xml version="1.0"?>' + new_search_xml
        #view_obj.write(cr, uid, filter_id, {'arch':new_search_xml})
        return res
    '''