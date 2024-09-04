# custom_flask_app_logging

This repo includes a python flask application script which append a log to a log file each and every time we send an http request to the flask application running on port 5000 and a bash script which generate a curl request for the flask application on port 5000 each 60 seconds time interval.

This helps who ever doing an R&D work on custom application log ingestion to log management or any SIEM solution. (Primariy for Linux, but with minor modification you can use in Windows enviornment also.)

#Install Python3 Flask
  sudo apt install python3-flask

#Run the python script to turn up the flask web application (App runs on -> http://localhost:5000)
  python3 app.py

#Install curl
  sudo apt install curl

#Modify permissions and run the automated bash script to generate curl requests for with 60 seconds time interval (optional)
  chmod +x auto_curl.sh
  ./auto_curl.sh
