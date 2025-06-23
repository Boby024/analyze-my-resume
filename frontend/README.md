# AMR: Frontend - Angular Application

<p>This is the frontend of the project, built with Angular and optionally containerized using Docker.</p>

<h2>Project Structure</h2>

<pre>
frontend/
├── angular.json         # Angular project configuration file
├── src/                 # Source code for the Angular application
└── Dockerfile           # Dockerfile for building and running the frontend in a container
</pre>

<h2>Getting Started</h2>

<h3>Prerequisites</h3>
<ul>
<li><a href="https://nodejs.org/en/download/">Node.js (v20+ recommended)</a></li>
<li><a href="https://angular.io/cli">Angular CLI (v17+)</a></li>
<li>Package Manager: npm(v10+)</li>
<li><a href="https://docs.docker.com/get-docker/">Docker</a> (optional, for containerized deployment)</li>
</ul>

<h3>Running the App (Locally)</h3>

<ol>
<li>Navigate to the <code>frontend</code> directory:
    <pre>cd frontend</pre>
</li>
<li>Install dependencies:
    <pre>npm install</pre>
</li>
<li>Serve the app locally:
    <pre>ng serve</pre>
</li>
</ol>

<p>The app will be available at <a href="http://localhost:4200/">http://localhost:4200/</a> by default.</p>

<h3>Running with Docker</h3>

<ol>
<li>Navigate to the <code>frontend</code> directory:
    <pre>cd frontend</pre>
</li>
<li>Build the Docker image:
    <pre>docker build -t arm-frontend .</pre>
</li>
<li>Run the container:
    <pre>docker run -p 4200:80 arm-frontend</pre>
</li>
</ol>

<p>The containerized app should now be accessible at <a href="http://localhost:4200/">http://localhost:4200/</a>.</p>

<h2>Notes</h2>
<ul>
<li>Source code lives in the <code>src/</code> directory following standard Angular structure.</li>
<li>Make sure your <code>Dockerfile</code> handles Angular production builds correctly (e.g., using <code>ng build --prod</code>).</li>
</ul>

<h2>License</h2>
<!-- <p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for details.</p> -->
