# -*- coding: utf-8 -*-
# author : ovalue/addi ait-mlouk
{
    'name': 'Axo Top Media',
    'version': '1.0',
    'author': 'Ovalue/Ait-Mlouk Addi',
    'website': 'http://www.ovalue.net/',
    'complexity': 'easy',
    'sequence': 1,
    'category': 'sale',
    'description': """
        Put your description here for your module:
            - model1
            - model2
            - model3
    """,
    'depends': ['base','mail','sale','account','purchase','account_asset'],
    'summary': 'sale, purchase',
    'data': [
        'views/axo_views.xml',
        'views/axo_inherit.xml',
        'data/sequence.xml',
        'report/sale_report.xml',
        'report/sale_report_print_pro.xml',
        'report/sale_report_pro.xml',
        'report/report.xml',
        'report/sale_report_print_comm.xml',
        'report/report_invoice_print.xml',
        'report/sale_report_print.xml',
        'report/report_invoice.xml',
        'report/purchase_order_templates.xml',
        'report/purchase_supp_order_templates.xml',
        'report/report_footer.xml',
        'menu.xml',
    ],
    
    'css': [
        #'static/src/css/ModuleName_style.css'
    ],
    
    'installable': True,
    'application': True,
}
