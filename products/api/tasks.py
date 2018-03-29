from celery import shared_task

@shared_task
def a(x, y):
	return x + y