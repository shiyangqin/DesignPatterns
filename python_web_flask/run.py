# -*- coding: utf-8 -*-
from flask import Flask, current_app

import logging_config
from App import main_app
from config import LOG
from utils.PostgreSQL import PG_Pool

app = Flask(__name__)
app.register_blueprint(main_app,url_prefix='/admin')

pg_link = PG_Pool()
app.app_context().push()
current_app.pool = pg_link.get_pool()

logging_config.config_logging(LOG.log_name, LOG.log_level)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
