FROM python:3

WORKDIR /usr/src/speech_rec/src

RUN apt-get update

RUN apt-get install -y swig libpulse-dev build-essential

RUN pip install --no-cache-dir SpeechRecognition pocketsphinx

COPY . . 

CMD ["python", "./src/demo.py"]
