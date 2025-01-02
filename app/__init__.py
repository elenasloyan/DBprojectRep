from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

# Update this with your actual credentials
DATABASE_URL = "postgresql://ellasloyan:asloyanelasloyan@localhost/dbproject"

engine = create_engine(DATABASE_URL)

# Check if the database exists; if not, create it
if not database_exists(engine.url):
    create_database(engine.url)
    print(f"Database {engine.url.database} created.")

# Set the owner of the database (assuming you have the necessary permissions)
with engine.connect() as conn:
    conn.execute("ALTER DATABASE dbproject OWNER TO ellasloyan")

print("Database initialized and owner set.")
