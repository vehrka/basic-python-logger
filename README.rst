Basic Python logger
===================

This is a basic Python logger.

It uses the logging facility from the standard Python Library to make an
file logger with a predefined configuration::

    2014-03-21 09:32:39,941 - basiclogger - DEBUG - Adding the point:: POINT -0.936 42.386
    2014-03-21 09:32:40,530 - basiclogger - DEBUG - Adding the point:: POINT -0.776 42.089

Usage::

    # Import the logger
    from basiclogger import pyLogger

    # Init the logger
    logger = pyLogger('test.log', 'DEBUG')

    # Use the force Luke
    logger.log.critical('This is a critical test')
    logger.log.error('This is an error test')
    logger.log.warning('This is a warning test')
    logger.log.info('This is an info test')
    logger.log.debug('This is a debug test')

The default logging level is *INFO* thus::

    logger = pyLogger('test.log')

and::

    logger = pyLogger('test.log', 'INFO')

are equivalents
