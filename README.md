# News Buster

<br />
<div id="top"></div>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><b><a href="#flow-of-project">Project Flow</a></b></li>
      </ul>
    </li>
    <li><a href="#getting-started">Getting Started</a></li>
      <ul>
        <li><a href="#prerequisite">Prerequisite</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

<div id="about-the-project"></div>

News filter Check the authenticity of the same news what we receive & response to someone's request to confirm
authenticity.

### Built With

<div id="built-with"></div>
This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for
the acknowledgements section. Here are a few examples.

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Celery](https://flask.palletsprojects.com/en/2.0.x/patterns/celery/)
* [RabbitMQ](https://www.rabbitmq.com/)
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

<!-- flow-of-project -->

### Project Floor Plan

<div id="flow-of-project"></div>
<!-- TODO: finalising the code flow here -->

- Required APIs:
    * Adding new User
    * Adding new preference option
    * Adding new preference to User
    * Email confirmation by user

- Database UML:
  ![database_uml.png](readme_content/database_uml.png)

- Process Diagram:
    <div id="image"></div>

  ![Mind Mapping.png](readme_content/flow_diagram.jpg)
    <br/>
_Above image depicts only a first draft ideology by [cupid-22](https://github.com/cupid-22) and there can be more solid
ways to make this code flow fireproof. This is the initial concept from the provided document by the institution._
<li>Process Description:</li>
<ul>
    <li>Cron job (Or libs replicating such functionality I am opting celery beat as it is integrated to the task queue) will keep the process in loop.</li> 
    <li>Individual task divided into multiple sub task using interface, Ideally, so whenever new site comes it is easily to add new functionality without alteration of new code.</li>
    <li>All the task below will go into different task so they can remain non-blocking, also the task from celery will be handled by RabbitMQ which indeed daemonize the process.</li>
    <li>fetch_news: Retrieve all the possible sites so as to Fetch news from them, and insert these news into the database with status of SUCCESS.</li>
    <li>Categorize the fetched news based on the keyword received in the title or the body, and once categorised it can be changed to status CATEGORIZED.</li>
    <li>Take up all the categorized news and find the users subscribed to the same tag preference and also put an entry in the NewsAuthenticity table where it will wait for the user to respond with a status of Authenticity.</li>
    <li>Check NewsAuthenticity for any unsent package and deliver them flagging the id with sent,wait for the user to respond which will be caught by Flask API GET endpoint where it update an particular resource flagging the authenticity of the news sent to user.</li>
    <li>Check NewsAuthenticity for any unsent package and deliver them flagging the id with sent,wait for the user to respond which will be caught by Flask API GET endpoint where it update an particular resource flagging the authenticity of the news sent to user.</li>
</ul>
<p align="right">(<a href="#image">back to image</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

<div id="getting-started"></div>
All the needed requirements are exported into the `requirements.txt` file which can be executed below-mentioned command.
Project is ready to deploy on heroku servers.

### Prerequisites

<div id="prerequisite"></div>

* Desired python and pip version.
  ```sh
  python >= 3.8.12
  pip >= 21.3.1
  ```

* Other requirements.<br>
    - [rabbitMQ](https://computingforgeeks.com/how-to-install-latest-rabbitmq-server-on-ubuntu-linux/)
    - [postgreSQL](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart)

### Installation

<div id="installation"></div>

1. Clone the repo
   ```sh
   git clone https://github.com/cupid-22/news-buster.git
   ```
2. Install pip packages
   ```sh
   pip install -r requirements.txt 
   ```
3. Initiate rabbitMQ as Message Broker
   ```sh
   sudo systemctl start rabbitmq-server.service
   ```
   ![img.png](readme_content/img.png)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

<div id="contributing"></div>

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also
simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>





<!-- CONTACT -->

## Contact

<div id="contact"></div>

Gaurav Mishra - [@Linkedin](https://www.linkedin.com/in/gaurav-mishra-work/) - gaurav.mishra.cx@gmail.com

Project Link: [https://github.com/cupid-22/news-buster.git](https://github.com/cupid-22/news-buster.git)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

<div id="acknowledgments"></div>

This project takes some boilerplate code from some of these sites and understanding from others.

* [Automated Web Scraping with python and celery](https://codeburst.io/automated-web-scraping-with-python-and-celery-ac02a4a9ce51)
* [ReadME boilerplate](https://github.com/othneildrew/Best-README-Template/edit/master/README.md)
* [Getting Started With Celery](https://www.youtube.com/watch?v=THxCy-6EnQM)
* [Simple Relationships](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#a-minimal-application)
* [Celery Beat](https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html#entries)

<p align="right">(<a href="#top">back to top</a>)</p>
