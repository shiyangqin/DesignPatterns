# -*- coding: utf-8 -*-
from flask import Flask, current_app

import logging_config
from app import main_app
from config import LOG
from utils.pg_util import PgPool

logging_config.config_logging(LOG.file_name, LOG.level)

app = Flask(__name__)
app.register_blueprint(main_app)

pg_pool = PgPool()
app.app_context().push()
current_app.pool = pg_pool.get_pool()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
