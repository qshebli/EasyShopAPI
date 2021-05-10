from flask import current_app as app
from .User import bp as usersController
from .Carts import bp as cartsController
from .Products import bp as productsController
from .Auth import bp as authController

app.register_blueprint(usersController, url_prefix='/api/users')
app.register_blueprint(cartsController, url_prefix='/api/carts')
app.register_blueprint(productsController, url_prefix='/api/products')
app.register_blueprint(authController, url_prefix='/api/auth')