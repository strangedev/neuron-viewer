version: '3'
services:
    app:
        image: docker.pkg.github.com/strangedev/neuron-buildbot/neuron-buildbot:latest
        ports: 
            - {{ buildbot.port }}:{{ buildbot.port }}
        volumes: 
            - neuron:{{ buildbot.localRepositoryPath }}/.neuron/output
            - ./config.json:/etc/neuron_buildbot/config.json
        {% if not buildbot.useDockerSecrets %}
            - ./secrets.json:/root/.neuron_buildbot/secrets.json
        {% else %}
        secrets:
            - neuron_buildbot
        {% endif %}
    nginx:
        image: nginx
        ports:
            - {{ webserver.port }}:80
        volumes:
            - neuron:/neuron:ro
            - ./nginx.conf:/etc/nginx/nginx.conf
            - ./htpasswd:/htpasswd

{% if buildbot.useDockerSecrets %}
secrets:
    neuron_buildbot:
        file: ./secrets.dev.json
{% endif %}

volumes:
    neuron:
        driver: local
