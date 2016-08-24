from system.core.router import routes

routes['default_controller'] = 'Products'
routes['GET']['/products'] = 'Products#index'
routes['GET']['/products/new'] = 'Products#new'
routes['GET']['/products/edit/<int:id>'] = 'Products#edit'
routes['GET']['/products/show/<int:id>'] = 'Products#show'
routes['POST']['/products/create'] = 'Products#create'
routes['POST']['/products/update/<int:id>'] = 'Products#update'
routes['POST']['/products/destroy/<int:id>'] = 'Products#destroy'

