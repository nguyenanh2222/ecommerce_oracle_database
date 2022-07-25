from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

host = "localhost"
port = "1521"
database = "xe"
username = "ECOMMERCE"
password = "123"


engine = create_engine(f"oracle+cx_oracle://{username}:{password}@{host}:{port}/{database}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = sessionmaker(bind=engine, future=True)

rs = engine.execute("""
SELECT table_name
FROM all_tables
ORDER BY table_name ASC""").all()
print(rs)