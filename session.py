from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

metadata = MetaData()
engine = create_engine(
    'mysql+pymysql://root:root@localhost:3306/DVD_store'
)

Session = sessionmaker(bind=engine)
session = Session()