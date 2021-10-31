from main import app
from celery_main import celery_app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=app.config.get('PORT'), debug=True, threaded=True)
    celery_app.add_periodic_task(10.0, celery_app.fetch_news.s(), name='Initial test')
