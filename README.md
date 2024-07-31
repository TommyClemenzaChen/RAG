# project_name RAG 

project_description: api for RAG

## Installation

From source:

```bash
git clone https://github.com/TommyClemenzaChen/RAG
cd RAG
pip install -r requirements.txt
```

## Documents for rag:

Creates a directory to store your data
```
cd src
mkdir data
cd data
mkdir data_source
cd data_source
```

Download any pdfs and put in data_source directory

Example:
```
wget https://arxiv.org/pdf/2407.09141.pdf
```

Call the database script to convert all the pdfs into a vector database

```
cd ../../../
python src/create_database.py
```


## Executing(local)



Just run:

```bash
$ python app.py
```

# IGNORE THE REST NOT FINSIHSED


[To see the help message and usage instructions.

## First run

```bash
project_name create-db   # run once
project_name populate-db  # run once (optional)
project_name add-user -u admin -p 1234  # ads a user
project_name run
```

Go to:

- Website: http://localhost:5000
- Admin: http://localhost:5000/admin/
  - user: admin, senha: 1234
- API GET:
  - http://localhost:5000/api/v1/product/
  - http://localhost:5000/api/v1/product/1
  - http://localhost:5000/api/v1/product/2
  - http://localhost:5000/api/v1/product/3


> **Note**: You can also use `flask run` to run the application.]: #
