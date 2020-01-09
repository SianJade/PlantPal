# Plant Pal - Plant Database and Encyclopedia

Stream Three Project: Data-Centric Development - Code Institute
 
## UX

The purpose of this project is to collect and display data about various plant species - both house plants and outdoor - in order for users to be able to find out information about a plant they have searched for, or plants within a certain genus or family, as well as to present the user with information aboout best care practices for their plants, such as what their lighting requirements are, how often they require watering, and what kind of soil they will best thrive in. For added visual context, a plant photo is supplied alongside each plant's information.

Wireframes for the application can be found in the assets folder of the repository.

A live desktop demo can be found [here](https://plant--pal.herokuapp.com/). The source code for this project can be found [here](https://github.com/SianJade/PlantPal).


## User stories

### User story 1:
As a newcomer to the keeping houseplants, I would like to be able to search houseplants by their common names so that I can find out what the most appropriate care for each of my plants would be.

### User story 2:
As a plant enthusiast, I would like to be able to browse plants by genus so that I can discover more species of plants that belong to a particular genus that I am fond of.

### User story 3:
As a Biology student, I would like to be able to find out information about different orders and families of plants for my school project on plant types.

### User story 4:
As a house plant enthusiast, I would like to be able to search for various plants by their preferred lighting conditions so that I can ascertain which plants will thrive in different areas of my home that have different lighting availabilty.


## Features

### Existing Features

- The site allows users to search for plants via latin name, common name, order, family, genus, preferred lighting conditions, preferred soil type, watering frequency, and whether the plant is a house plant or an outdoor plant using the search bar and then returns a list of seacrch results which match their search bar input; from here the users can access the page of any plant listed in the search results.

- The site also allows users to browse plants by genus name and then allows the user to view all plant species within the selected genus.

- Users are able to submit details of new plants to the database via the 'Add a Plant' page, including details such as the plant's Latin name, common name, genus, preferred ligthting conditions and watering frequency, as well as an image of the plant in order to provide the visual context of the plant's appearance for other users.

- The application features Flask's flashed messages feature wherever relevant (such as upon entry of an incorrect username or password, or if a user attempts to add/edit a plant without having logged in first) in order to inform the user of input errors or if they are unable to perform their desired action and why this is.

- For the sake of good UX practices, the application's flashed messages are contained in dismissable alert boxes so that once the user has read the alert information, they can clear the message from the screen without having to refresh the page or navigate to a different page within the application.

- As MongoDB cannot store image files, images are instead uploaded to the database as a string via a text input. Below the this input field are instructions on how to upload their chosen image to the database - the user must click the anchor text, where a new tab will open using `target="_blank"` and take the user to image sharing site [PostImages](https://postimages.org/) where they can upload their chosen plant image, and then (as instructed on the Add Plant page) copy the direct link to the image and paste this into the plant image input. This image is then displayed at the top of the plant's information page once it has been submitted to the database. For user convenience, I opted to find an image sharing site that did not require the user to first create an account before they were able to upload an image and retrieve the required link, as I felt this would not be best UX pratice in terms of convenience for the user. Whilst hotlinking is also not best UX practice, because of the constraints of MongoDB's available field types, this was the most suitable option for image hosting in this particular project.

- For the sake of good UX and design pratices, I opted to hide the 'My profile' and 'Logout' nav links using Jinja if statements if the user was not logged into their account, as these links would not be necessary for non-logged in users. Conversely, once the user has logged into their account, Jinja if statements are used to hide the 'Login' nav link and display the 'My profile' and 'Logout' nav links.

- Whilst I opted to hide the 'My profile' and 'Logout' nav links to non-logged in users, I decided to keep the 'Add plant' nav link visible to all users - logged in or otherwise - despite the user needing to be logged in to add a plant to the databse. I chose to do this so that new visitors to the app can esily be made aware that as well as viewing information about various plants, they can also add information about plants to the databse themselves. I felt this may not otherwise be clear to newcomers to the application if the nav link was hidden until logged in. As the user needs to be logged in, though, the 'Add plant' nav link redirects to the login page when clicked if the user is not already logged in.

- The application features if/else statements to ensure that the user cannot create an account with a username that already exists in the database, or add a new plant whose latin name already exists in the database in order to prevent suplicate entries. Checks to ensure the username and password entered on the login page a- exist in the databse, and b- that the inputted username and password match, if they do then the user is allowed to login, if not, a Flask flashed message appears informing the user of their error.


### Features Left to Implement

- In future versions of the app, I would like to add functionality for users to upload a photograph of a plant which they may not know the name of, so that the app can search through the existing plants in the database and then redirect them to that particular plant's page within the app should a page with information about that particular plant exist.

- I would also like to implement functionality for the user to upload a photograph of a particular location where they would like to keep a plant, then based on the lighting conditions shown in the photograph, recommend which types of plants may be well suited to the particular location.

- In future releases I would like to implement CAPTCHA on the login page of the app to ensure that the user attempting to login is human.


## Technologies Used

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - The project uses HTML5 to construct the pages within the application.

- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
    - The project uses CSS3 in order to style the HTML5 and Bootstrap elements and components.

- [Bootstrap (ver 4.3.1)](https://getbootstrap.com/)
    - The project uses the Bootstrap 4 grid and components in order to achieve a responsive layout and styling.

- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference)
    - This project uses some Javascript in order to ensure that a user's passwords match when creating an account.

- [Python (ver 3.0)](https://www.python.org/download/releases/3.0/)
    - The project uses Python in order to wire up the database to the front end, as well as to implement relevant functions for the nature of the application.

- [Flask (ver 1.1.1)](http://flask.palletsprojects.com/en/1.1.x/)
    - The project uses the micro-framework Flask as the base of the application, as well as many of its inbuilt functions.

- [Jinja (ver 2.10)](https://jinja.palletsprojects.com/en/2.10.x/)
    - The project uses the Jinja templating langauge in order to extend the base HTML and prevent unnecessary repetition of HTML code, allowing existing code to be reused where possible, as well as to implement for statements inside the HTML documents to display returned results from app.py functions, and if statements to show and hide certain information depending on whether or not a user is logged in.

- [MongoDB (ver 4.2.0)](https://www.mongodb.com/)
    - The project uses MongoDB to host and store the databases required for the project.


## Testing

- HTML code has been run through the [W3C Markup Validator](https://validator.w3.org/) and corrected accordingly.

- CSS code has been validated via the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and returned no errors.

- Once the functionality for a user to edit their account details was in place, I discovered that the user was able to change their userame to that of another user in the database when updating their details - this would have affected the login process as the details used to log in to the application are the username and password, so if multiple of the same username existed in the database who would each have different passwords as the accounts belong to different users, this would prevent the users who have the same username as one another from logging into their accounts. To prevent this, I opted to disable to username field on the edit account page, so that the user is not at risk of taking another user's username.

- The `genera()` function was initially returning multiple of the same genus name if there was more than one plant with that particular genus in the databse, however each genus only needed to be listed once, so that the user could select a genus and view all plants within it. To overcome this issue, the function makes use of the MongoDB collection method `distinct` in order to ensure that each plant genus is only listed once on the All Genera page.

- Whilst `sort('latin_name', pymongo.ASCENDING)` worked fine to display the individual plants in alphabetical order on the view all plants page, I discovered that the same method could not be used to alphabetise the genus names retrieved in the `genera()` function - this is due to the use of the MongoDB collection method `distinct` - these two methods cannot work in conjunction with one another. In order to resolve this, the Python `sort()` method was used on the list of returned genera to order them alphabetically as required for easier user browsing.

- When updating a plant's information, I discovered that although the plant photo input field was pre-filled with the existing value of the plant photo field in the database as required, upon submitting the updated plant details, the plant photo link string would vanish from the database. Upon investigation, I discovered that this was because I had not added `'plant_image': request.form.get('plant_image')` to the `update_plant()` function in my app.py file after I had initially figured out how to submit a plant photo to the databse in the add plant form, as this functionality had been added after the rest of the `update_plant()` function was already in place.

- After the function to only show logged in users the 'My profile' and 'Logout' nav links had been implemented, I discovered that after a new user account had been created and the user had been redirected to their newly created profile page, the 'Login' nav link was still visible instead of the 'my profile' and 'logout' links being shown as intended. This was due to the fact that in the `create_account()` function, there was no code to add the new user to the session after the line ofcode to insert the new user into the database. Once the appropriate code was added to add the new user to the sessionn, the appropriate nav links appeared in the nav bar.

- The application has been tested across different web browsers and screens of all sizes, including iPhone (and Safari), Moto G5 (on Google Chrome and Opera), Samsung Galaxy tablet (and its inbuilt internet app,as well as Google Chrome), Amazon Kindle (using the Amazon Silk web browser), as well as on larger devices and on broswers such as Microsoft Edge, Firefox, and Internet Explorer. The site works well across all devices and all functionality works as intended. The only issue of note is that on the View all plants page, the button is not beside the plant name, but below ad off to right slightly.

- Index.html page has a small white strip at the bottom across all devices, however this does not appear on any other page.


## Deployment
- The application is hosted via [Heroku](https://plant--pal.herokuapp.com/), with the source code being available on [GitHub](https://github.com/SianJade/PlantPal), and is deployed from the master branch - this allows the deployed application to automatically update with any new commits that are made to the master branch.
    - To deploy the dashboard to Heroku, I first had to set up a virtual environment in my code editor to ensure that when I used pip freeze to save my app's requirements to a text file, only the requirements of the project itself were added to the document, and not all of the various requirements and dependencies that come with Cloud9 itself.
    - I then had to set the config vars manually in Heroku in the application's settings tab - here I had to set various keys and values including the port, the IP, the MongoURI link, and my secret key. The MongoURI and secret key link had to be set manually in the config vars as these were saved locally in my env.py file which (due to it containing my MongoDB username and password in the URI link) were inside my `.gitignore` folder. This meant that Heroku did not have access to them until they were set manually in the config vars.
    - Then to ensure my Heroku app updated in realtime with my commits to my Github repository, I opened up the 'Deploy' tab inside my PlantPal Heroku dashboard, and connected the Heroku app to my repo and enabled automatic deploys, so that all pushes to the master branch on Github would also be pushed to Heroku, meaning I did not have to also push to Heroku manually.
    - Finally, to ensure the app would open successfully in Heroku, I had to remove the line `import env` from the top of my app.py code, as Heroku does not have access to this with it being in my `.gitignore` folder, and so could not successfully deploy whilst this line was still included as it could not import the module, heance the config vars.

    
- To run this application locally:
    - Click the green 'clone or download' button in the [GitHub repository for the project](https://github.com/SianJade/PlantPal).
    - Copy the link provided by clicking the clipboard button to the right of the link.
    - In your terminal, type `git clone`, paste in the previously copied link, and hit return.
    - The application should now be installed on your device.

## Credits

- The code used to facilitate flashed messages has been adapted from code found at [Flask](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/).

- The Javascript code used to ensure that the user has entered two matching passwords when creating their account has been adapted from code found at [GeeksForGeeks](https://www.geeksforgeeks.org/password-matching-using-javascript/).

### Content

- Information for each plant's genus, family, and order has been taken from the plant's [Wikipedia](https://en.wikipedia.org/wiki/Wiki) page for the purpose of populating the database.

- The font used for the navbar brand, links, and headers can be found on [GoogleFonts](https://fonts.google.com/specimen/Great+Vibes).

### Media

- Images of each of the plants have been taken from [GoogleImages](https://images.google.co.uk/), as have the background images for all pages on all devices.