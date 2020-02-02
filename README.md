# Plant Pal - Plant Database and Encyclopedia

Stream Three Project: Data-Centric Development - Code Institute

## UX

The purpose of this project is to serve as an online catalogue of information about various indoor and outdoor plant species from around the world. This includes their scientific classifications such as their Latin names, family, and genus for those who may be interested in plant geneaolgy or who may wish to use this information to find out more about the biology and/or origins of a specific plant, or of a larger genus/family to which that plant belongs.

Alongside the more scientific plant information is information on what best care practices are for a particular plant, as well as which conditions the plant will thrive best in. This information is intended to allow house plant/gardening enthusiasts to ascertain what kind of lighting, soil type, and watering frequency each plant prefers, so that they can look after each of their plants to the best of their ability, since even plants within the same genus or family can require very different care and maintenence, so a site which contains all of this various information for many different plants in one place would come in very handy.

The user is able to search for specific plants by searching for a common name (such as Snake Plant) or Latin name (such as Sansevieria Trifasciata), as well as being able to browse a broader selection of related plants by searching for a particular genus (such as Tradescantia or Sansevieria) or family (such as Asparagaceae). The ability for users to browse plants by whether they are indoor or outdoor plants, as well as their preferred lighting conditions allow for users to perhaps select new plants which they would like to acquire for a certain spot in their house or garden.

Users are also able to add entries for plants which are not already in the database - including an image of the plant, for visual context, or they can edit the details of plants which are already in the database. To complete these actions the user must be logged in, so as to ensure that upon creation of a new plant entry, a field containing the creator's username is included in the database entry for the plant, which allows for checks to be put in place to ensure that only the creator of a plant's page is able to delete it - this is to ensure there is no other users can randomly or maliciously delete another user's research and hard work from the site. Other users are, however, able to amend plant information should they wish to - this is a feature which may require the implentation of some form of moderation in the future to prevent abuse or misuse of this system.

