from odoo import fields, models, api,_
from odoo.exceptions import UserError, AccessError

class AccountMove(models.Model):
    _inherit = "account.move"
    customer_po = fields.Char(string="Customer PO")
    customer_podate = fields.Date(string="Customer PO-Date")


class StockPicking(models.Model):
    _inherit = 'stock.picking'
    customer_po = fields.Char(string="Customer PO")
    customer_podate = fields.Date(string="Customer PO-Date")


class SaleOrder(models.Model):
    _inherit = "sale.order"
    customer_po = fields.Char(string="Customer PO")
    customer_podate = fields.Date(string="Customer PO-Date")

    def _action_confirm(self):
        res = super()._action_confirm()
        for each_pick in self.picking_ids:
            each_pick.customer_po=self.customer_po
            each_pick.customer_podate=self.customer_podate
        return res


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def create_invoices(self):
        res = super().create_invoices()
        sale_orders = self.env['sale.order'].browse(self._context.get('active_ids', []))
        for sale in sale_orders:
            for inv in sale.invoice_ids:
                inv.customer_po = sale.customer_po
                inv.customer_podate = sale.customer_podate
        return res

