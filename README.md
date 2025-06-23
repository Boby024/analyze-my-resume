# analyze-my-resume

<h2>Description</h2>
A web application that allows users to upload resumes and job descriptions, 
then intelligently analyzes the resume content to highlight skill gaps, 
missing keywords, and offer AI-powered improvement suggestions using NLP and the OpenAI API.

<h2>Tech Stack</h2>

| Layer          | Technology                            | Purpose                                                  |
| -------------- | ------------------------------------- | -------------------------------------------------------- |
| Frontend       | Angular                               | Responsive UI, form handling, result visualization       |
| Backend        | Flask (Python)                        | REST API, orchestration between NLP and OpenAI APIs      |
| NLP Processing | Python (spaCy, NLTK, or Transformers) | Text extraction, keyword extraction, similarity analysis |
| AI Enhancement | Not defined yet                       | Generate suggestions for resume improvement              |
| File Parsing   | PyPDF2 or pdfplumber                  | Extract text from uploaded documents                     |
| Deployment     | Docker                                | /                                                        |


<h2>Core Features</h2>

<ol>
  <li>
    <strong>Resume Upload &amp; Parsing</strong>
    <ul>
      <li><strong>Input:</strong> Upload resume file (PDF, DOCX)</li>
      <li><strong>Backend Process:</strong>
        <ul>
          <li>Parse document</li>
          <li>Clean and normalize text (remove headers/footers, etc.)</li>
        </ul>
      </li>
    </ul>
  </li>

  <li>
    <strong>Job Description Input</strong>
    <ul>
      <li>Text box or file upload for job description</li>
      <li>Normalize and tokenize for NLP analysis</li>
    </ul>
  </li>

  <li>
    <strong>Resume vs JD Analysis</strong>
    <ul>
      <li><strong>NLP Matching:</strong>
        <ul>
          <li>Keyword extraction (TF-IDF / RAKE / Named Entity Recognition)</li>
          <li>Compare resume and JD for overlap</li>
          <li><strong>Highlight:</strong>
            <ul>
              <li>Missing required skills</li>
              <li>Mentioned soft vs hard skills</li>
              <li>Role-specific terminology</li>
            </ul>
          </li>
        </ul>
      </li>
    </ul>
  </li>

  <li>
    <strong>Skill Gap Visualization</strong>
    <ul>
      <li>Angular UI highlights:
        <ul>
          <li>Present keywords</li>
          <li>Missing/weak keywords</li>
        </ul>
      </li>
      <li>Radar chart or bar chart showing match %</li>
    </ul>
  </li>

  <li>
    <strong>AI-Generated Suggestions (Bonus Feature)</strong>
    <ul>
      <li>Prompt API suggestion (e.g., GPT-4) with:
        <ul>
          <li>Resume text</li>
          <li>Job description</li>
        </ul>
      </li>
      <li>Receive suggestions like:
        <ul>
          <li>“You should include experience with React if you have it.”</li>
          <li>“Consider emphasizing leadership or collaboration experience.”</li>
        </ul>
      </li>
    </ul>
  </li>

  <li>
    <strong>Report Download</strong>
    <ul>
      <li>Option to export a summary PDF:
        <ul>
          <li>Skill match %</li>
          <li>Missing keywords</li>
          <li>AI suggestions</li>
        </ul>
      </li>
    </ul>
  </li>
</ol>

<h2>Run the project</h2>
<li> Backend: follow instructions in README.md inside the folder "backend"</li>
<li> Frontend: follow instructions in README.md inside the folder "frontend"</li>