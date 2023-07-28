# Backend Bistro

## MoSCoW

### Must have :
  * Connection to PostrgeSQL database
  * Menu items table (model)
    - Primary Key
    - Name
    - Description
    - Price
    - Spicy Level
    - Cuisine type
    - Category type
  * Cuisine table (model)
    - Cuisine ID - primary key
    - Cuisine Type
  * Category table (model)
    - Category ID - primary key
    - Category type
  * Create VIEWS to send JSON data back to a GET request for a list of all menu items <br>
    with category and cuisine listed in the data
  * Create ROUTES to use views created in the previous step
### Should have : 
  * Ability to use all CRUD operations
  * Admin access -- user groups for restaraunt owners
  * Ability to change menus based on location
### Could have :
  * CSV Export functionality
### Won't have : 
  * Nuclear launch codes

## Endpoints
 * /menu
 * /breakfast
 * /lunch
 * /dinner
 * /appetizer
 * /drink

## ***Only need to be able execute READ functionality of the CRUD operations*** ##

# Link to [schema](https://dbdiagram.io/d/64c1a5fd02bd1c4a5ec28fbd)
