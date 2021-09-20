import sqlite3

db_path = '/Users/mehulchopra/Documents/training/kh/icon-media-dataanalytics/library_db.db'

def connection():
  return sqlite3.connect(db_path)