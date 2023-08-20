# OpenAI-Flask-App
provides a solution to build and deploy a gpt chatbot with OpenAI API using Flask and docker.

To run the Flask app locally;
```
pip install -r requirements.txt
```

Replace the OpenAI key in the app.py:
```
api_key = 'OPENAI_API_KEY'
```

Run in the command line:
```
python app.py
```

To test it locally:
```
curl -X POST -H "Content-Type: application/json" -d "{\"query\": \"are you a dog person or a cat person?\"}"  http://localhost:5000/
```

