<h1>Inform-agency app</h1>

<h3>Project Description</h3>

<p>This system allows tracking editors responsible for each newspaper issue. 
It helps the chief editor always know who worked on a specific edition. 
Additionally, each newspaper can have multiple topics assigned.</p>

<p>Only authenticated users can add, edit, and delete newspaper issues, editors, and topics.</p>

<h3>Requirements</h3>

Required Tools:
<ul>
<li>Python 3.12</li>

<li>Django 5.1.7</li>

<li>Bootstrap4 for frontend styling</li>
</ul>

<h3>Database Structure</h3>

<h4>The project includes the following main tables:</h4>
<ul>
<li>editors – stores information about editors</li>

<li>newspapers – contains data about newspaper issues</li>

<li>topics – list of possible newspaper topics</li>
</ul>

<h3>Required Data Files</h3>

To initialize the database, load the following three JSON files:
<ul>
<li>data.json - list of database for project</li>
</ul>

<h3>Installation and Setup</h3>

Clone the repository:

    git clone https://github.com/dkornit/inform-agency

Install dependencies:

    pip install -r requirements.txt

Apply migrations:

    python manage.py migrate

Import data from JSON files into the database:

    python manage.py loaddata data.json

Run the development server:

    python manage.py runserver

Open the application in your browser at:

    http://127.0.0.1:8000/

Any user can watch the ListView, DetailView, main page. 




