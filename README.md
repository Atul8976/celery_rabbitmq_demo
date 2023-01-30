# celery_rabbitmq_demo
django project which demonstrate use of celery with rabbitmq

start celery worker with rabbitmq

celery -A projectname worker -l info -P gevent

delete pending stask from rabbitmq
celery -A projectname purge