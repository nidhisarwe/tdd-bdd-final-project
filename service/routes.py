######################################################################
# Task 4a - READ A PRODUCT
######################################################################
@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    """
    Retrieve a single Product

    This endpoint will return a Product based on its id
    """
    app.logger.info("Request to Retrieve a product with id [%s]", product_id)

    product = Product.find(product_id)
    if not product:
        abort(status.HTTP_404_NOT_FOUND, f"Product with id '{product_id}' was not found.")

    app.logger.info("Returning product: %s", product.name)
    return product.serialize(), status.HTTP_200_OK

######################################################################
# Task 4b - UPDATE A PRODUCT
######################################################################
@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    """
    Update an existing Product

    This endpoint will update a Product based on the posted data
    """
    app.logger.info("Request to Update a product with id [%s]", product_id)

    product = Product.find(product_id)
    if not product:
        abort(status.HTTP_404_NOT_FOUND, f"Product with id '{product_id}' was not found.")

    # Update with new data
    product.deserialize(request.get_json())
    product.update()

    app.logger.info("Product with ID [%s] updated", product_id)
    return product.serialize(), status.HTTP_200_OK

######################################################################
# Task 4c - DELETE A PRODUCT
######################################################################
@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    """
    Delete a Product

    This endpoint will delete a Product based on its id
    """
    app.logger.info("Request to Delete a product with id [%s]", product_id)

    product = Product.find(product_id)
    if product:
        product.delete()

    app.logger.info("Product with ID [%s] deleted", product_id)
    return "", status.HTTP_204_NO_CONTENT

######################################################################
# Task 4d - LIST ALL PRODUCTS
######################################################################
@app.route("/products", methods=["GET"])
def list_all_products():
    """
    List all Products

    This endpoint will return all Products
    """
    app.logger.info("Request to List all products")
    products = Product.all()
    return jsonify([product.serialize() for product in products]), status.HTTP_200_OK

######################################################################
# Task 4d - LIST PRODUCTS BY NAME
######################################################################
@app.route("/products", methods=["GET"])
def list_products_by_name():
    """
    List Products by Name

    This endpoint will return all Products matching a given name
    """
    name = request.args.get("name")
    app.logger.info("Request to List products by name: %s", name)

    products = Product.find_by_name(name)
    return jsonify([product.serialize() for product in products]), status.HTTP_200_OK

######################################################################
# Task 4d - LIST PRODUCTS BY CATEGORY
######################################################################
@app.route("/products", methods=["GET"])
def list_products_by_category():
    """
    List Products by Category

    This endpoint will return all Products in a specified category
    """
    category = request.args.get("category")
    app.logger.info("Request to List products by category: %s", category)

    products = Product.find_by_category(category)
    return jsonify([product.serialize() for product in products]), status.HTTP_200_OK

######################################################################
# Task 4d - LIST PRODUCTS BY AVAILABILITY
######################################################################
@app.route("/products", methods=["GET"])
def list_products_by_availability():
    """
    List Products by Availability

    This endpoint will return all Products that match a specified availability
    """
    available = request.args.get("available")
    app.logger.info("Request to List products by availability: %s", available)

    products = Product.find_by_availability(available)
    return jsonify([product.serialize() for product in products]), status.HTTP_200_OK
