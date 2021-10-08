import databases
import sqlalchemy
from .config import settings

metadata = sqlalchemy.MetaData()
database = databases.Database(settings.POSTGRESQL_URI)
engine = sqlalchemy.create_engine(settings.POSTGRESQL_URI)
