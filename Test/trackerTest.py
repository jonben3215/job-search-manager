import pytest
import trackerClass
from trackerClass import job_tracker

@pytest.fixture
def tracker():
    t = job_tracker(":memory:", ":memory:")
    
    t.app_cursor.execute("""
            CREATE TABLE IF NOT EXISTS JOB_APP (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                COMPANY_NAME TEXT NOT NULL,
                JOB_TITLE TEXT NOT NULL,
                DATE_APPLIED TEXT NOT NULL,
                JOB_URL TEXT,
                STATUS NOT NULL,
                INTERVIEW_DATE TEXT NOT NULL,
                NEXT_ACTION TEXT)                   
    """)
    
    t.auth_cursor.execute("""
            CREATE TABLE IF NOT EXIST CREDENTIALS (
                ID INTEFER PRIMARY KEY AUTOINCREMENT,
                COMPANY_NAME, TEXT NOT NULL,
                USERNAME TEXT,
                PASSWORD_MANAGEMENT TEXT,
                JOB_URL TEXT)
    """)
    t.app_conn.commit
    t.auth_conn.commit
    
    yield t
    
    t.auth_conn.commit
    t.app_conn.commit
    