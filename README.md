# Deployment of neuron-buildbot

## Requirements

- docker
- docker-compose
- pipenv

## Configuration

Adjust `config.yaml` and `secrets.yaml`.
The options are documented there.

Run `pipenv run build_config.py` to generate the configuration from yaml.

## Running

You need to login into GitHub using a personal access token before you can pull.

`docker-compose up`
