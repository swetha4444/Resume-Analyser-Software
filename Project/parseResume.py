import re
import docx2txt
import csv
import os
import networkx as nx
import matplotlib.pyplot as plt

def remove_junk(txt) :
    if '.' in txt :
        txt = txt.split(".")[0]
    if '\n' in txt :
        txt = txt.split('\n')[0]
    return txt

def InitializeCSV() :
    with open("data.csv",'w') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'phone', 'skills' , 'address' , 'workExp','email','about'])

def docxToCsv (filename,single = 1) :
    data = docx2txt.process(filename)
    name = remove_junk(re.search(r'[Name|NAME]\s*:\s*[A-Za-z]*\s*[A-Za-z]*\s*\.*',data).group().split(":")[1])
    phone_no = remove_junk(re.search(r'Phone No\s*:\s*\+?[0-9]*\s?[0-9]+\s*\.*',data).group().split(":")[1])
    email = re.search(r'Email\s*:[\S\s]*:',data).group().split(":")[1]
    email = email.rsplit('.', 1)[0]
    address = remove_junk(re.search(r'Address\s*:.*\n',data).group().split(":")[1])
    work_experience = re.search(r'Work Experience\s*:[\S\s]*:',data).group().split(":")[1]
    work_experience = work_experience.rsplit('.', 1)[0]
    skills = remove_junk(re.search(r'Programming Languages\s*:\s*[A-Za-z\s*,\s*0-9]*\s*\.*',data).group().split(":")[1].split(".")[0])
    about =  re.search(r'Summary\s*:[\S\s]*:',data).group().split(":")[1]
    about = about.rsplit('.', 1)[0]
    list =  [name,phone_no,skills,address,work_experience,email,about]
    if single :
        InitializeCSV()
    with open("data.csv",'a') as f:
        writer = csv.writer(f)
        writer.writerow(list)

def FolderOfDocxToCSV (path) :
    files_list = os.listdir(path)
    InitializeCSV()
    for i in files_list :
        docxToCsv(path+"/"+i,0)
