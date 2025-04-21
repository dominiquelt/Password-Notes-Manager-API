import sqlalchemy as sa
from database import Base, engine



#notes model
class Notes(Base):
    __tablename__ = 'notes'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    content = sa.Column(sa.String, nullable=False)

#making tables in the db
Base.metadata.create_all(bind=engine)
