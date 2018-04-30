import os, signal, tornado, logging
from logging.handlers import RotatingFileHandler
from tornado_handlers.main_handler import main_handler


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

def signal_handler(sig_num, frame):
    tornado.ioloop.IOLoop.instance().stop()
    

def build_config():
    app_config = []
    
    # Add all handlers
    app_config.append(('/', main_handler))
            
    # return the app_config
    return app_config    

def run():
    logging.info('Preparing signal handlers')
    # register signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    
    logging.info('Building config')
    app_config = build_config()
    api_port = 8080
    
    
    application = tornado.web.Application(app_config)
    logging.info('Listening on port {0}..'.format(api_port))
    application.listen(api_port)

    try:  
        # start the app and wait for a close
        tornado.ioloop.IOLoop.instance().start()
        return
    except:
        # handle error with shutting down loop
        tornado.ioloop.IOLoop.instance().stop()

if __name__ == '__main__':
    try:
        setup_logging()
        run()
    except Exception as e:
        logging.error(e)

        
        
