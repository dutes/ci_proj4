# Recipe Sharing Platform

## Overview
The recipe sharing platform is a web application that allows users to create an account and share manage recipes.
The project is built using Django and designed to provide a repsonsive, interactive and engaging expierence for cullinary fans.

## Table of Contents
TBD

## WireFrame

need to scan sketch

## Functional specificiations







## User Walk through
### Landing page
![landing page](/docs/readme_img/landing_page.png)

The first view the user gets when opening the project is the landing page. 
Here the user is introduced to the concept of the site via an introduction paragraph.
The user can login, if they already have an account or sign up if they do not.

### Nav Menu
![Navmenu](/docs/readme_img/nav_menu.png)

The nav menu is available to the user by clicking on the burger menu icon in the top right of the screen. 
The menu expands offering the user the navigation choices available to them. Clicking on a page will open the selected page and minimise the nav menu once again.


### Login
![Login](tbd)

The login page is where the user will enter the full site. Without being logged in the add, delete and edit recipes are blocked from them.
The login text fields are validated by the django library.
The login diaog also has a link to open the sign up dialog should the user need it.
Dialog is modal and cannot be dismissed, except by click the cancle or close buttons.

### Sign UP
![Signup](tbd)

The sign up dialog contains the username field, the password and confirm password fields.
All fields are validated. The useranme must be at least 8 chars which cannot be extended or include spaces. 
The passwords must be at least 5 chars and must the the same in both the original as well as the confirmation field.
User feedback on the validity of their usernames and passwords is realtime and feedback is given as red text under the appropriate fields.
User is logged in automatically when their user account is created.
Dialog is modal and cannot be dismissed, except by click the cancle or close buttons.

### Meal Categories (Starters, Mains, Desserts)
![Categorgies](tbd)

Each of the category pages, starters, mains and desserts contain the recipes of each category as selected by the user that created them.
Each category view has a scrollable list of accordian format recipe cards. The user can scroll through the recipe cards in minimised format which shows them the image and title of each recipe. 
If the user wants the full recipe they simply click the accordion card and it expands to the full recipe card.
All category pages are viewable without logging in.


### Add Recipe
![Add New Recipe](/docs/readme_img/add_recipe.png)

The add recipe view is where the user enters the recipe they have chosen.
The view consists of a text field for the recipe name, text areas for the ingredients and instructions. A drop down selector for the category and a file picker for an image for the recipe. All feilds are manditory and are validated. 
The image is represented by a 100x100 placeholder until it is replaced by the user's uploaded image.
The add recipe view is not viewable unless logged in.


### Edit Recipe
![Edit reicpe](tbd)

The edit recipe view shows a list of the user's created recipes. User only sees recipes they have created in this view. 
The list is presented with a mini version of the recipe's image and the title in a reducecd size tile with an EDIT button on each tile.
Clicking on EDIT opens an edit dialog where the changes can be made and saved or cancelled.
Once edited and saved the recipe's instance is updated and the change reflected on the recipe card in the relevant category view.
The edit reicpe page is not viewable unless logged in.

### Delete Recipe
![Delete recipe](tbd)

The delete view is similar in format to the edit recipe page. Each of the user's recipes are presented in a list with a DELTE button in the tile. Only the currently logged in user's recipes are allowed to be deleted.
Clicking the delete button opens a confirmation dialog, cancelling on this dialog will not delete the recipe. Clicking on YES to confirm will remove the recipe from the data base and the relevant category. 

### Logout 
The user is given the option to logout in the nav menu. This helps to ensure their recipes form unwanted deletions or editting


## Model
![Model Diagram](tbd)

The Recipe model is the backbone of the Recipe Sharing Platform, designed to store and manage user-submitted recipes effectively. It includes fields to capture essential details like the name of the recipe, a descriptive title that makes it easy for users to identify. The ingredients field, a text area, allows users to list all the components required to create the dish. Complementing this is the instructions field, where detailed, step-by-step guidance can be provided. The category field organizes recipes into predefined groups like starters, mains, and desserts, enhancing discoverability. An optional image field lets users upload a picture of their creations, adding a visual element to the platform. Each recipe is linked to a user via a foreign key, ensuring that every recipe has an identifiable author. Together, these fields form a robust structure, ensuring recipes are informative, categorized, and visually appealing, while maintaining a clear association with their creators.


