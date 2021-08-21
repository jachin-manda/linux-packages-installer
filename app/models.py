from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Text
from app import Base


@dataclass
class PackagesAndCommands(Base):
    __tablename__ = "packages_and_commands"

    id = Column("id", Integer, primary_key=True)
    package_name = Column("package_name", String(50), unique=True, nullable=False)
    package_desc = Column("package_desc", Text, nullable=True)
    command_debian = Column("command_debian", Text, nullable=False)
    command_fedora = Column("command_fedora", Text, nullable=False)

    def __repr__(self):
        return self.package_name


def create_table(engine):
    Base.metadata.create_all(bind=engine)
