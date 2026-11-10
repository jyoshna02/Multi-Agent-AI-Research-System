import sqlite3
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE_DIR = os.path.join(BASE_DIR, "database")

os.makedirs(DATABASE_DIR, exist_ok=True)

DATABASE_NAME = os.path.join(
    DATABASE_DIR,
    "research_history.db"
)
def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn
def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS research_reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT NOT NULL,
            research_date TEXT NOT NULL,
            final_report TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
def save_research(topic, final_report):
    conn = get_connection()
    cursor = conn.cursor()

    research_date = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cursor.execute("""
        INSERT INTO research_reports
        (topic, research_date, final_report)
        VALUES (?, ?, ?)
    """, (topic, research_date, final_report))

    conn.commit()
    conn.close()

    print("Research saved successfully!")
    
def get_all_reports():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, topic, research_date
        FROM research_reports
        ORDER BY id DESC
    """)

    reports = cursor.fetchall()

    conn.close()

    return reports
def get_report_by_id(report_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, topic, research_date, final_report
        FROM research_reports
        WHERE id = ?
    """, (report_id,))

    report = cursor.fetchone()

    conn.close()

    return report
if __name__ == "__main__":

    create_table()

    print("Database created successfully!")

    reports = get_all_reports()

    print("Saved Research History:", reports)
       