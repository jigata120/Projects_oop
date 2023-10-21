# Marketplace App - README

## Overview

Welcome to the README for the Marketplace App. This Django-based marketplace application allows users to buy and sell various items. The codebase includes views and functions to manage products, the user cart, user registration, login, and logout functionalities, and other essential features.

## Functionality

Below is an overview of the key functionalities and views provided by this application:

### Filter Products by Price

- `filter_products_by_price(request)`: Filters products by a price range specified by the user. Handles various scenarios, such as when both minimum and maximum prices are not provided. Redirects to the home page with applied filters.

### Edit Product

- `edit_product(request, product_id)`: Allows users to edit product details. Validates the form and saves the updated product. Redirects to the home page.

### Delete Product from Cart

- `delete_product_from_cart(request, product_id)`: Removes a product from the user's cart. Increments the product's quantity and saves it. Redirects to the home page.

### Custom 404 Page

- `custom_404_view(request, exception)`: A custom view to handle 404 (Page Not Found) errors. Renders a custom 404 page.

### Delete Product

- `delete_product(request, product_id)`: Deletes a product from the marketplace. Redirects to the home page.

### Add Product to Cart

- `add_to_cart(request, product_id)`: Adds a product to the user's cart. Decrements the product's quantity and saves it. Updates the cart and redirects to the home page.

### Calculate Cart Price

- `cart_price(cart_objects)`: Calculates the total price of products in the cart.

### Create Product

- `create_product(request)`: Allows users to create a new product. Validates the form and saves the product. Redirects to the home page.

### Product Details

- `product_detail(request, product_id)`: Displays the details of a specific product.

### Home Page

- `home(request)`: Renders the home page, displaying a list of products. Calculates the total price of the user's cart.

### About Page

- `about(request)`: Renders a view providing information about the marketplace app.

### User Registration

- `register(request)`: Allows users to register by providing a username, password, and email. Creates a user and their cart. Redirects to the login page.

### User Login

- `login_user(request)`: Handles user login by authenticating the provided username and password. Redirects to the home page upon successful login.

### User Logout

- `logout_user(request)`: Logs the user out and redirects to the login page.

## Getting Started

To get started with the Marketplace App, follow these steps:

1. [Install Django](https://docs.djangoproject.com/en/3.2/topics/install/) if you haven't already.

2. Clone this repository to your local machine.

3. Set up your Django project and configure the necessary models, templates, forms, and user authentication.

4. Integrate the provided functions into your Django project to enable the described functionality.

5. Run your Django development server and navigate to the home page to explore the marketplace.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Your contributions are welcome!

## License

This project is open-source and available under the [MIT License](LICENSE). Feel free to use it for your own projects or as a learning resource.

## Contact

If you have any questions or need further assistance, please reach out to [Your Name] at [Your Email].

Happy coding! 🚀
