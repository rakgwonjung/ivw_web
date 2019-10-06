daemon=True
bind='unix:/ivw/web/bo/run/gunicorn.sock bo.wsgi:application'
workers=5
