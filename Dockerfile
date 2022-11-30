FROM python:3.12.0a2-buster
RUN apt-get update &&\
    /usr/local/bin/python3 -m pip install --upgrade pip &&\
    /usr/local/bin/python3 -m pip install --upgrade setuptools &&\
    adduser myuser
ENV PATH="/home/myuser/.local/bin:${PATH}"
ENV FLASK_APP=main.py
ENV FLASK_RUN_PORT=8080
ENV FLASK_DEBUG=TRUE
ENV QR_CODE_IMAGE_DIRECTORY='static'
ENV QR_CODE_DEFAULT_URL='https://www.njit.edu'
ENV QR_CODE_DEFAULT_FILE_NAME='default.png'
WORKDIR /home/myuser
COPY --chown=myuser:myuser . .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["runuser", "-u", "myuser", "--", "python3", "-m", "flask", "run", "--host=0.0.0.0"]
