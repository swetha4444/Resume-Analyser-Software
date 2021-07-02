# Resume Analyser Software
A resume is a summarized document which represents a job seeker’s professional background and skills for a prospective employer. The resume parser converts an unstructured form of resume data into a structured format, it extracts it into machine-readable output like CSV. Automated resume screening increases quality of hire by reducing false positives because candidates can't trick the system through keyword stuffing. It also reduces false negatives because candidates with good qualifications no longer slip through the keyword filters.

## Features
 * **Parses the resume (pdf, txt, word file) and retrieves details.**
    * hi
 * **Summarises the work experience and  work-experiences and retrieves key words.**
    * Scoring a sentence is differs with different algorithms. Here, we are using **TF-IDF score of words in a sentence to give weight to the paragraph**. The sentences with higher scores are chosen.
    * **Distilbert** is used as it has shown great performance in similarity tasks, which is what we are aiming for with keywords extraction. To find the candidates that are most similar to the document, **cosine similarity** is used. The most similar candidates to the document are good keywords for representing each review and the keywords are thus got from the candidates. On entering the review number corresponding keywords are returned.
 * **Batch process a set of resumes** and catogerise applicants based on skills and other factors.
    * The application gets a set of resumes, parses each of it and  creates a ```CSV``` file which can be used to filterout applicants with specific requirments.
 * **Data Analysis on batch processed resume.**
    * Graphical insights of the number of applicants of a given batch of resumes have a particular skill.
 * **Knowledge graph of resume skills and work experience.**
    *  Key elements of resumes can be stored and visualized as knowledge graphs. **Knowledge graph of people and the programming skills** they mention on their resume after parsing it.
 * **Resume based job classification**.
    * **CNN based model** takes your work experience into account,and decides what job is well suited for you. The model is fed with about 10,000 rows of job-roles and its  requirments taken from ```Naukri.com```

## Usage
* Download the sample resume to follow its format.
* As a student you can upload your resume and the software can fetch you the knowledge graph and a job recommendation.
* As a recruiter, to batch process a set of resumes, add all the resumes to a folder names ```Resumes``` and upload that folder.
   * You can download the summary of all the resumes in form of a CSV file or search for applicants with a given skill set.
   * Can get a knowledge graph
   * Overall data analysis on the number of applicants with a particular skill

## Technology Stack
<p float="left">
  <img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" />
  <img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/>
  <img alt="HTML5" src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"/>
  <img alt="CSS3" src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white"/>
   <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Canva-%2300C4CC.svg?&style=for-the-badge&logo=Canva&logoColor=white" />
 </p>

## Installation
To run the flask app in a  windows environment
 1. Install python 3.8
 2. Run ```pip install virtualenv```
 3. Run ```mkdir Project``` to create project directory
 4. Donload/Clone the project and run ```cd Project``` to move to the project directory
 5. Run ```virtualenv venv``` to create a virtual environment
 6. Run ```.\Scripts\activate```  to activate the virtual environment
 7. Install the required dependencies ```pip install -r requirments.txt```
 8. Copy the contents of the Flask app folder to your virtual environment and use command ```python app.py``` to run the app.  

## Output
  
https://user-images.githubusercontent.com/68152189/122644103-1ae8d000-d131-11eb-9f0b-13990ddfe8b3.mp4

