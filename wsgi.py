import redischat as main

app = main.configured_app()

# gunicorn -b '0.0.0.0:3000' wsgi:app
# nohup gunicorn -b '0.0.0.0:3000' wsgi:app &
