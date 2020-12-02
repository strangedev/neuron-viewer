# Deployment of neuron-buildbot

## Requirements

- docker
- docker-compose
- pipenv

## Configuration

Adjust the yaml files in `config/`.
The options are documented there.

Run `pipenv run python build_config.py` to generate the configuration from yaml.

## Running

You need to login into GitHub using a personal access token before you can pull.

`docker-compose up`

## Upgrading

The general steps are:
- commit your config 
- pull the new verison with `git pull`
- solve conflicts in the `yaml` files
- rebuild the config
- pull the latest images with `docker-compose pull`
- restart with `docker-compose up -d`

### To v1.0.0

This upgrade contains breaking changes to:
- `buildbot_config.yaml`
- `webserver_config.yaml`
- `secrets.yaml`

This upgrade adds the following features:
- Multiple users are now supported by basic auth.

#### `buildbot_config.yaml`

- `repositoryURL` was renamed to `repositoryUrl`
- The `authFlow` `"PATFlow"` was renamed to `"TokenFlow"`

#### `webserver_config.yaml`

The parameters `username` and `password` have been replaced with an array of `users`.

Each array item is now an object containing a `username` and `password`.