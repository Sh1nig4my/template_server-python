##PYTHON##

#TODO installazione python locale. (Possibilmente LTS).
https://www.python.org/downloads/

#TODO aggiugnere spiegazione ogni import
#Pacchetti da installare 
pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install pymysql
pip install pydantic[email] 

#Runnare il server
uvicorn main:app --reload  

#Swagger
http://127.0.0.1:8000/docs

#Architettura
project/
├── main.py
├── database.py         # Configurazione del DB (engine, session, get_db) 
├── models/
│   └── user.py         # Modello ORM (SQLAlchemy)
├── schemas/
│   └── user.py         # Schemi Pydantic (DTO) per input/output
├── repositories/
│   └── user_repository.py  # Funzioni per interagire con il DB
├── services/
│   └── auth_service.py     # Logica di business per l'autenticazione
└── routes/
    └── auth.py         # Endpoints/Controller per login, registrazione, logout



####EXTRA####
#Frontend

#Index
http://127.0.0.1:8000/static/index.html


project/
├── main.py
├── database.py         # Configurazione del DB (engine, session, get_db)
├── models/
│   └── user.py         # Modello ORM (SQLAlchemy)
├── schemas/
│   └── user.py         # Schemi Pydantic (DTO) per input/output
├── repositories/
│   └── user_repository.py  # Funzioni per interagire con il DB
├── services/
│   └── auth_service.py     # Logica di business per l'autenticazione
├── routes/
│   └── auth.py         # Endpoints/Controller per login, registrazione, logout
└── static/             # File statici per il frontend
    ├── index.html
    ├── css/
    │   └── styles.css
    └── js/
        └── script.js




