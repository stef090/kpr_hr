# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Module: datacom_obrt
#    Author: Stjepan Lovasic
#    mail:   stjepan.lovasic@gmail.com
#    Copyright (C) 
#    Contributions: 
#                   
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
{
    "name" : "Obrt - KPR",
     "version" : "0.1",
    "author" : "Datacom",
    "description" : """
Knjiga prometa za obrtnike
==========================

Author: Stjepan Lovasic stjepan.lovasic@gmail.com

Contributions: 
Summary: 

Modul daje funkcionalnost knjige prometa 
prema u racunovodstvu u RH. Namijenjeno obrtnicima.

""",
   
    "category" : "Accounting",
    'depends': [],
    'update_xml': [
                   'res_company_view.xml',
                   'kpr_view.xml',
                   'period_view.xml',
                   'nkd_data.xml',
                   'period_data.xml',
                   'wizard/period_closure_wizard_view.xml',
                   #'wizard/kpr_print_wizard_view.xml',
                   'wizard/pj_select_wizz_view.xml',
                   'report/promet_report_view.xml',
                   ],
    "active": False,
    "installable": True,
}