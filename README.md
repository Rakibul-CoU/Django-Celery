Celery unlocks a worker process for Django. This means you can offload tasks from the main request/response cycle within Django. Using Celery becomes critical when your app starts to scale or you need better performance out of Django.

Django is a batteries included web framework written in Python. Django is how you'll create a web application so users can leverage your software.

Redis is the datastore and message broker between Celery and Django. In other words, Django and Celery use Redis to communicate with each other (instead of a SQL database). Redis can also be used as a cache as well. An alternative for Django & Celery is RabbitMQ (not covered here).

All three work together to make some asynchronous magic. Here's a few great use cases for Django + Celery:

  Offloading any long-running tasks
  Sending emails and/or email notifications
  Generating reports that take 3+ seconds to create
  Running Machine Learning training and/or inference
  Run specific functions on a schedule
  Backup a database
  Powering up / powering down additional virtual machines for handling load
  Triggering workflows and/or sending webhook notifications
