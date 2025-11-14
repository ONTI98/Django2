<h1>Introduction</h1>
<p><strong>Codonti Social</stromg> is a Django-based,fully responsive social media template that is based on information-sharing for educational purposes. its purpose is to serve as a template for making Django-based social media applications open to developer-specific modifications.</p>

<h1>Overview</h1><br>
<p>The main app's backend is built with Python's Django framework.The following are all the technologies used:<br>
<ul>
    <li>Django framework</li>
    <li>HTML</li>
    <li>Vanilla CSS</li>
    <li>Vanilla Javascript</li>
    <li>JQuery</li>
    <li>Tailwind CSS</li>
</ul>
</p>
<h1>Light mode mobile and large devices </h1>
<h2>Responsive design</h2>
<div align="center">
    <img src="https://github.com/ONTI98/Django2/blob/main/fullstack1023.jpg?raw=true" 
    style="width:500px;">
</div>
<div align="center">
    <img src="https://github.com/ONTI98/Django2/blob/main/fullstack1025.jpg?raw=true"
    style="">
</div>

<h1>Dark mode mobile and large devices </h1>
<div align="center">
    <img src="https://github.com/ONTI98/Django2/blob/main/fullstack1022.jpg?raw=true" 
    style="width:500px;">
</div>
<div align="center">
    <img src="https://github.com/ONTI98/Django2/blob/main/fullstack1024.jpg?raw=true"
    style="">
</div>

<h1>Features</h1>
<ul>
    <li>Follow unfollow button</li>
    <li>Posts</li>
    <li>Dicsover:Shows posts from users that have an account, that you may not be following upon opening an account)</li>
    <li>Account</li>
    <li>Django sign up an sign in forms</li>
</ul>

<h3>Features that can be added on</h2>
<ul>
    <li>Like button</li>
    <li>Comments</li>
    <li>Reposting</li>
    <li>Custom-styled forms</li>
</ul>

<h1>Application structure</h1>
<code>
    Directory structure:
    └── onti98-django2/
        ├── README.md
        ├── manage.py
        ├── requirements.txt
        ├── feed/
        │   ├── __init__.py
        │   ├── admin.py
        │   ├── apps.py
        │   ├── models.py
        │   ├── tests.py
        │   ├── urls.py
        │   ├── views.py
        │   ├── migrations/
        │   │   ├── 0001_initial.py
        │   │   └── __init__.py
        │   └── templates/
        │       └── feed/
        │           ├── create.html
        │           ├── detail.html
        │           ├── discover.html
        │           └── homepage.html
        ├── followers/
        │   ├── admin.py
        │   ├── models.py
        │   └── views.py
        ├── frontend/
        │   └── js/
        │       └── main.js
        ├── myapp/
        │   ├── settings.py
        │   ├── urls.py
        │   └── templates/
        │       ├── base.html
        │       ├── account/
        │       │   ├── base.html
        │       │   ├── login.html
        │       │   ├── password_change.html
        │       │   ├── password_reset.html
        │       │   └── signup.html
        │       └── includes/
        │           └── post.html
        ├── profiles/
        │   ├── admin.py
        │   ├── forms.py
        │   ├── models.py
        │   ├── urls.py
        │   ├── views.py
        │   └── templates/
        │       ├── profile.html
        │       ├── profile_details.html
        │       ├── profile_update.html
        │       └── update_profile.html
        ├── templates/
        │   └── homepage.html
        └── til/
            ├── __init__.py
            ├── asgi.py
            ├── settings.py
            ├── urls.py
            └── wsgi.py

</code>
<h1>Running app for development</h1>
<p>To run the app You will need to do the following</p>
<h3>Clone the respository</h3>
<code>git clone https://github.com/ONTI98/Django2.git</code>
<p>In the terminal, create a virtual environment</p>
<code>python -m venv .venv</code>
<h3>Set execution policy to 'Remotesigned' in your terminal (ONLY IF YOU DO NOT HAVE ADMIN ACCESS)<h3>
<code> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process</code>
<h3>Activate the virtual environment scripts</h3>
<p>VS Code</p>
<code>./.venv/Scripts/activate</code>
<p>OR</p>
<code>cd .venv</code><br>
<code>cd Scripts</code><br>
<code>activate</code>
<h3>Install requirements</h3>
<code>pip install -r requiremenets.txt</code>
<h2>HEADS-UP: You might neeed to do some migrations and debugging<h2>
<h1>HAVE A BLAST</H1>

