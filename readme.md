# Submission (Abhishek Thakur):

# [Document for running code](Document_Submission\WSD_assignment_flask_qr_code.docx)


# Docker and Flask

For this assignment you will be creating a flask application to generate a QR code based on form input.  All you need
is to type the code into main.py that is in the photos below and practice the commands in the video.

# Submission Requirements:

Create a text document and put a screenshot of your form and a screenshot of the QR code that the form generates and upload to canvas

## Lesson Video

[Instructor Video](https://youtu.be/5Ca4kUSNA68)

## Readings - No, really you should read these

* [How to Dockerize a Flask  Application](https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/)
* 
## Bonus Task - Good Docker practice, it demonstrates using JavaScript / NodeJS

* https://docs.docker.com/get-started/

## Code Photos
1. [main.py - part 1](readme_images/main-part1.png)
2. [main.py - part 2](readme_images/main-part2.png)

## CURL Command Line Command from inside the container in the video
curl -X POST http://flask:8080 -H "Content-Type: application/x-www-form-urlencoded" -d "qrurl=http://wwww.yahoo.com" --output 


## Command Reference - No Particular Order

* docker build -t kaw393939/python312 . <- builds image called "kaw393939/python312"
* docker run -it kaw393939/python312   <- Runs python type exit() to get out
* docker run -it kaw393939/python312 <- Runs the default main.py CMD in the dockerfile
* docker run -it kaw393939/python312 app.py  <-overrides cmd/command in dockerfile to run app.py instead
* docker compose up --build < runs the service defined through the docker-compose.yml file that tells it to build the
  Dockerfile
* docker compose up <- Runs the program but doesn't build a new image
* docker run --volume /Users/keithwilliams/Desktop/fall2022/qrprog/qr_generator_service/images:/home/myuser/images
  Note:  You need to build each time you change your dockerfile
* docker exec -it <container ID> bash allows you to login to the running container
* docker tag local-image:tagname new-repo:tagname <renames the image
* docker push new-repo:tagname <pushes the image to docker hub
* docker login <- login to dockerhub if it says access denied when you try to push
curl -X POST https://reqbin.com/echo/post/form
   -H "Content-Type: application/x-www-form-urlencoded" 
   -d "param1=value1&param2=value2"


