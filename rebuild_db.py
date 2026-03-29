import sqlite3
import os

# Delete old database
if os.path.exists('businesses.db'):
    os.remove('businesses.db')
    print('Deleted old database')

# Create new database with correct schema
conn = sqlite3.connect('businesses.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE businesses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    business_name TEXT NOT NULL,
    owner_name TEXT NOT NULL,
    category TEXT NOT NULL,
    description TEXT NOT NULL,
    whatsapp TEXT,
    phone TEXT,
    location TEXT,
    delivers INTEGER DEFAULT 0,
    photo_filename TEXT,
    is_verified INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

print('✅ Database recreated with correct schema')
conn.close()
