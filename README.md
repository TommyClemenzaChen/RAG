# RAG project

## System design overview:
![image](https://github.com/user-attachments/assets/f4fc4426-e549-4da7-a788-d9ecddfa241f)


## Installation

From source:

```bash
git clone https://github.com/TommyClemenzaChen/RAG
cd RAG
pip install -r requirements.txt
```

## Creating database for retrieval(run before using the app):

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
## Executing(Docker)

Building images:
```
docker build --no-cache -t rag:latest .
```

Running: 
```
docker run -p 8000:8000 rag:latest   
```

## Executing(local)



Just run:

```bash
$ python app.py
```

