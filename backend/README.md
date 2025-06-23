# AMR: Backend - Flask Application

<p>A Flask-based web application structured with Docker support.</p>
<h2>Project Structure</h2>

<pre>
analyze-my-name/
├── backend/
│   ├── src            # Application source code (routes, models, utils, etc.)
        ├── core          # AI structure: extractor (text from pdf), Generation of suggestions
        ├── logs          # logs are stored and could be saved in the databse (in future)
        ├── model         # sqlalchemy db model
        ├── payload       # for request and response via routes
        ├── service       # logic behind routes and integration of core logic
        ├── utils         # for features such as: token_required, log script and helper functions
        ├── app.py        # contains function for creating flask app
        ├── config.py     # for importing flask app configuration variables
        ├── extensions.py # declarations of main flask features extensions
        
|   ├── requirements.txt
|   ├── .env           # Environment variables for Flask settings
|   ├── run.py         # Entry point for the Flask application
│   └── Dockerfile     # Dockerfile for containerizing the backend app
</pre>

<h2>Getting Started</h2>

<h3>Prerequisites</h3>
<ul>
  <li><a href="https://www.python.org/downloads/">Python 3.12+</a></li>
  <li><a href="https://docs.docker.com/get-docker/">Docker</a> (optional, for containerized deployment)</li>
  <li><a href="https://pip.pypa.io/en/stable/">pip</a> for installing Python packages</li>
</ul>

<h3>Environment Configuration</h3>

<p>Create a <code>.env</code> file in the <code>backend/</code> directory to store environment variables. These are used by Flask for configuration.</p>

<p>Example <code>.env</code> file:</p>
<pre>
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///app.db
</pre>


<h3>Running the App (Locally)</h3>

<ol>
  <li>Navigate to the <code>backend</code> directory:
    <pre>cd backend</pre>
  </li>
  <li>Create a virtual environment:
    <pre>python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate</pre>
  </li>
  <li>Install dependencies:
    <pre>pip install -r requirements.txt</pre>
  </li>
  <li>Run the Flask app:
    <pre>python3 run.py</pre>
  </li>
</ol>

<p>The app should now be running at <a href="http://localhost:5000/">http://localhost:5000/</a>.</p>

<h3>Running with Docker</h3>

<ol>
  <li>Navigate to the <code>backend</code> directory:
    <pre>cd backend</pre>
  </li>
  <li>Build the Docker image:
    <pre>docker build -t amr-backend .</pre>
  </li>
  <li>Run the Docker container:
    <pre>docker run --env-file .env -p 5000:5000 amr-backend</pre>
  </li>
</ol>

<p>The app should now be accessible at <a href="http://localhost:5000/">http://localhost:5000/</a>.</p>

<h2>Notes</h2>
<ul>
  <li>All Flask application logic should be placed within the <code>src/</code> directory.</li>
  <li>Ensure a <code>requirements.txt</code> file is included for Python dependency management.</li>
</ul>

<h2>License</h2>
<!-- <p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for details.</p> -->
