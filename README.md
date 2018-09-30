# DevOps Log Analysis

Udacity Full Stack Web Developer Logs Analysis Project
[Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Introduction

In this, we have to execute complex queries on a large database (> 1M rows) to extract interesting stats.

The database in question is a newspaper company database where we have 3 tables; `articles`, `authors` and `log`.
* `articles` - Contains articles posted in the newspaper so far.
* `authors` - Contains list of authors who have published their articles.
* `log` - Stores log of every request sent to the newspaper server.

## Motivation

For this project, I used Docker instead of Vagrant as recommended because I am more interested in Docker and Microservices. 

The structure of the application is microservices. Each services has its own Dockerfile where the dependencies are declared. 

The services are orchestrated and combined by the docker-compose.yml file.

    .
    ├── docker-compose.yml
    ├── src                     # Source Code
    │   ├── postgresql          # postgresql backing service
    │   └── python              # main application service written in python
    └── ...

*entrypoint.sh* ensures containers are brought up in succinct order: postgresql is needed to come up first because it is a backing service.

Inspired by *The Twelve-Factor Application Design* (https://12factor.net/)

## Benefits and Features

* Containers (Docker) are much more efficient than Virtual Machines (Vagrant)
* Dependencies are declared, injected, decoupled and source controlled
* Fully Automated, Deterministic and Reproducible Build
* Removes all manual steps that will cause issues for CI/CD

## Requirements

Docker (https://www.docker.com/get-started)

## Installing

Clone the Project using Git LFS

```bash
git lfs clone ...
```

Open Terminal && cd into Project

```bash
docker-compose up --build
```

## Teardown

```bash
docker-compose down
```
