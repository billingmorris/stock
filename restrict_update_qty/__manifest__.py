{
    'name': 'Restrict Update Quantities',
    'version': '14.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Restrict users from using the "Update Quantities" button',
    'description': 'This module restricts users from updating product quantities in product.template and product.product models.',
    'author': 'Bill Morris',
    'depends': ['stock'],
    'data': [
        'security/security.xml',
        'views/product_views.xml',
    ],
    'installable': True,
    'application': False,
}
