#  NTT pyATS Docker

This is an adapted docker image of the offical pyATS test framework Docker image. The motivation was to create a container with a lower barrier of entry and adaptable for project needs.

## How to use the pyATS Docker image 

### Downloading the PyATS image

Currently the image must be built from source. Will look to host on artifactory to allow for `docker pull` in the future.

Clone the repository:

`git clone https://scm.dimensiondata.com/uki/projects/uefa/ntt-pyats-docker.git`

To build a Docker image from the Dockerfile, run the following command from inside this directory

`$ docker build -t pyats .`

Note: Changing the name of the container will require editing of the `docker-compose.yml`

`docker-compose up -d` - To run as daemon.

To access, either:

`docker exec -it pyats-docker-compose_pyats_1 /bin/bash`

or 

`docker exec -it pyats-docker-compose_pyats_1 <command>` 


## CRON Jobs

You should look to apply any cron jobs from the host itself. An example of this would be: 

`*/30 * * * * docker exec -it pyats-docker-compose_pyats_1 pyats run job tests/example_job.py --testbed-file small-testbed.yml`

The `pyats-cron-example` file will hold common example to apply to your crontab.

## Notes

- Cron is working
- Email & Webex Alerts working
- Pyats logs server restarts every 5 mins. 

## Using the image

On your OS store any pyATs tests in `/pyats` - These will then be found in the container under `/tests`

`docker exec -it pyats-docker-compose_pyats_1 /bin/bash` - Is recommended for dev work. 

`docker exec -it pyats-docker-compose_pyats_1 <command>` - External commands/cron jobs

Make all modifications on the OS side to scripts, conf files etc.


