**NEWS APPLICATION**

News Application uses News API to fetch all the news around the world.
You can search the news based on:
- Language
- Keywords
- Country
- Category

**Requirements:**
Tools and packages required to successfully install this project. For example:
- Python 3.7
- Python IDE (PyCharm)
- Django

**Installation of Python:**
https://docs.python.org/3/using/windows.html

**Install PyCharm from:** https://www.jetbrains.com/pycharm/

**Cloning the project repository:**
git clone project-url

**Features:**
- Admin functionality to create, delete and block users
- Login functionality for users
- Users can search news based on: keywords and phrases
- Added filters for search enhancement:
  - Language
  - Country
  - Category
  - Date published
  - Name of the source
- New tab reflecting the list of search results
- Button to refresh the search results
- Sorted search results based on "Date published"
- Added authentication for every user to view the keywords that they searched for.
- Prevented frequent searches for the same keyword. We cannot search for same keyword for the next 15 minutes.
- Avoided creating duplicate keyword into user's account table

**Initializing the project:**
- Import the project to PyCharm
- Make sure that you are inside the project path, example: cd  D:\Users\PSangamn\PycharmProjects\newsapp
- Install Django through terminal using the command: pip install django
- Creating the database: python manage.py makemigrations
- Running the migrations: python manage.py migrate
- Creating Admin: python manage.py createsuperuser
- Run the application in admin mode: python manage.py runserver
- Post running the server, please go to this path for admin mode: /admin
- Login using admin credentials used while creating Admin.
- Go to 'Accounts' table and click on 'Add Account' and create a new user.
- Logout from admin account and go to root path(Example: Remove: '/admin' from url)
- Login to the user account that is created from Admin.

**Instructions to use the project:**
- Post logging in with the user credentials, by default, you will see Indian News.
- Various search functionalities:
  - Category: Select a category from the dropdown and click on Search
  - Country: Type the country name and click on search button(Eg: us, in, ca)
  - Latest news: Give a keyword (eg.: Tesla) and click on search button
  - Language: Give a keyword and select a language from the dropdown and click on search
  - Date published: Give a keyword and give a date(yyyy-mm-dd) and click on search button
  - Name of the source: Give a keyword and give a source name(eg.: wired) and click on search button

**Time taken to build this project:** 5 Days

**Overall experience:** 
- Worked on creating database
- Worked on APIs to handle incoming requests
- Worked on Models to interact with database
- Worked on handling Cookies
- Worked on HTML, CSS and Bootstrap