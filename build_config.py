#!/usr/bin/env python3

import yaml
import json
import jinja2
import hashlib
import base64

buildbot_config = {}
webserver_config = {}

with open("./config/buildbot_config.yaml", "r") as config_yaml:
    buildbot_config = yaml.safe_load(config_yaml)
    with open("./config.json", "w") as config_json:
        json.dump(buildbot_config, config_json)

with open("./config/secrets.yaml", "r") as secrets_yaml:
    with open("./secrets.json", "w") as secrets_json:
        json.dump(yaml.safe_load(secrets_yaml), secrets_json)

with open("./config/webserver_config.yaml", "r") as config_yaml:
    webserver_config = yaml.safe_load(config_yaml)

with open("./docker-compose.yml", "w") as compose:
    tplLoader = jinja2.FileSystemLoader(searchpath=".")
    tplEnv = jinja2.Environment(loader=tplLoader)
    template = tplEnv.get_template("docker-compose.yml.tpl")
    compose.write(template.render(buildbot=buildbot_config, webserver=webserver_config))

with open("./htpasswd", "w") as htpasswd:
    for user in webserver_config["users"]:
        username = user["username"]
        password_hash = hashlib.sha1(user["password"].encode("ascii")).digest()
        password_b64 = base64.b64encode(password_hash).decode("ascii")
        htpasswd.write(f"{username}:{{SHA}}{password_b64}\n")
