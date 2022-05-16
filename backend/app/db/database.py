from sqlalchemy import create_engine

DATABASE_URL='postgresql://postgres:postgres@127.0.0.1:5432/rwdb'

engine = create_engine(
    DATABASE_URL, connect_args={}
)
# metadata = sqlalchemy.MetaData()
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
database = "DATABASE_URL"
