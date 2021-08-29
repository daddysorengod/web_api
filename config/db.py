from sqlalchemy import create_engine, MetaData

# SQLALCHEMY_DATABASE_URI = "postgresql://user:password@postgresserver/db"
engine = create_engine("mysql+pymysql://root@localhost:3306/dbapi")
meta = MetaData()
conn = engine.connect()