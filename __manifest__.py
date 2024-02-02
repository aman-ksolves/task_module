{
    'name': 'Task Module',
    'version': '1.0',
    'author': 'Aman',
    'depends': ['base', 'project', 'sale'],

    'description': 'A simple Odoo module with Project task.',
    'data': [
        'views/project_task_from_view.xml',
        'views/sale_order_inherit_form_view.xml',

    ],
    'application': True,

}
