{
    'name': "Agua de Azahar Format",
    'version': '17.0.1.0.0',
    'summary': "Formatos personalizados para Agua de Azahar",
    'description': """
        Módulo que contiene formatos personalizados para Agua de Azahar:
        - Factura con datos bancarios
        - Factura, ordenes y albaranes con referencia de cliente
    """,
    'author': "José Aguilar",
    'website': "https://www.xtendoo.es",
    'category': 'Customizations',
    'depends': [
        'base',
        'account',
        'sale',
        'stock',
    ],
    'data': [
        'views/report_invoice_bankacc.xml',
        'views/report_invoice_client_reference.xml',
        'views/report_invoice_quantity.xml',
        'views/report_proforma_quantity.xml',
        'views/report_stock_quantity.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
