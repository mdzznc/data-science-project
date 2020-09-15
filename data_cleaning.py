# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

df = df[df['Salary Estimate'] != '-1']
salary = df['Salary Estimate'].apply(lambda x:
                                     x.replace(' (Glassdoor Est.)','').replace('k','').replace('$','').replace('CA',''))

df['min_salary'] = salary.apply(lambda x: x.split("-")[0])
df['max_salary'] = salary.apply(lambda x: x.split("-")[1])
df['avg_salary'] = (df['min_salary'].apply(lambda x: float(x)) + df['max_salary'].apply(lambda x: float(x)))/2

df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)

df['python_required'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

loc = df["Location"].value_counts()

df_out = df.drop(columns = ['Headquarters', 'Competitors', 'Sector', 'Industry', 'Founded'])
df_out.to_csv('data_cleaned.csv',index = False)