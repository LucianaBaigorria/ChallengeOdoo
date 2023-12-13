# -*- coding: utf-8 -*-
{
    "name": "primer_challenge",
    'summary':"""
    modulos de inscripcion y programas de alumnos
    """,
    'author': "luciana",
    'category': 'educacion',
    'version': '1.0',
    'depends':[],
    'data':[
        'views/menu_view.xml',
        'views/alumno_view.xml',
        'views/inscripcion_view.xml',
        'views/programa_view.xml',
        'security/listado_security.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'aplication':True,
}

#En el manifest se declaran todas las librerias, data, vistas para que el modulo funcione