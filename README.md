[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

![image](https://user-images.githubusercontent.com/44437166/183901196-8b47f337-4aa0-4ab7-a6e2-f7079c536618.png)

![image](https://user-images.githubusercontent.com/44437166/183892232-53f7e0e5-0bcb-4f54-bc0e-5d8c76248af0.png)


![image](https://user-images.githubusercontent.com/44437166/181994412-9c3c82d1-02e3-44ac-8708-e6d7617ecf3d.png)

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/benbel376/ELT_Pipeline_Project_2">
  </a>
  <h1 align="center">ELT Pipeline Project 2</h1>
  <p align="center">
    A fully dockerized ELT pipeline using MySQL, PostgreSQL, Airflow, DBT, Redash and Superset.
    <br />
    <a href="https://sensordataelt.herokuapp.com/index.html"><strong>Explore the docs »</strong><a>
    <br />
    <br />
    ·
    <a href="https://github.com/benbel376/ELT_Pipeline_Project_2/issues">Report Bug</a>
    ·
    <a href="https://github.com/benbel376/ELT_Pipeline_Project_2/issues">Request Feature</a>
    .
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)
The objective of this project was to migrate an ELT pipeline developed for the week 11 challenge using(MYSQL, DBT, Apache Airflow, and Redash) to a more scalable and robust ELT pipeline. This was accomplished by changing the two main components, namely the MySQL data warehouse to Postgres and the Redash dashboard to Superset.

### Built With

Tech Stack used in this project
* [MYSQL](https://getbootstrap.com)
* [PostgreSQL](https://www.postgresql.org/)
* [Apache Airflow](https://jquery.com)
* [dbt](https://laravel.com)
* [Redash](https://laravel.com)
* [Superset](https://superset.apache.org/)

├── airflow
│    ├── dags
│    │   └── workflow.py
│    ├── logs
│    │   └── test
│    └── plugins
│        └── test    ```
├── data
│   ├── extracted_features.csv
│   └── ...
├── dbt
│   ├── models
│   │   └── adludio_models
│   │       ├── schema.yml
│   │       └── trans_join.sql
├── docker
│   ├── docker-compose-airflow.yml
│   ├── docker-compose-postgres.yml
│   ├── docker-compose-redash.yml
│   └── dockerfiles
│       ├── airflow
│       │   ├── dockerfile
│       │   └── requirements.txt
│       └── postgres
│           └── dockerfile
├── models
├── notebooks
│   ├── EDA.ipynb
│   ├── experiment.ipynb
│   ├── feature_extraction.ipynb
│   ├── mlruns
│   │   └── ...
│   └── modeling.ipynb
├── scripts
│   ├── python
│   │   ├── connection_manager.py
│   │   ├── feature_extractor.py
│   │   ├── ingest_global.py
│   │   ├── modeling_utils.py
│   └── sql
│       ├── clean_data.sql
│       ├── extraction.sql
│       ├── ingestion.sql
│       ├── loading.sql
│       ├── postgres_init.sql
│       └── redash_visuals.sql
└── setup.sh

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Make sure you have docker installed on local machine.
* Docker
* DockerCompose
  
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/benbel376/ELT_Pipeline_Project_2
   ```
2. Datawarehouse
   ```sh
   cd sensor_data_elt
   ```
3. Run
   ```sh
    docker-compose up
   ```
4. Can access and Modefy the default configrations for each tool using the `.env` files.


<!-- USAGE EXAMPLES -->
## Usage

### Adminer: 
Adminer (formerly phpMinAdmin) is a full-featured database management tool written in PHP. Used to access MYSQL and Postgres Databases.
- MYSQL:
   ```sh
   Navigate to `http://localhost:8080/` on the browser
   use `mysqldb` server
   use `dbtdb` database
   use `root` for username
   use `root` for password
   ```
- Postgress:
   ```sh
   Navigate to `http://localhost:8080/` on the browser
   use `postgres-dbt` server
   use `dbtdb` database
   use `dbtuser` for username
   use `pssd` for password
   ```
### Airflow: 
  Airflow is used for aurchestration and automation.
   ```sh
   Navigate to `http://localhost:8080/` on the browser
   use `admin` for username
   use `admin` for password
   ```
### DBT:
DBT is used for cleaning and transforming the data in the warehouses. 
- Airflow is used for automation of running and testing dbt models
- navigate to `https://sensordataelt.herokuapp.com/index.html` to access dbt docs

### Redash
   ```sh
   open terminal and execute `docker-compose run — rm server create_db`
   using adminer create a user and grant read access
   Navigate to `http://localhost:5000/` on the browser
   ```
### Superset
- navigate to `localhost:8088` to access Airflow 



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Biniyam Belayneh - biniyambelayneh376@gmail.com

Project Link: [https://github.com/benbel376/ELT_Pipeline_Project_2](https://github.com/benbel376/ELT_Pipeline_Project_2)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [10 Academy](https://www.10academy.org/)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/benbel376/ELT_Pipeline_Project_2.svg?style=for-the-badge
[contributors-url]: https://github.com/benbel376/ELT_Pipeline_Project_2/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/benbel376/ELT_Pipeline_Project_2.svg?style=for-the-badge
[forks-url]: https://github.com/benbel376/ELT_Pipeline_Project_2/network/members
[stars-shield]: https://img.shields.io/github/stars/benbel376/ELT_Pipeline_Project_2.svg?style=for-the-badge
[stars-url]: https://github.com/benbel376/ELT_Pipeline_Project_2/stargazers
[issues-shield]: https://img.shields.io/github/issues/benbel376/ELT_Pipeline_Project_2.svg?style=for-the-badge
[issues-url]: https://github.com/benbel376/ELT_Pipeline_Project_2/issues
[license-shield]: https://img.shields.io/github/license/benbel376/ELT_Pipeline_Project_2.svg?style=for-the-badge
[license-url]: https://github.com/benbel376/ELT_Pipeline_Project_2/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/biniyam-belayneh-demisse-42909617a//

