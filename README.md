# Amdari_assessment

The model is stored as a pickel file with the name rf_fraud_detection_pipeline.pkl
I used FastAPI for the deployment even though I can also work with strealit

Set up
1. Install requirements.txt as provided using the python package manager pip
--pip install requirements.txt, installing in a virtual environment is recommended

2. activate the environment and run
-- uvicorn main:app -- reload 
this starts up the server running at localhost and port 8000

3. visit localhost:8000/docs to use the FastAPI swagger UI for the endpoints

4. Click on Try it

5. Edit the JSON file provided and provide the data needed and click on execute

6. Scroll down to see the models prediction

