"""
seed_data.py — Student BizDir
Run this script to populate the database with sample business listings.
This creates a fresh start if the table is empty.
"""

import sqlite3
import os

# Path to the actual database file used by the app
DATABASE_PATH = "bizdir.db"

# Sample business data with all required fields
# Each tuple: (business_name, owner_name, category, description, whatsapp, phone, location, delivers, photo_filename, is_verified)
sample_businesses = [
    # Verified businesses (is_verified = 1)
    ("Cecilia's Glow Skincare", "Cecilia Mensah", "Beauty & Skincare",
     "Natural handmade skincare products – organic shea butter, facial scrubs, and body oils made by a level 300 student.",
     "0241234567", "0556789012", "Women's Common Room, Central Hall", 1, "glow_skincare.jpg", 1),
    
    ("Campus Chili Kitchen", "Kwame Asare", "Food & Drinks",
     "Spicy homemade chili with jollof rice, available daily at the science cafeteria. Special orders available for events.",
     "0547890123", "0204567890", "Science Cafeteria, near Block B", 1, "chili_kitchen.jpg", 1),
    
    ("TechFix Solutions", "Michael Osei", "Tech & Services",
     "Phone screen repairs, laptop troubleshooting, and software installation. Free diagnostics for students.",
     "0204567890", "0249876543", "ICT Centre, Room 12", 0, "techfix.jpg", 1),
    
    ("Afro Threads", "Adwoa Serwaa", "Fashion & Clothing",
     "Custom African print clothing, alterations, and accessories. We make bespoke outfits for any occasion.",
     "0551234567", "0549876543", "Textiles Workshop, Arts Block", 0, "afro_threads.jpg", 1),
    
    ("BrightLights Decor", "Samuel Adjei", "Lights & Decor",
     "LED fairy lights, room decoration packages, and custom neon signs for your hall room or events.",
     "0249876543", "0598765432", "Hall 3, Room 45", 1, "brightlights.jpg", 1),
    
    ("Notes & More", "Akosua Boateng", "Services",
     "Printed lecture notes, project binding, laminating, and stationery supplies. Located near the main library.",
     "0501122334", "0209988776", "Main Library, Ground Floor", 0, "notes_more.jpg", 1),
    
    ("Fit Eats", "Esi Amankwah", "Food & Drinks",
     "Healthy meal preps – grilled chicken, mixed vegetables, and fresh smoothies delivered to your hostel.",
     "0278899001", "0551122334", "Delivery only (campus-wide)", 1, "fit_eats.jpg", 1),
    
    ("SnapShot Studio", "Kofi Annan", "Services",
     "Campus photography for events, portraits, and graduation photos. Affordable student packages.",
     "0245566778", "0501234567", "Creative Arts Centre", 0, "snapshot.jpg", 1),
    
    ("HairCraft", "Abena Serwaa", "Beauty & Skincare",
     "Natural hair braiding, styling, and wig making. Book your appointment online or visit our salon.",
     "0209988776", "0241122334", "Hall 2, Common Room", 0, "haircraft.jpg", 1),
    
    ("JS Tutorial Hub", "Yaw Asare", "Services",
     "Coding lessons for beginners – Python, JavaScript, and web development. One-on-one tutoring available.",
     "0591122334", "0201234567", "Library Study Room 3", 0, "tutorial_hub.jpg", 1),
    
    # Pending business (is_verified = 0) – to demonstrate admin approval
    ("Eco Clean", "Nana Yaw", "Services",
     "Eco-friendly cleaning services for hostels and rooms. We use biodegradable products.",
     "0240001111", "0502223333", "Hall 5, Room 10", 1, "", 0),
]

def seed_database():
    """Populate the database with sample data if the businesses table is empty."""
    # Check if the database file exists
    if not os.path.exists(DATABASE_PATH):
        print(f"Database file '{DATABASE_PATH}' not found. Please run the app first to create it.")
        return
    
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # Check if there are already any rows in the businesses table
    cursor.execute("SELECT COUNT(*) FROM businesses")
    count = cursor.fetchone()[0]
    
    if count > 0:
        print(f"Database already has {count} businesses. Skipping seed to avoid duplicates.")
        conn.close()
        return
    
    # Insert sample data
    insert_sql = """
        INSERT INTO businesses
        (business_name, owner_name, category, description, whatsapp, phone, location, delivers, photo_filename, is_verified)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    
    for biz in sample_businesses:
        cursor.execute(insert_sql, biz)
    
    conn.commit()
    inserted = len(sample_businesses)
    conn.close()
    
    print(f"✅ Seeded {inserted} businesses into {DATABASE_PATH}.")

def verify_data():
    """Print a quick summary of the seeded data."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM businesses")
    total = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM businesses WHERE is_verified = 1")
    verified = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM businesses WHERE is_verified = 0")
    pending = cursor.fetchone()[0]
    
    print(f"\n📊 Database Summary:")
    print(f"   Total businesses: {total}")
    print(f"   Verified (live): {verified}")
    print(f"   Pending approval: {pending}")
    
    if total > 0:
        print("\n   Sample businesses (first 5):")
        cursor.execute("SELECT business_name, category FROM businesses LIMIT 5")
        for row in cursor.fetchall():
            print(f"   - {row[0]} ({row[1]})")
    
    conn.close()

if __name__ == "__main__":
    print("🌱 Seeding Student Business Directory Database...\n")
    seed_database()
    verify_data()
    print("\n✨ Done. Run the app to see the seeded businesses.")