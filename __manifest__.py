# -*- coding: utf-8 -*-

{
    "name": "Hospital Management",
    "summary": "Manage Patient Appointment Workflow", 
    "author": "We",
    "license": "AGPL-3",
    "category": "Uncategorized",
    "website": "https://github.com/datalytiks",
    "version": "17.0.1.0",
    "depends": ['base','mail'],
    "data":[
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        'views/menu_items.xml',
    ],
    "application": True,
    "installable": True,
}

