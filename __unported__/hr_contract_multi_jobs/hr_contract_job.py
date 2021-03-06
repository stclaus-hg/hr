# -*- coding:utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Savoir-faire Linux. All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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

from openerp.osv import fields, orm


class hr_contract_job(orm.Model):
    """
    An instance of a job position for an employee's contract.

    This model may look trivial for now, but the purpose is that other modules
    add fields to it, e.g. a salary class or a wage scale. These are fields
    that depend on both the contract and the job position.
    """
    _name = 'hr.contract.job'
    _description = 'Relational object between contract and job'

    _columns = {
        'name': fields.related(
            'job_id',
            'name',
            string='Job',
        ),
        'job_id': fields.many2one(
            'hr.job',
            'Job',
            required=True,
            ondelete='cascade',
        ),
        'contract_id': fields.many2one(
            'hr.contract',
            'Contract',
            required=True,
            ondelete='cascade',
        ),
        'is_main_job': fields.boolean(
            'Main Job Position'
        ),
    }
