# TODO replace port number with the same one from the Dockerfile
exec gunicorn -b :5000 --access-logfile - --error-logfile - app:app