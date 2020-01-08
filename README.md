# Plant Pal - Plant Database and Encyclopedia

Stream Three Project: Data-Centric Development - Code Institute
 
## UX

The purpose of this project is to 

Wireframes for the application can be found in the assets folder of the repository.

A live desktop demo can be found [here](https://plant--pal.herokuapp.com/). The source code for this project can be found [here](https://github.com/SianJade/PlantPal).


## User stories

### User story 1:
As a newcomer to the keeping houseplants, I would like to be able to search houseplants by their name so that I can find out what the most appropriate care for each of my plants would be.

### User story 2:
As a plant enthusiast, I would like to be able to browse plants by genus so that I can discover more species of plants that belong to a particular family/genus that I am fond of.

### User story 3:
As a Biology student, I would like to be able to find out information about different orders and genus of plants for my school project on plant types.

### User story 4:
As a house plant enthusiast, I would like to be able to browse various plants by their preferred lighting conditions so that I can ascertain which plants will thrive in different areas of my home that have different lighting availabilty.


## Features

### Existing Features

- The site allows users to search for plants via latin name, common name, order, family, genus, preferred lighting conditions, preferred soil type, watering frequency, and whether the plant is a house plant or an outdoor plant using the search bar and then returns a list of seacrch results which match their search bar input; from here the users can access the page of any plant listed in the search results.

- The site also allows users to browse plants by genus name and then allows the user to view all plant species within the selected genus.

- Users are able to submit details of new plants to the database via the 'Add a Plant' page, including details such as the plant's Latin name, common name, genus, preferred ligthting conditions and watering frequency, as well as an image of the plant in order to provide the visual context of the plant's appearance for other users.

- The application features Flask's flashed messages feature wherever relevant (such as upon entry of an incorrect username or password, or if a user attempts to add/edit a plant without having logged in first) in order to inform the user of input errors or if they are unable to perform their desired action and why this is.

- As MongoDB cannot store image files, images are instead uploaded to the database as a string via a text input. Below the this input field are instructions on how to upload their chosen image to the database - the user must click the anchor text, where a new tab will open using `target="_blank"` and take the user to image sharing site [PostImages](https://postimages.org/) where they can upload their chosen plant image, and then (as instructed on the Add Plant page) copy the direct link to the image and paste this into the plant image input. This image is then displayed at the top of the plant's information page once it has been submitted to the database. For user convenience, I opted to find an image sharing site that did not require the user to first create an account before they were able to upload an image and retrieve the required link, as I felt this would not be best UX pratice in terms of convenience for the user. Whilst hotlinking is also not best UX practice, because of the constraints of MongoDB's available field types, this was the most suitable option for image hosting in this particular project.


### Features Left to Implement

- In future versions of the app, I would like to add functionality for users to upload a photograph of a plant which they may not know the name of, so that the app can search through the existing plants in the database and then redirect them to that particular plant's page within the app should a page with information about that particular plant exist.

- I would also like to implement functionality for the user to upload a photograph of a particular location where they would like to keep a plant, then based on the lighting conditions shown in the photograph, recommend which types of plants may be well suited to the particular location.


## Technologies Used

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - The project uses HTML5 to construct the pages within the application.

- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
    - The project uses CSS3 in order to style the HTML5 and Bootstrap elements and components.

- [Bootstrap (ver 4.3.1)](https://getbootstrap.com/)
    - The project uses the Bootstrap 4 grid and components in order to achieve a responsive layout and styling.

- [Python (ver 3.0)](https://www.python.org/download/releases/3.0/)
    - The project uses Python in order to wire up the database to the front end, as well as to implement relevant functions for the nature of the application.

- [Flask (ver 1.1.1)](http://flask.palletsprojects.com/en/1.1.x/)
    - The project uses the micro-framework Flask as the base of the application.

- [Jinja (ver 2.10)](https://jinja.palletsprojects.com/en/2.10.x/)
    - The project uses the Jinja templating langauge in order to extend the base HTML and prevent unnecessary repetition of HTML code, allowing existing code to be reused where possible.

- [MongoDB (ver 4.2.0)](https://www.mongodb.com/)
    - The project uses MongoDB to host and store the databases required for the project.


## Testing

- HTML code has been run through the [W3C Markup Validator](https://validator.w3.org/) and corrected accordingly.

- CSS code has been validated via the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and returned no errors.


## Deployment
- The application is hosted via [Heroku](https://plant--pal.herokuapp.com/), with the source code being available on [GitHub](https://github.com/SianJade/PlantPal), and is deployed from the master branch - this allows the deployed application to automatically update with any new commits that are made to the master branch.

    
- To run this application locally:
    - Click the green 'clone or download' button in the [GitHub repository for the project](https://github.com/SianJade/PlantPal).
    - Copy the link provided by clicking the clipboard button to the right of the link.
    - In your terminal, type `git clone`, paste in the previously copied link, and hit return.
    - The application should now be installed on your device.

## Credits

- The code used to facilitate flashed messages has been adapted from code found at [Flask](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/)

### Content

-

### Media

-