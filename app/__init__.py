from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

DATABASE_URL = "postgresql://your_user:your_password@localhost/your_database_name"

engine = create_engine(DATABASE_URL)

if not database_exists(engine.url):
    create_database(engine.url)
    print(f"Database {engine.url.database} created.")

# Set owner (assuming you have the necessary permissions)
with engine.connect() as conn:
    conn.execute("ALTER DATABASE your_database_name OWNER TO your_user")

print("Database initialized and owner set.")
