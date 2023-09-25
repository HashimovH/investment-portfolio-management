
# Investment App

This app is light weight investment flow which allows clients to buy shares from different stocks and track their gain/loss over some period of time

# Stack

### Back-end
- Python (FastAPI)
- Postgres - Database
- Docker and Docker Compose - Containerization
- Pytest - Testing

### Front-end
- React
- React Router - Routing
- ESLint - Linting
- Axios - API Requests


# Local Setup

## Prerequisite
- Installed `Docker` and `Docker Compose`
- Internet Connection
- Git

First you need to clone the repository into your local machine as follows:
```
git clone git@github.com:HashimovH/investment-portfolio-management.git
```

Then change directory to project directory by running

```
cd investment-portfolio-management
```

command.

In next step, thanks to having Docker, using the following command will make the project up and running

```
docker-compose up -d --build
```

# Implementation details

## Back End

I tried to stick to the Clean Architecture principles while developing back-end. Splitted project into `repository`, `service`, `http`, `domain` layers to increase maintainability.

#### More plans - if having more time
- Using sockets for real-time stock and price changes
- Using high-level locks for transaction process
- Adding K8s manifest files
- Implementing Metrics, Grafana and Prometheus

## Front End
Since I am back-end heavy Software Engineer, I did my best to build clean Front-end. I followed UI mocks from the description and created similar UI by using `Bootstrap` classes and `flex` CSS.

`Axios` was my tool to make API requests to fetch or post data.

### More plans - if having more time
- Using Interceptor to automatically add token into headers in each request

# Screen Recording
https://drive.google.com/file/d/1OueDtzRDkjE9Jae-fbm7OfhnVvZJBFAB/view?usp=sharing

Overall Time Spent: ~23 Hours. (Saturday, Sunday, Monday)
