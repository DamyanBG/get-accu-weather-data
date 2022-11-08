from flask import Flask
from flask_restful import Api
from flask_apscheduler import APScheduler

from tasks import get_current_data


class Config:
    DEBUG = True
    SCHEDULER_API_ENABLED = True


app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)
scheduler = APScheduler()

# Add cron job to be executed on every 15 minutes

scheduler.add_job(func=get_current_data, trigger="cron", minute="*/15", id="get_current_data")


scheduler.init_app(app)
scheduler.start()

if __name__ == "__main__":
    app.run()
