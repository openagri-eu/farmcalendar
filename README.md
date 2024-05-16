# Farm Calendar Application Setup

This README provides detailed instructions on setting up the PostgreSQL database and pgAdmin for the Farm Calendar 
application using Docker.

## Prerequisites

Before you start, make sure Docker and Docker Compose are installed on your system. You will also need to create a 
Docker network named `shared_network_fc` if it's marked as external in the Docker Compose configuration.

## Services Setup

This setup includes two main services:

1. **PostgreSQL** - The database server.
2. **pgAdmin 4** - A web-based administration tool for PostgreSQL.

## Configuration

### 1. Docker Compose

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

volumes:
  postgres_data_fc: {}

networks:
  shared_network_fc:
    driver: bridge
    external: true
```

### 2. Environment File

Create a .env file in the same directory as your docker-compose.yml with the following environment variables:

```
POSTGRES_DB=farm_calendar
POSTGRES_USER=farm_calendar_admin
POSTGRES_PASSWORD=<YourPasswordHere>

PGADMIN_DEFAULT_EMAIL=<YourEmailHere>
PGADMIN_DEFAULT_PASSWORD=<YourPasswordHere>
```
Replace <YourPasswordHere> and <YourEmailHere> with your actual credentials.


### 3. Network Setup

If the network shared_network_fc does not exist, you must create it manually using the following Docker command:

```commandline
docker network create shared_network_fc
```

This network allows your Docker containers to communicate internally while isolating them from external access.


# Running the Services

To start the services, navigate to the directory containing your docker-compose.yml and run:

```commandline
docker-compose up -d
```

This command starts the containers in detached mode.


# Accessing pgAdmin

After starting the services, pgAdmin will be accessible through your web browser at:

```commandline
http://localhost:8088
```

Use the email and password specified in the .env file to log in.


# Stopping the Services

To stop and remove the containers, use:

```commandline
docker-compose down
```

# Volume Management

The data for PostgreSQL is persisted in a Docker volume (postgres_data_fc). This ensures that your database data remains intact even after the container is stopped or removed.


# Additional Information

For additional configuration options or more detailed information on using PostgreSQL and pgAdmin with Docker, refer to the official documentation for PostgreSQL and pgAdmin.
