from datetime import date
import csv
import os
# https://github.com/VoIlAlex/readme-cli
# BEWARE: Some ugly code incomming!
class MyClass():
    def __init__(self):
        self.p0n = str(input(
            "Enter Project ID: ") or
            "p00")
        pass

    def get_project_details(self):
        self.projectCreationDate = date.today().strftime("%d %b %Y") 
        
        self.projectTitle = str(input(
            "Enter Project Title: ") or
            "<Project Title>")
        self.tldr = str(input(
            "Enter Short Description: ") or
            "<Short Description>")
        
        self.algorithm = str(input(
            "Enter Algorithm used: ") or
            "<Algorithm>")
        self.domain = str(input(
            "Enter Domain of project: ") or
            "<Domain of project>")
        
        self.nbFileName = str(input(
            "Enter Google Colab File Name: ") or
            "<Google Colab File Name>")
        self.nbLink = str(input(
            "Enter Google Colab File Link: ") or
            "<Google Colab File Link>")
        
        self.sourceName = str(input(
            "Enter Original content title: ") or
            "<Original content title>")
        self.sourceLink = str(input(
            "Enter Original content link: ") or
            "<Original content link>")
        pass

    def gen_p0n_md_files(self):
        # projects.csv -> "Date","Name","TLDR","Algorithm","NotebookName","NotebookLink"
        # README.md -> everything!!
        readme_content = ''
        with open('p0n/README.md','r') as f:
            readme_content = ''.join(f.readlines())
            pass
        with open(self.p0n+'/README.md', 'w+') as fp:
            readme_content = readme_content.format(
                    projectTitle = self.projectTitle,
                    domain = self.domain,
                    algorithm = self.algorithm,
                    tldr = self.tldr,
                    nbFileName = self.nbFileName,
                    nbLink = self.nbLink,
                    sourceName = self.sourceName,
                    sourceLink = self.sourceLink,
                    p0n=self.p0n,
                )
            fp.write(readme_content)
            pass
    def gen_p0n_py_files(self):
        app_content = ''
        with open('p0n/App.md','r') as f:
            app_content = ''.join(f.readlines())
            pass
        with open(self.p0n+'/App.py','w') as fp:
            app_content = app_content.format(
                tldr = self.tldr,
                projectTitle = self.projectTitle,
                p0n = self.p0n.upper(),
            )
            fp.write(app_content)
            pass
        init_content = ''
        with open('p0n/__init__.md','r') as f:
            init_content = ''.join(f.readlines())
            pass
        with open(self.p0n+'/__init__.py','w') as fp:
            init_content = init_content.format(
                tldr = self.tldr,
                p0n = self.p0n,
                projectTitle=self.projectTitle,
            )
            fp.write(init_content)
            pass
        pass
    def gen_p0n_files(self):
        if not os.path.exists(self.p0n):
            os.makedirs(self.p0n)
        self.gen_p0n_md_files()
        self.gen_p0n_py_files()
        pass
    def gen_project_csv(self):
        CSV_FILE_NAME = "projects.csv"
        # "Date","Name","TLDR","Algorithm","NotebookName","NotebookLink"
        fieldNames = ["Date","Name","TLDR","Algorithm","NotebookName","NotebookLink"]
        List=[
            self.projectCreationDate,
            self.projectTitle,
            self.tldr,
            self.algorithm,
            self.nbFileName,
            self.nbLink,
        ]
        with open(CSV_FILE_NAME, 'a', newline='') as f_object:
            writer_object = csv.writer(f_object,quoting=csv.QUOTE_ALL)
            writer_object.writerow(List)
            f_object.close()
        pass
    def gen_project_meta_files(self):
        self.gen_p0n_files()
        self.gen_project_csv()
        pass
    