All forms used for adding/editing plants, creating accounts, and logging in feature top aligned labels for each input field rather than left or right aligned labels - whilst this does make each form longer in terms of the view on the page, using top aligned labels does improve the overall readability of the form for the user, this is because placing the label above the input element rather than to the side allows the user to view both elements together with a single eye movement. I also opted not to make the form labels bold, as a [UX study by Matteo Penzo](https://www.uxmatters.com/mt/archives/2006/07/label-placement-in-forms.php) which tracked the eye movements and timings for users filling out various forms, found that bold labels above an input resulted in an increased time for filling out the form, meaning that to use bold labels in this context would make the form less readable for users. To further enhance readability, all plant information and user information is displayed in a table format to allow for a more uniform layout of each data field and its contents - keeping the field names aligned one below the other, and likewise with the field content.

As well as a search bar on the site's main landing page, I have also included a search input in the navbar - this has been implemented so that users do not have to return to the homepage in order to search for a plant, and instead can perform this action from whichever page they may happen to be on within the site. In order to conform to UX convention and mental models, the nav links have been aligned to the left of the nav bar upon the addition of a navbar search box, and the search box aligned to the right of the screen.

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

- The site allows users to search for plants via latin name, common name, order, family, genus, preferred lighting conditions, preferred soil type, watering frequency, and whether the plant is a house plant or an outdoor plant using the search bar and then returns a list of seacrch results which match their search bar input; from here the users can access the page of any plant listed in the search results. The site also allows users to browse plants by a broader genus name and then allows the user to view all plant species within the selected genus.

- In order for users to be able to what a plant looks like before they click the `view plant` button, each indvidual plant is displayed via the use of Bootstrap cards - this allows for a thumbnail image of the plant to be shown along with its latin and common names. This visual aid allows users who may be looking through plants based on their appearance to view a plant image without having to view all of its details, then if this plant interests them/is what tey are looking for, they can click `view plant` for further information.

- Users are able to submit details of new plants to the database via the 'Add a Plant' page, including details such as the plant's Latin name, common name, genus, preferred ligthting conditions and watering frequency, as well as an image of the plant in order to provide the visual context of the plant's appearance for other users.

- The application features Flask's flashed messages feature wherever relevant (such as upon entry of an incorrect username or password, or if a user attempts to add/edit a plant without having logged in first) in order to inform the user of input errors or if they are unable to perform their desired action and why this is. For the sake of good UX practices, the application's flashed messages are contained in dismissable alert boxes so that once the user has read the alert information, they can clear the message from the screen without having to refresh the page or navigate to a different page within the application.

- As MongoDB cannot store image files, images are instead uploaded to the database as a string via a text input. Below the this input field are instructions on how to upload their chosen image to the database - the user must click the anchor text, where a new tab will open using `target="_blank"` and take the user to image sharing site [PostImages](https://postimages.org/) where they can upload their chosen plant image, and then (as instructed on the Add Plant page) copy the direct link to the image and paste this into the plant image input. This image is then displayed at the top of the plant's information page once it has been submitted to the database. For user convenience, I opted to find an image sharing site that did not require the user to first create an account before they were able to upload an image and retrieve the required link, as I felt this would not be best UX pratice in terms of convenience for the user. Whilst hotlinking is also not best UX practice, because of the constraints of MongoDB's available field types, this was the most suitable option for image hosting in this particular project.

- For the sake of good UX and design pratices, I opted to hide the 'My profile' and 'Logout' nav links using Jinja if statements if the user was not logged into their account, as these links would not be necessary for non-logged in users. Conversely, once the user has logged into their account, Jinja if statements are used to hide the 'Login' nav link and display the 'My profile' and 'Logout' nav links.

- Whilst I opted to hide the 'My profile' and 'Logout' nav links to non-logged in users, I decided to keep the 'Add plant' nav link visible to all users - logged in or otherwise - despite the user needing to be logged in to add a plant to the databse. I chose to do this so that new visitors to the app can esily be made aware that as well as viewing information about various plants, they can also add information about plants to the databse themselves. I felt this may not otherwise be clear to newcomers to the application if the nav link was hidden until logged in. As the user needs to be logged in, though, the 'Add plant' nav link redirects to the login page when clicked if the user is not already logged in.

- The application features if/else statements to ensure that the user cannot create an account with a username that already exists in the database, or add a new plant whose latin name already exists in the database in order to prevent suplicate entries. Checks to ensure the username and password entered on the login page a- exist in the databse, and b- that the inputted username and password match, if they do then the user is allowed to login, if not, a Flask flashed message appears informing the user of their error.

- Users are able to add plants to the database and edit a plant's information only if they are logged into their account, if they are logged in and are also the initial creator of a plant page, they have the ability to delete the plant entirely if they so wish. Users are also able to delete their own account from the database should they wish. In future releases, I would like to hide the 'delete plant' button from any user that is not the initial creator of the plant page - at present, I have not been able to succcessfully implement this function - the 'delete plant' button remains visible to all users, however the check to ensure that only the initial creator of a plant page can delete it remains fully functional, and an error message is displayed to any user who is not the initial creator of the page who may try to delete it, to inform them that is action is not allowed. The delete plant link has been left as an unstyled button in order to differentiate it from the edit plant button visually without detracting too much from the overall colour scheme of the site.


### Features Left to Implement

- In future versions of the app, I would like to add functionality for users to upload a photograph of a plant which they may not know the name of, so that the app can search through the existing plants in the database and then redirect them to that particular plant's page within the app should a page with information about that particular plant exist.

- In future releases, I would also like to implement functionality which redirects the user back the the previous page after they have logged in - i.e. if the user was attempting to add or edit a plant and was prompted to login in order to do so, then once they had completed this action, instead of being redirected to their profile page, they would be redirected back to the page they were previouslt on to complete their desired action, therefore improving the overall UX of the site. So far the only ways I have been able to find to implement this have been by using Django, which I currently do not have enough knowledge of to be able to implement within this project.

- I would also like to implement functionality for the user to upload a photograph of a particular location where they would like to keep a plant, then based on the lighting conditions shown in the photograph, recommend which types of plants may be well suited to the particular location.

- In future releases I would like to implement CAPTCHA on the login page of the app to ensure that the user attempting to login is human.

- In future releases I would like to divise a way to allow users to update their profile details, however in the meantime I have had to remove this functionality.


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

- Python code has been run through the [PEP8 Online Checker](http://pep8online.com/) and all errors found - such as trailing whitespace and lines being over 79 characters - have been amended. However two lines remain which contain string literals for flashed messages (lines 156 and 211) which go over the recommended 79 characters per line - this is because when adding a line break in the middle of the string literal for the flashed messages, I received the error message 'EOL while scanning string literal' in the code editor, due to this I have opted to leave the content inside the string literals on one line, and break the line wherever else possible in order to keep the line length as close to 79 characters as realistically possible. In order to add a line break to line 3 of the app.py file to fit PEP8 line length guidelines without receiving an error, the imported modules have been wrapped in parantheses.

- Throughout the app.py file, there are four continuation lines which the PEP8 Online checker has flagged as over/under-indented for the visual indent (lines 36, 37, 122, and 276) - these lines are only slightly over/under-indented, however - this is due to tabbing being used for indentation throughout the app.py file, and have be in order to avoid mixing spaces and tabs for indentation (as per PEP8 indentation guidelines).

- Once the functionality for a user to edit their account details was in place, I discovered that the user was able to change their userame to that of another user in the database when updating their details - this would have affected the login process as the details used to log in to the application are the username and password, so if multiple of the same username existed in the database who would each have different passwords as the accounts belong to different users, this would prevent the users who have the same username as one another from logging into their accounts. To prevent this, I opted to disable to username field on the edit account page, so that the user is not at risk of taking another user's username.

- After testing the above functionality, I discovered that upon submitting the updated account information, because the username field had been marked as disabled, that the username was removed entirely upon saving to the databse. To resolve this issue I completely removed the username field from the update account page and corresponding function - however this also rendered the username field empty upon form submission. As I do not currently have a solution for this bug, I have opted to temporarily remove the update account function in the short term until I have divised a solution for this issue, as without a username, the user cannot log in to their account at all once they have updated it. The user is still able to delete their account.

- The `genera()` function was initially returning multiple of the same genus name if there was more than one plant with that particular genus in the databse, however each genus only needed to be listed once, so that the user could select a genus and view all plants within it. To overcome this issue, the function makes use of the MongoDB collection method `distinct` in order to ensure that each plant genus is only listed once on the All Genera page.

- Whilst `sort('latin_name', pymongo.ASCENDING)` worked fine to display the individual plants in alphabetical order on the view all plants page, I discovered that the same method could not be used to alphabetise the genus names retrieved in the `genera()` function - this is due to the use of the MongoDB collection method `distinct` - these two methods cannot work in conjunction with one another. In order to resolve this, the Python `sort()` method was used on the list of returned genera to order them alphabetically as required for easier user browsing.

- When updating a plant's information, I discovered that although the plant photo input field was pre-filled with the existing value of the plant photo field in the database as required, upon submitting the updated plant details, the plant photo link string would vanish from the database. Upon investigation, I discovered that this was because I had not added `'plant_image': request.form.get('plant_image')` to the `update_plant()` function in my app.py file after I had initially figured out how to submit a plant photo to the databse in the add plant form, as this functionality had been added after the rest of the `update_plant()` function was already in place.

- After the function to only show logged in users the 'My profile' and 'Logout' nav links had been implemented, I discovered that after a new user account had been created and the user had been redirected to their newly created profile page, the 'Login' nav link was still visible instead of the 'my profile' and 'logout' links being shown as intended. This was due to the fact that in the `create_account()` function, there was no code to add the new user to the session after the line ofcode to insert the new user into the database. Once the appropriate code was added to add the new user to the sessionn, the appropriate nav links appeared in the nav bar.

- The application has been tested across different web browsers and screens of all sizes, including iPhone (and Safari), Moto G5 (on Google Chrome and Opera), Samsung Galaxy tablet (and its inbuilt internet app,as well as Google Chrome), Amazon Kindle (using the Amazon Silk web browser), as well as on larger devices and on broswers such as Microsoft Edge, Firefox, and Internet Explorer. The site works well across all devices and all functionality works as intended. The only issue of note is that on the View all plants page, the button is not beside the plant name, but below ad off to right slightly.

- Index.html page has a small white strip across the bottom on all devices, however this does not appear on any other page.


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