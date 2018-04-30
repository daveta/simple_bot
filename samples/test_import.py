from unittest import TestCase
import logging, sys
from bvt.util.modules import import_module , bot_types, load_class
from bvt.util.modules import load_bot_types
import pkgutil
from bvt.bot_type_handlers.event import EventHandler
from bvt.bot_type_handlers import __type_handlers_map__


def get_logger(level=logging.INFO):
        log = logging.getLogger()
        log.level = level
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s'))
        log.handlers = []
        log.addHandler(handler)
        return log
    
def close_logger(log):
        logging.shutdown()

class ModuleTests(TestCase):
    def setUp(self):
        self.log = get_logger()
    def tearDown(self):
        close_logger(self.log)

    def test_module_load(self):
        self.log.info('Loading library')
        mod = import_module("bvt.bot_type_handlers") 
        self.log.info('Here is module info {0}'.format(mod))
        
    def test_bot_handlers(self):
        self.log.info('Supported types')
        pgk = load_bot_types("bvt.bot_type_handlers")
        self.log.info('Here are the packages: {0}'.format(pgk))
        
    def test_event_handler(self):
        load_bot_types("bvt.bot_type_handlers")
        self.log.info("here are the types:{0}".format(bot_types))
        type_handler_map = [x for x in __type_handlers_map__ if x[0] == 'event'][-1]
        foo = str(type_handler_map[1])
        handler_c = type_handler_map[1]()
        handler_c.Handle('foo')
        
        