from flask import Flask, request
from flask_cors import CORS
import json
from datetime import datetime

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

    jobtitle=  data['jobtitle']
    company=  data['company']
    about=  data['about']
    description =  data['description']
    requirements = data['requirements']
    jobtype =  data['jobtype']
    location = data['location']
    industry = data['industry']
    salary =  data['salary']
    slug =  data['slug']
    #date= data['date']
    
    #date_obj = datetime.strptime(date, '%a, %d %b %Y %H:%M:%S %Z')
    #formatted_date = date_obj.strftime('%Y-%m-%d')
    #date = formatted_date
    
    job_instance = db('jobs')
  
    job_rows = job_instance.select(condition=f"WHERE jobtitle='{jobtitle}'")
   
    
    if len(job_rows):

        
        print(job_rows[0])

    else:
      
       job_instance.insert("jobtitle, company, about, description, requirements, jobtype, location, industry, salary, slug", f"'{jobtitle}', '{company}', '{about}','{description}','{requirements}','{jobtype}','{location}', '{industry}','{salary}','{slug}'")
       
    return f"{jobtitle} job added from {company}"



@app.route('/get_job', methods=["GET"])

def get_job_route():
    tmp_jobs = []

    job_instance = db('jobs')

    job_rows = job_instance.select()

    for row in job_rows:
        tmp_job = {
            "id": row[0],
            "jobtitle":row[1],
            "company":row[2],
            "about":row[3],
            "description":row[4],
            "requirements":row[5],
            "jobtype":row[6],
            "location":row[7],
            "industry":row[8],
            "salary":row[9],
            "slug":row[10]
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

        tmp_prod = {
            "id": row[0],
            "jobtitle":row[1],
            "company":row[2],
            "about":row[3],
            "description":row[4],
            "requirements":row[5],
            "jobtype":row[6],
            "location":row[7],
            "industry":row[8],
            "salary":row[9],
            "slug":row[10]
        }

        return tmp_prod
    else:
        return {}