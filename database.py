from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# db_url_format = dialect+driver://dbuser;dbpasswd;dbhost;dbport;dbname
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")
db_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
print(f"db_url : {db_url}")

engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
db = Session()

create_table_query = text('''
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
    ); ''')

create_courses_query = text('''
    CREATE TABLE IF NOT EXISTS courses  (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    level VARCHAR(255) NOT NULL
    ); ''')

create_enrollment_query = text('''
    CREATE TABLE IF NOT EXISTS enrollments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    userId INT NOT NULL,
    courseId INT NOT NULL,
    FOREIGN KEY (userId) REFERENCES users (id),
    FOREIGN KEY (courseId) REFERENCES courses (id)
    ); ''')

try:
    db.execute(create_table_query)
    db.execute(create_courses_query)
    db.execute(create_enrollment_query)

    db.commit()
    print("All Tables created successfully")
except Exception as e:
    db.rollback()
    print(f"Something went wrong: {e}")

finally:
    db.close()
