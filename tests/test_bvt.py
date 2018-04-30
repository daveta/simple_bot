
import logging
import logging
from logging.handlers import RotatingFileHandler
from unittest import TestCase

from bvt.service_host import build_config
from bvt.handlers.main_handler import main_handler
import tornado.web, tornado.ioloop, time, os, sys

log = None

def setup_logging():
    logging.info('Setting up logging infrastructure')
    
    # create the rotating log handler
    handler = RotatingFileHandler(os.path.join('.', 'bvt-test.log'),
                                  maxBytes=5*1024, # 5 MB chunks,
                                  backupCount=5 # limit to 25 MB logs max
                                  )
    
    # set the formatter
    handler.setFormatter(logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s'))
    
    # setup the root logging with the necessary handlers
    log = logging.getLogger()
    log.addHandler(handler)
    
    # set to info for normal processing
    log.setLevel(logging.INFO)  




class BvtTestHarness(TestCase):

    @classmethod
    def tearDownClass(cls):
        super(BvtTestHarness, cls).tearDownClass()
        logging.shutdown()


    def test_service(self):


        log.info('Starting app')
        application = tornado.web.Application(build_config())

        # run on a local API
        try:
            tornado.ioloop.IOLoop.instance().start()
        except Exception as e:
            log.error(e)


    def stop_io(self):
        # sleep and stop
        tornado.ioloop.IOLoop.instance().stop()
