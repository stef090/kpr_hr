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

class obrt_period(osv.Model):
    
    _name='obrt.period'
    _description='Period knjige prometa'
    
    _columns={
              'name':fields.char("Naziv perioda", size=128),
              'date_start':fields.date('Pocetni datum'),
              'date_end':fields.date('Zavrsni datum'),
              'closed':fields.boolean('Period zatvoren')
              }