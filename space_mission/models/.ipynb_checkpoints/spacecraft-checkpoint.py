# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spacecraft(models.Model):
    _name = 'space_mission.spacecraft'
    _description = 'Sapce Mission Spacecraft'
    
    name = fields.Char(string='Spacecraft Name', required = True)
    model = fields.Char(string='Spacecraft Model', required = True)
    type = fields.Selection(string='Spacecraft Type',
                           selection=[('passengers', 'Passengers'),
                                     ('star_destroyer', 'Star Destroyer'),
                                     ('star_cruiser', 'Star Cruiser')],
                            copy = False
                           )
    fuel_type = fields.Selection(string='Fuel Type',
                                selection=[('conventional', 'Vonventional'),
                                          ('nuclear', 'Nuclear'),
                                          ('solar', 'Solar')],
                                copy = False
                                )
    passenger_capacity = fields.Integer(string='Passenger Capacity')
    length = fields.Float(string='Ship Length')
    width = fields.Float(string='Ship Width')
    height = fields.Float(string='Ship Height')
    weight = fields.Float(string='Ship Weight')
    active = fields.Boolean(string='Active?', default = True)
    
    
    