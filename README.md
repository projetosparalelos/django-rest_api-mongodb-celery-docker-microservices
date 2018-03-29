Microservices architecture based web application

This is and example web application based on microservices architecture. It has 3 decoupled and scalable services:

1. Products Management
2. Order Management
3. Email Sending

#Technology Stack:

Python
Django/Django REST Framework
Celery
Rabbitmq
Mongodb
Nginx
Docker
Swagger UI

Python used as the backend development language. Django used as the backend framework. Django REST Framework or DRF used as the REST API development framework, celery used as the async task manager, Rabbitmq used as a message broker, Mongodb used as the database backend, Nginx used as the API gateway and finally docker used as the deployment method. Swagger used for documenting API

Each services have their seperate database completely decoupled. Nginx sits in front of each of the services to abstract all the microservices API endpoints into single one.

For testing:

1. Clone the repo
2. Run ```docker-compose build``` while inside the services folder
3. After docker completes all the building staffs, run ```docker-compose up -d``` to run each microservices.
4. Now go to your localhost, docker machine ip or server ip to access the API endpoints.
5. API endpoints: please see /api/v1/{services}/docs/

Deployed and tested in a real production server.
