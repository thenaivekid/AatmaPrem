# AatmaPrem 
We are too busy with our work,study and people around us. I believe that we must give ourself some quality time to reflect on ourselves, find our nature and what we want to do in life. `AatmaPrem` means self love in Sanskrit. This web app lets you discover the universe within yourself. 

## Features
- Admin canb create a topic for users to reflect on.
- User authentication.
- Per user database provides privacy to user data.
- User can add items on diverse topics about himself/herself. Eg user can add their fears in the `post` Fears. 
- Once they finish doing that item, they can mark done. Eg if user has added fear of being criticized and s/he work on herself/himself and get over that fear, then s/he can mark that fear done.
- User can discover his/her personality traits
- User can analyze people around them and find out if s/he is spending time with people s/he shouldn't be around.
- User spends some time reflecting on his/her day everyday with some help of the app.
- This app uses some apis to get some stoic quotes and lets user visualize something by using image generation AI of openai.
- Admin can give some useful external links to relevant topics of self love with title and link.
- This app smartly reuses same codes to generate pages of widely diverse topics.


# Distinctiveness and Complexity

This project is not similar to any of the projects we have done for the course. This app does not sell anything. Thus, this is distinct from Pizza project and ecommerce. This is not a social media. This is obviously different from google UI project and mail app because this has both backend and front end. Wiki project merely takes wiki input from users and lets them view the wiki page. But this app lets admin to create new topic for other users and users can discover facts about themselve on various topics and add items to change about themselves and can mark done once they successfully change that particular thing about himself/herself. User can analyze folks around them. The app uses a costum made algorithm to score poeple out of 100. The person with 100 score is the ideal person for that user and people with very low score are toxic and need to be avoided. People are sorted according to that score. Journaling section provides a template for the user to keep track of their day and view their diaries sorted by date. Mindfulness section uses publicly available apis. Open ai api to generate images and `https://api.adviceslip.com/advice` to generate advice and `https://api.themotivate365.com/stoic-quote` to get stoic quotes. This app also allows admin to provide useful links that are stored in `ExternalLink` table with title and the link itself. This app uses 5 custom database models:
- `Post` that stores the diverse topics for users to think about themselves. Eg Watchlist.
- `PostItem` that stores input item of some topic that can be done or in progress. Eg Harry Porter can be a item in Watchlist.
- `AnalyzingPeople` stores big 5 personality traits and some relevant facts about people in the user's life.
- `Journal` stores journal with particular items like highlights of of each day.
- `ExternalLink` stores title and link to some relevant web pages.

This web app uses vanila JS to fetch data from Django backend and display items for smooth user experience and css to create nice interface. A little help of Bootstrap is taken to make pages more responsive in addition to flexbox. 
This proves the complexity of the project as well as the distinctiveness.

# Created files
Under the directory `templates/deepdive`
- layout.html that defines basic layout for all web pages.
- index.html that displays the topics for reflection sorted by category.
- post.html that displays the details and finished and unfinished items of that particular topic.
- journal.html that allows user to add journal and view journals sorted by date.
- analyzingPeople.html that allows user to analyze people with the help of a template and shows people sorted by their score.
- mindfulness.html shows quotes, external links and lets user visualize any thought using openai image generation model.

Under the directory `static/deepdive`
- index.js that contains JS code to create form, add items and mark items done.
- mindfulness.js makes api calls and shows the quotes in the html page and also sends the query for image generation to django backend and also displays the generated image using the image urls returned by django.
- style.css that styles all the html documents.

For custom algorithm to score people
- util.py contains `scorePeople` function and a helper function `traitScore`.

Urlpatterns are in urls.py in deepdive directory.

# How to run the app
In the parent directory containing `manage.py` file, run
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

Since the api secret key of open ai can not be pushed to github, the image generation may not work.