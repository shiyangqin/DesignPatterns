# -*- coding: utf-8 -*-
from flask import Flask, current_app

import logging_config
from app.app_test import app as app_test
from config import Log
from utils.PostgreSQL import PG_Pool

app = Flask(__name__)
app.register_blueprint(app_test)


pg_pool = PG_Pool()
app.app_context().push()
current_app.pool = pg_pool.get_pool()


if __name__ == '__main__':
    logging_config.config_logging(Log.log_name, Log.log_level)
    app.run(host='0.0.0.0', port=9002, debug=True)
