# -*- coding: utf-8 -*-
###############################################################################
#
#    OpenEduCat Inc
#    Copyright (C) 2009-TODAY OpenEduCat Inc(<https://www.openeducat.org>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from odoo import models, fields,api,_
from odoo.exceptions import ValidationError


class OpFacilityLine(models.Model):
    _inherit = "op.facility.line"

    classroom_id = fields.Many2one('op.classroom', 'Classroom')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            add=self.search([('facility_id','=',vals['facility_id']),
                             ('classroom_id','=',vals['classroom_id'])])
            if add :
                raise ValidationError(
                        _("Facility name exists. Please choose a unique name or update the quantity."))
        return super(OpFacilityLine, self).create(vals_list)