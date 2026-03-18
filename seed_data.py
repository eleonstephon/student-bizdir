"""
Seed Data Script for Student Business Directory
Run this script to populate the database with sample businesses
"""

import sqlite3
import os

# Database path
DB_PATH = 'businesses.db'

# Sample business data
businesses = [
    # Business Name, Category, Description, Contact, Image
    ("Cecilia's Glow Skincare", "Beauty & Skincare", 
     "Natural handmade skincare products - organic shea butter, facial scrubs, and body oils made by a level 300 student.",
     "0241234567", "glow_skincare.jpg"),
     
    ("Campus Chili Kitchen", "Food & Drinks", 
     "Spicy homemade chili with jollof rice, available daily at the science cafeteria. Special orders available for events.",
     "0547890123", "chili_kitchen.jpg"),
     
    ("TechFix Solutions", "Tech & Services", 
     "Phone screen repairs, laptop troubleshooting, and software installation. Free diagnostics for students.",
     "0204567890", "techfix.jpg"),
     
    ("Afro Threads", "Fashion & Clothing", 
     "Custom African print clothing, alterations, and accessories. We make bespoke outfits for any occasion.",
     "0551234567", "afro_threads.jpg"),
     
    ("BrightLights Decor", "Lights & Decor", 
     "LED fairy lights, room decoration packages, and custom neon signs for your hall room or events.",
     "0249876543", "brightlights.jpg"),
     
    ("Notes & More", "Services", 
     "Printed lecture notes, project binding, laminating, and stationery supplies. Located near the main library.",
     "0501122334", "notes_more.jpg"),
     
    ("Fit Eats", "Food & Drinks", 
     "Healthy meal preps - grilled chicken, mixed vegetables, and fresh smoothies delivered to your hostel.",
     "0278899001", "fit_eats.jpg"),
     
    ("SnapShot Studio", "Services", 
     "Campus photography for events, portraits, and graduation photos. Affordable student packages.",
     "0245566778", "snapshot.jpg"),
     
    ("HairCraft", "Beauty & Skincare", 
     "Natural hair braiding, styling, and wig making. Book your appointment online or visit our salon.",
     "0209988776", "haircraft.jpg"),
     
    ("JS Tutorial Hub", "Services", 
     "Coding lessons for beginners - Python, JavaScript, and web development. One-on-one tutoring available.",
     "0591122334", "tutorial_hub.jpg")
]

def create_database():
    """Create the database and businesses table"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS businesses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            contact TEXT,
            image TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ Database table created successfully")

def seed_data():
    """Insert sample businesses into the database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Clear existing data (optional - removes duplicates)
    cursor.execute("DELETE FROM businesses")
    
    # Insert all businesses
    for business in businesses:
        cursor.execute('''
            INSERT INTO businesses (name, category, description, contact, image)
            VALUES (?, ?, ?, ?, ?)
        ''', business)
    
    conn.commit()
    count = cursor.rowcount
    conn.close()
    
    print(f"✅ Successfully inserted {count} businesses into the database")

def verify_data():
    """Verify the data was inserted correctly"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM businesses")
    count = cursor.fetchone()[0]
    
    print(f"\n📊 Database Summary:")
    print(f"   Total businesses: {count}")
    
    if count > 0:
        cursor.execute("SELECT name, category FROM businesses LIMIT 5")
        print("   Sample businesses:")
        for row in cursor.fetchall():
            print(f"   - {row[0]} ({row[1]})")
    
    conn.close()

if __name__ == "__main__":
    print("🌱 Seeding Student Business Directory Database...\n")
    
    # Remove existing database if you want a fresh start
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print("🗑️  Removed existing database")
    
    # Create and seed
    create_database()
    seed_data()
    verify_data()
    
    print("\n✨ Done! Your app is now ready with sample data.")