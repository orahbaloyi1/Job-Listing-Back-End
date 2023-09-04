from flask import Flask, request
from flask_cors import CORS

import config
from db import db

app = Flask(__name__)   
CORS(app)

@app.route('/')         
def main():
    return "jobs"


@app.route('/submit_job', methods=["POST"])
def submit_job_route():
    data = request.form
    
    slug =  data['slug']
    jobtitle=  data['jobtitle']
    company=  data['company']
    about=  data['about']
    description =  data['description']
    requirements = data['requirements']
    jobtype =  data['jobtype']
    location = data['location']
    industry = data['industry']
    salary =  data['salary']
   
    
    job_instance = db('jobs')
  
    job_rows = job_instance.select(condition=f"WHERE jobtitle='{jobtitle}'")
   
    
    if len(job_rows):

        
        print(job_rows[0])

    else:
      
       job_instance.insert("slug, jobtitle, company, about, description, requirements, jobtype, location, industry, salary", f"'{slug}', '{jobtitle}', '{company}', '{about}', '{description}', '{requirements}', '{jobtype}', '{location}', '{industry}', '{salary}'")
       
    return f"{jobtitle} job added from {company} by {slug}"



@app.route('/get_job', methods=["GET"])

def get_job_route():
    job_instance = db('jobs')
    
    tmp_jobs = []

    job_rows = job_instance.select()

    for row in job_rows:
        tmp_job = {
            "id": row[0],
            "slug":row[1],
            "jobtitle":row[2],
            "company":row[3],
            "about":row[4],
            "description":row[5],
            "requirements":row[6],
            "jobtype":row[7],
            "location":row[8],
            "industry":row[9],
            "salary":row[10]
        }
        
        tmp_jobs.append(tmp_job)
        
    jobs_dict ={
        "jobs": tmp_jobs
        }
    return jobs_dict

@app.route('/get_job/<job_slug>', methods=["GET"])
def get_info_route(job_slug):
    job_instance = db('jobs')

    job_rows = job_instance.select(condition=f"WHERE slug='{job_slug}'")

    if len(job_rows):
        row = job_rows[0]

        tmp_job = {
            "id": row[0],
            "slug":row[1],
            "jobtitle":row[2],
            "company":row[3],
            "about":row[4],
            "description":row[5],
            "requirements":row[6],
            "jobtype":row[7],
            "location":row[8],
            "industry":row[9],
            "salary":row[10]  
        }

        return tmp_job
    else:
        return {}

@app.route('/suscribe_job', methods=["POST"])
def suscribe_job_route():
    data = request.form
    
    emailaddress =  data['emailaddress']
    email_instance = db('suscribe')
    
    rows = email_instance.select(condition=f"WHERE emailaddress='{emailaddress}'")
   
    if len(rows):
        print(rows[0])
    else:
        
        email_instance.insert("emailaddress", f"'{emailaddress}'")
        
        return f"You just suscribed by {emailaddress}"
