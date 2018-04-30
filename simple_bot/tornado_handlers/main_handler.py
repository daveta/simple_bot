from tornado.web import RequestHandler, asynchronous
import logging    
from botbuilder.schema import (Activity, ActivityTypes, ChannelAccount)
from botframework.connector import ConnectorClient
from botframework.connector.auth import (MicrosoftAppCredentials,
                                         JwtTokenValidation, SimpleCredentialProvider)
import json
import logging
from tornado_handlers import __APP_ID__, __APP_PASSWORD__
from util.modules import bot_types, load_class
from bot_type_handlers import __type_handlers_map__


class main_handler(RequestHandler):
    def initialize(self):
        RequestHandler.initialize(self)
        self.log = logging.getLogger()
        self.bot_types = [x[0] for x in __type_handlers_map__]
        
    @asynchronous
    def get(self):
        logging.info('GET invoked')
        self.write("Hello, world")
        self.set_status(200, 'All good')
        self.finish()
        
    def __handle_authentication(self, activity):
        credential_provider = SimpleCredentialProvider(__APP_ID__, __APP_PASSWORD__)

        try:
            JwtTokenValidation.assert_valid_activity(
                activity, self.request.headers.get("Authorization"), credential_provider)
            return True
        except Exception as ex:
            return False
        
    @asynchronous
    def post(self):
        logging.info('GET invoked')
        
        # Pull activity
        assert int(self.request.headers['Content-Length']) == len(self.request.body), 'No match on content length!'
        body = self.request.body
        data = json.loads(str(body, 'utf-8'))
        activity = Activity.deserialize(data)
        
        # Verify app_id's
        if not self.__handle_authentication(activity):
            self.set_status(401, 'Authentication failed')
            self.finish()
            return
        
        # Dispatch on type
        
        if activity.type in self.bot_types:
            type_handler_map = [x for x in __type_handlers_map__ if x[0] == activity.type][-1]
            type_handler_class = type_handler_map[1]()
            try:
                type_handler_class.Handle(activity)
                self.set_status(202, 'All Good')
                self.finish()
                return                
            except Exception as ex:
                self.log.error(ex)
            
        else:
            self.set_status(404, 'Unknown command')
            self.finish()
            return                
            
            
            
