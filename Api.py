from flask import Flask, request
from flask_cors import CORS
import json

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

    jobtitle =  data['jobtitle']
    company = data['company']
    locations =  data['locations']
    about = data['about']
    description =  data['description']
    requirements = data['requirements']
    typ =  data['typ']
    industry = data['industry']
    salary =  data['salary']
    dat = data['dat']


    job_instance = db('jobs')
  
    job_rows = job_instance.select(condition=f"WHERE jobtitle='{jobtitle}'")
   
    
    if len(job_rows):
        
        print(job_rows[0])

    else:
      
       job_instance.insert("jobtitle, company, locations, about, description, requirements, typ, industry, salary, dat ", f"'{jobtitle}', '{company}', '{locations}', '{about}', '{description}', '{requirements}', '{typ}', '{industry}', '{salary}', '{dat}'")
    
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
            "locations":row[3],
            "about":row[4],
            "description":row[5],
            "requirements":row[6],
            "typ":row[7],
            "industry":row[8],
            "salary":row[9],
            "dat":row[10]

        }
        
        tmp_jobs.append(tmp_job)

    jobs_dict ={
        "jobs": tmp_jobs
    }

    return jobs_dict
##CREATE TABLE jobs (
	##id SERIAL PRIMARY KEY,
	##jobtitle TEXT NOT NULL,
	##company TEXT NOT NULL,
	##locations TEXT NOT NULL,
	##about Text NOT NULL,
	##description TEXT,
	##requirements TEXT NOT NULL,
	##typ TEXT NOT NULL,
	##industry TEXT NOT NULL,
	##salary DOUBLE PRECISION NOT NULL,
	##dat INT NOT NULL
	##);