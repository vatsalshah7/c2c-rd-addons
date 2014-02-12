# -*- coding: utf-8 -*-
##############################################
#
# Swing Entwicklung betrieblicher Informationssysteme GmbH
# (<http://www.swing-system.com>)
# Copyright (C) ChriCar Beteiligungs- und Beratungs- GmbH
# all rights reserved
#    31-DEC-2012 (GK) created
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsibility of assessing all potential
# consequences resulting from its eventual inadequacies and bugs.
# End users who are looking for a ready-to-use solution with commercial
# guarantees and support are strongly advised to contract a Free Software
# Service Company.
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/> or
# write to the Free Software Foundation, Inc.,
# 59 Temple Place - Suite 330, Boston, MA  02111-1.17, USA.
#
###############################################
from openerp.osv import fields, osv

class invoice_ebInterface_installer(osv.osv_memory):
    _name    = 'account.invoice.ebinterface.installer'
    _inherit = 'res.config.installer'

    def execute(self, cr, uid, ids, context=None):
        self.execute_simple(cr, uid, ids, context)
        super(invoice_ebInterface_installer, self).execute(cr, uid, ids, context=context)
    # end def execute

    def execute_simple(self, cr, uid, ids, context=None) :
        inv_obj = self.pool.get('account.invoice')
        inv_ids = inv_obj.search(cr, uid, [("state", "in", ("open", "paid"))])
        inv_obj.generate_ebInterface(cr , uid, inv_ids, context=context)
    # end def execute_simple
# end class invoice_ebInterface_installer
invoice_ebInterface_installer()
