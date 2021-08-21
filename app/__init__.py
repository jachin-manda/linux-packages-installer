from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from rich.console import Console
from rich.table import Table
from rich.panel import Panel


engine = create_engine("sqlite+pysqlite:///./db.sqlite3", future=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
console = Console()


from app.models import create_table

create_table(engine)
