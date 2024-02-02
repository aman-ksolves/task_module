from odoo import models, fields


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    task_id = fields.Many2one('project.task', readonly=True)

    def save_manually(self):
        return True


class ProjectTaskInherit(models.Model):
    _inherit = 'project.task'

    sale_order_ids = fields.One2many('sale.order', 'task_id')

    def open_so_wiz(self):
        return {
            'view_mode': 'form',
            'res_model': 'sale.order',
            'views': [[False, 'form']],
            'target': 'new',
            'type': 'ir.actions.act_window',
        }