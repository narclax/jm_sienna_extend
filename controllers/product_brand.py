from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import QueryURL, WebsiteSale

class CustomWebsiteSale(WebsiteSale):
    # Method to get the brands.
    @http.route(["/page/product_brands"], type="http", auth="public", website=True)
    def product_brands(self, **post):
        b_obj = request.env["product.brand"]
        domain = [("website_published", "=", True)]
        if post.get("search"):
            domain += [("name", "ilike", post.get("search"))]
        brand_rec = b_obj.sudo().search(domain,order="sequence")

        keep = QueryURL("/page/product_brands", brand_id=[])
        values = {"brand_rec": brand_rec, "keep": keep}
        if post.get("search"):
            values.update({"search": post.get("search")})
        return request.render("website_sale_product_brand.product_brands", values)