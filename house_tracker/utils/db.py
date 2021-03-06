
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = None
# a session factory, name it as class name style
Session = None

def get_database_url():
    import house_tracker_settings as settings
    
    config = settings.database
    return  ('%s://%s:%s@%s/%s?charset=utf8' % 
             (config['driver'], config['user'], config['password'],
              config['host'], config['name'])
             )

def init_db(**kwargs):
    global engine, Session
    if not engine:
        engine = create_engine(get_database_url(), encoding='utf-8', **kwargs)
    if not Session:
        Session = sessionmaker(bind=engine)
    
def get_engine():
    if not engine:
        init_db()
    return engine

def get_session(**kwargs):
    if not Session:
        init_db(**kwargs)
    return Session()

