# -*- coding: utf-8 -*-
from flask import Flask, current_app

import loggingConfig
from App import mainApp
from config import LOG
from utils.PostgreSQL import PgPool

loggingConfig.configLogging(LOG.log_name, LOG.log_level)

app = Flask(__name__)
app.register_blueprint(mainApp)

pgPool = PgPool()
app.app_context().push()
current_app.pool = pgPool.getPool()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
