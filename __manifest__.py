# -*- coding: utf-8 -*-
{
    'name': "filtro_clientes",

    'summary': """ """,

    'description': """
        Filtro realizado para mostrar clientes que pertenezcan a la compañia actual
        que se encuentra el usuario.
    """,

    'author': "Katya Guadalupe Salas Rodríguez",
    'website': "http://www.cuartoangulo.com/",

    'category': 'sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}