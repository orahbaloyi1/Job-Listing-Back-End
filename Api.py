from flask import Flask, send_file, request
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
       # return(job_rows) #Add new
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






 
  #job_id = None #new add
 #job_id = job_rows[0][0]
        # 
 
  # company_instance = db('company') #new add

 
  #return f'Submission from {company_id}'

# company_id = company_instance.insert("company_", job_id", f"'{json.dumps(cart)}', {job_id}")
 # job_id = jobs_instance.insert("jobtitle, company", f"'{jobtitle}', '{company}'")



 #"name": row[1],
 #           "email": row[2],
 #           "jobtittle":row[3]"
 #           "companyname":row[3]
  #          "location": row[2],
  #          "aboutcompany": row[3],
   #         "desc": row[4]
   #         "Requirements":[]
   #         "type"
    #        "in"