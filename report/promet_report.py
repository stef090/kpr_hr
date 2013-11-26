# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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

import time
import datetime
from report import report_sxw

class obrt_kpr(report_sxw.rml_parse):
    
    def format_date(self, date):
        cur_format = "%Y-%m-%d"
        new_format = "%d.%m.%Y"
        date_tuple = datetime.datetime.strptime(date, cur_format)
        return date_tuple.strftime(new_format)
    
    def __init__(self, cr, uid, datas, context):
        super(obrt_kpr, self).__init__(cr, uid, datas, context=context)
        self.localcontext.update({
            'time': time,
            'format_date': self.format_date
        })
        
        
    def prepare_list(self,list_pj):
        list_pj.sort(key=lambda x: x.id, reverse=False)
        return list_pj
    
    
        
        
report_sxw.report_sxw(
    'report.obrt.kpr',
    'obrt.kpr',
    'l10n_hr_obrt/obrt_kpr/report/promet_report.rml',
    parser=obrt_kpr,
    header = False
)
