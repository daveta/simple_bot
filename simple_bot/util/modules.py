import importlib
import pkgutil
import logging

bot_types = []
def load_bot_types(package_name):
    try:
        log = logging.getLogger()
        log.debug('Loading package: %s', package_name)            
        pkg = import_module(package_name)
        # walk_packages ==> (module_loader, name, ispkg)
        for m in [p[1] for p in pkgutil.walk_packages(pkg.__path__, pkg.__name__ + '.') if not p[2]]:
            try:
                log.info('import module: %s', m)
                type_name = m.split('.')[-1]
                if not type_name in bot_types: 
                    bot_types.append(type_name)
                import_module(m)
            except ImportError as ie:
                log.error('Failed to import module %m due to %s:', m, str(ie))
            except:
                pass
        return pkg
    except ImportError:
        return None
        
def import_module(module_name):
    try:
        return importlib.import_module(module_name)
    except ImportError as ie:
        logging.getLogger().error('Failed to import module %s due to "%s":', module_name, str(ie))

        
def load_class(qualified_name):
    try:
        path, name = qualified_name.rsplit('.', 1)
    except ValueError:
        return None
    
    mod = import_module(path)
    
    if mod:
        try:
            return getattr(mod, name)
        except AttributeError:
            return None
            
    return None