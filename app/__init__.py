from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

SUPERUSER_DATABASE_URL = "postgresql://postgres:superuser_password@localhost/postgres"
USER_DATABASE_URL = "postgresql://ellasloyan:asloyanelasloyan@localhost/dbproject"

superuser_engine = create_engine(SUPERUSER_DATABASE_URL)

if not database_exists(superuser_engine.url):
    create_database(superuser_engine.url)
    print(f"Database {superuser_engine.url.database} created.")


with superuser_engine.connect() as conn:
    conn.execute("ALTER DATABASE dbproject OWNER TO ellasloyan")
    print("Database owner set to ellasloyan.")

# Create engine using regular user credentials
user_engine = create_engine(USER_DATABASE_URL)

print("Database initialized and owner set.")

