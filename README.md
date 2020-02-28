# HouseOfSaud
 
Saudi Arabia's Royal Family is one of the most powerful monarchies in the world but also the least well known. This website
aims to bridge this gap in knowledge by presenting a clear view of the first generation of the ruling branch
of Saudi Arabia. 

Data has been scraped from Google Search results (using Python's scrapy library)  and stored in a mongoDB database. A Python Flask backend was used for the API endpoints and React JS was used for the front end.


# Setup Instructions (Server)

1. Install the latest versions of python3, pip3 and python3-venv.

2. In this directory, run the following command to configure a virtual environment:

        $ python3 -m venv venv

3. Activate the virtual environment with the following command:

        $ source venv/bin/activate

   If using windows, run the following instead:

        $ venv\Scripts\activate

4. Install the dependencies from requirements.txt:

        (venv) $ pip3 install -r requirements.txt

6. Navigate to /HouseOfSaud/gitRep/flask-backend  and execute <code>flask run</code>

        (venv) $ flask run
        * Serving Flask app "pymongoexample"
        * Environment: production
        WARNING: This is a development server. Do not use it in a production deployment.
        Use a production WSGI server instead.
        * Debug mode: off
        * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    
    Leave this terminal running for the duration of your session.

Note: 
```js
    deactivate - Step out of the virtual env.
```

# Setup Instructions (Client)

1. Create a separate terminal window and navigate to /HouseOfSaud/gitRep/saud-frontend and execute <code>npm install</code>

2. After this run <code>npm start</code> and you should be taken to http://localhost:3000 where the app will be running.

