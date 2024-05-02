# Copyright 2020 Tecnativa - David Vidal
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)
from odoo import  api, fields, models


class WebsiteExtend(models.Model):
    _inherit = "website"

    #Slider 1 Portada
    slider_1_status = fields.Boolean(
        string='Activar',
    )
    slider_1_title = fields.Char(string='Titulo Superior',)
    slider_1_subtitle = fields.Char(string='Subtitulo',)
    slider_1_extra_text = fields.Char(string='Texto Adicional',)
    slider_1_banner_image = fields.Binary(
        string='Imagen de Fondo (1920x800)',
    )
    slider_1_button = fields.Char(string='Titulo Botón',)
    slider_1_url = fields.Char(string='Url',)

    #Slider 2 Portada
    slider_2_status = fields.Boolean(
        string='Activar',
    )
    slider_2_title = fields.Char(string='Titulo Superior',)
    slider_2_subtitle = fields.Char(string='Subtitulo',)
    slider_2_extra_text = fields.Char(string='Texto Adicional',)
    slider_2_banner_image = fields.Binary(
        string='Imagen de Fondo (1920x800)',
    )
    slider_2_button = fields.Char(string='Titulo Botón',)
    slider_2_url = fields.Char(string='Url',)


    #Banner Central
    central_banner_title = fields.Char(string='Titulo Banner Central',)
    central_banner_subtitle = fields.Char(string='Subtitulo Banner Central',)
    central_banner_desc = fields.Char(string='Descripción Banner Central',)
    central_banner_image = fields.Binary(
        string='Imagen de Banner (1800x600)',
    )
    central_banner_button = fields.Char(string='Titulo Botón',)
    central_banner_url = fields.Char(string='Url',)
