import psycopg2
import psycopg2.extras
import csv
import os
from config import password
# aws rds 

params = {
    "host"      : "rds-pg-jobs.chfavwsr5bmp.us-east-1.rds.amazonaws.com",
    "dbname"    : "postgres",
    "user"      : "postgres",
    "password"  :  password, 
    "port" : "5432"     
}

conn = psycopg2.connect(**params)

with conn.cursor() as cursor:
    
    with open('data/state.csv', 'r') as f:    
        cmd = 'COPY economy.state("state_id", "city", "state") FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
    
        cursor.copy_expert(cmd, f)
    conn.commit()
    
    with open('data/company.csv', 'r') as s:    
        cmd = 'COPY economy.company("company_id", "state_id", "company_name", "rating", "size", "founded", "type_of_ownership", "industry", "sector", "revenue", "headquarter") FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
    
        cursor.copy_expert(cmd, s)
    conn.commit()

    with open('data/job.csv', 'r') as t:    
        cmd = 'COPY economy.job("job_id", "job_title", "easy_apply", "avg_salary","min_salary", "max_salary", "company_id", "state_id") FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
    
        cursor.copy_expert(cmd, t)
    conn.commit()









 