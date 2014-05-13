#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging


class pyLogger:
    """ A basic python logger using logging

    Logs to the file passed as argument

    Formats each log entry whith the date, the module name, and the level
    """

    def __init__(self, logname, level='INFO'):
        """ Gets the filename and the level """

        loglevel = logging.NOTSET

        if level == 'CRITICAL':
            loglevel = logging.CRITICAL
        elif level == 'ERROR':
            loglevel = logging.ERROR
        elif level == 'WARNING':
            loglevel = logging.WARNING
        elif level == 'INFO':
            loglevel == logging.INFO
        elif level == 'DEBUG':
            loglevel = logging.DEBUG

        # Argumentos del logger. Por defecto el nivel debería ser INFO
        self.log = logging.Logger(logname)
        self.log.setLevel(loglevel)

        handler = logging.FileHandler(logname)
        handler.setLevel(loglevel)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s \
                                                                - %(message)s')
        handler.setFormatter(formatter)

        self.log.addHandler(handler)
