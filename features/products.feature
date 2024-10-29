Feature: Product Management
  This feature allows the user to manage products by performing operations like reading, updating, deleting, listing all, and searching products based on category and availability.

######################################################################
# Task 6a - BDD Scenario for READING a Product
######################################################################
Scenario: Read a Product
    When I visit the "Home Page"
    And I set the "Name" to "Hat"
    And I press the "Search" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    And I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see the message "Success"
    And I should see "Hat" in the "Name" field
    And I should see "A red fedora" in the "Description" field
    And I should see "True" in the "Available" dropdown
    And I should see "Cloths" in the "Category" dropdown
    And I should see "59.95" in the "Price" field

######################################################################
# Task 6b - BDD Scenario for UPDATING a Product
######################################################################
Scenario: Update a Product
    When I visit the "Home Page"
    And I set the "Name" to "Hat"
    And I press the "Search" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    And I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see the message "Success"
    And I set the "Description" to "A stylish blue fedora"
    And I press the "Update" button
    Then I should see the message "Update Successful"

######################################################################
# Task 6c - BDD Scenario for DELETING a Product
######################################################################
Scenario: Delete a Product
    When I visit the "Home Page"
    And I set the "Name" to "Hat"
    And I press the "Search" button
    Then I should see the message "Success"
    When I copy the "Id" field
    And I press the "Clear" button
    And I paste the "Id" field
    And I press the "Retrieve" button
    Then I should see the message "Success"
    And I press the "Delete" button
    Then I should see the message "Delete Successful"

######################################################################
# Task 6d - BDD Scenario for LISTING ALL PRODUCTS
######################################################################
Scenario: List All Products
    When I visit the "Home Page"
    And I press the "List All" button
    Then I should see a list of all products
    And I should see "Hat" in the list of products
    And I should see "Shoes" in the list of products

######################################################################
# Task 6e - BDD Scenario for Searching a Product based on Category
######################################################################
Scenario: Search a Product by Category
    When I visit the "Home Page"
    And I set the "Category" to "Cloths"
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Hat" in the "Name" field

######################################################################
# Task 6f - BDD Scenario for Searching a Product based on Availability
######################################################################
Scenario: Search a Product by Availability
    When I visit the "Home Page"
    And I set the "Available" dropdown to "True"
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Hat" in the "Name" field
