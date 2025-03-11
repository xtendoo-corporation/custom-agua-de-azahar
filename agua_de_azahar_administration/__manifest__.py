# __manifest__.py
{
    "name": "Agua de Azahar Administration",
    "summary": "Customizations for Agua de Azahar administration",
    "version": "1.0.0",
    "author": "Abraham (Xtendoo)",
    "license": "AGPL-3",
    "website": "",
    "category": "Administration",
    "depends": ["account",
                "sale",
                "web",
                ],
    "data": [
        "views/report_invoice_inherit.xml",
        "views/report_sale_inherit.xml",
        "views/report_templates.xml",
        "views/report_delivery_document.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
