# Farm Calendar Application Setup

This README provides detailed instructions on setting up the PostgreSQL database and pgAdmin for the Farm Calendar
application using Docker.

## Prerequisites

Before you start, make sure Docker and Docker Compose are installed on your system.
Later versions of Docker also include now Docker Compose, but it is used as `docker compose` instead of `docker-compose`.

## Service Setup

### Setting up Configurations (.env file)
If you wish to start up this Farm Calendar service from this repository, you'll need to first copy the `.env.sample` file into a new file called `.env`, which will be the source of all configurations for this service, and its database.

In this new `.env` file you should change the configurations of the service to meet your deployment scenario. We strongly suggest changing configurations for the default usernames and passwords of the services used.

The details for the configuration variables that are not self-explanatory are:
* **GATEKEEPER_LOGIN_URL**: This should be set to the OpenAgri Gatekeeper login endpoint if you wish to use this as the authentication method. Alternativelly, not setting this variable will fall-back to a local session based user authentication on this FarmCalendar service.
* **JWT_SIGNING_KEY**: If using the Gatekeeper for authentication, this should be set to the JWT signing key used by the Gatekeeper.


## Running
There is already a simple and ready to use `docker-compose.yml` file for your convinience. Nonetheless, you should be able to use the existing file as a base, and adapt it to your own deployment setup.

To run the service, execute the following command:
```
$ docker compose up -d
```

## Stopping/Restarting

To stop the service related containers, run:

```commandline
docker compose stop
```
And to start again the stopped containers:

```commandline
docker compose start
```

To stop and remove the containers, use:

```commandline
docker-compose down
```

## More Examples of Setup
As mentioned before, you can extend the existing `docker-compose.yml` to be more complex and to best fit your deployment scenario. The following setup includes a PgAdmin4 service in addition to the DB and FarmCalendar, while using a named (shared_network_fc) shared bridge network in docker. This setup also exemplifies the use of a external volume to hold the database data, therefore removing the database container will not remove the database information.

This setup also requires the addition of the following configurations to your `.env` file (replacing the placeholder values with the actual ones):
```
PGADMIN_DEFAULT_EMAIL=<YourEmailHere>
PGADMIN_DEFAULT_PASSWORD=<YourPasswordHere>
```

Here's the `docker-compose.yml` for setting up PostgreSQL and pgAdmin:

```yaml
version: '3.9'

services:
  postgres_fc:
    image: postgres:latest
    restart: always
    container_name: postgres_fc_container
    env_file:
      - .env
    ports:
      - "5432:5432"
    volumes:
      - postgres_data_fc:/var/lib/postgresql/data
    networks:
      - shared_network_fc

  pgadmin_fc:
    image: dpage/pgadmin4
    container_name: pgadmin_fc_container
    restart: always
    env_file:
      - .env
    ports:
      - "8088:80"
    networks:
      - shared_network_fc
    depends_on:
      - postgres_fc

  farm_calendar:
    build: .
    image: ghcr.io/openagri-eu/farmcalendar:latest
    command: python manage.py runserver 0.0.0.0:8000
    ports:
      - "8000:8000"
    depends_on:
      - postgres_fc
    environment:
      POSTGRES_HOST: postgres_fc
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}

volumes:
  postgres_data_fc: {}

networks:
  shared_network_fc:
    driver: bridge
    external: true
```

### Accessing pgAdmin

After starting the services, pgAdmin will be accessible through your web browser at:

```commandline
http://localhost:8088
```

Use the email and password specified in the .env file to log in.

# License
This project code is licensed under the EUPL 1.2 license, see the LICENSE file for more details.
Please note that each service may have different licenses, which can be found their specific source code repository.