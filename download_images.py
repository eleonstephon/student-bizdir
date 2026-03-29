"""
download_images.py - Download placeholder images for all businesses
"""

import os
import requests
import time

# Create uploads folder if it doesn't exist
os.makedirs('static/uploads', exist_ok=True)

# List of all image filenames needed (56 images - Eco Clean has no image)
image_filenames = [
    # Beauty & Skincare (10)
    'glow_skincare.jpg', 'haircraft.jpg', 'nail_haven.jpg', 'fresh_face.jpg', 
    'barber_spot.jpg', 'lash_studio.jpg', 'organic_roots.jpg', 'makeup_efia.jpg', 
    'scent_soul.jpg', 'glow_clinic.jpg',
    
    # Food & Drinks (10)
    'chili_kitchen.jpg', 'fit_eats.jpg', 'sweet_tooth.jpg', 'java_junction.jpg', 
    'tasty_bites.jpg', 'smoothie_bar.jpg', 'pizza_palace.jpg', 'nanas_kitchen.jpg', 
    'coffee_code.jpg', 'frozen_delights.jpg',
    
    # Tech & Services (9)
    'techfix.jpg', 'tutorial_hub.jpg', 'pc_doctors.jpg', 'print_go.jpg', 
    'web_wizards.jpg', 'data_recovery.jpg', 'social_media.jpg', 'phone_unlock.jpg', 
    'it_tutoring.jpg',
    
    # Fashion & Clothing (9)
    'afro_threads.jpg', 'campus_couture.jpg', 'shoe_haven.jpg', 'beads_bling.jpg', 
    'threads_style.jpg', 'vintage_vibes.jpg', 'tailor_shop.jpg', 'accessory_corner.jpg', 
    'campus_uniforms.jpg',
    
    # Lights & Decor (9)
    'brightlights.jpg', 'room_revamp.jpg', 'party_perfect.jpg', 'poster_world.jpg', 
    'led_studio.jpg', 'cozy_corners.jpg', 'wall_art.jpg', 'festive_lights.jpg', 
    'home_essentials.jpg',
    
    # Services (9 - excluding Eco Clean which has no image)
    'notes_more.jpg', 'snapshot.jpg', 'event_planners.jpg', 'tutoring.jpg', 
    'laundry.jpg', 'cv_pro.jpg', 'moving_helpers.jpg', 'tech_support.jpg', 
    'study_hub.jpg'
]

# Free image APIs that don't require authentication
# Using Lorem Picsum (always returns nice placeholder images)
def download_image(filename, width=400, height=300):
    """Download a random image from Lorem Picsum"""
    try:
        # Use Lorem Picsum with a random seed based on filename
        seed = abs(hash(filename)) % 1000
        url = f'https://picsum.photos/id/{seed}/{width}/{height}'
        
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            filepath = os.path.join('static/uploads', filename)
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print(f'✅ Downloaded: {filename}')
            return True
        else:
            # Fallback to random image
            url = f'https://picsum.photos/{width}/{height}?random={seed}'
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                filepath = os.path.join('static/uploads', filename)
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f'✅ Downloaded: {filename}')
                return True
    except Exception as e:
        print(f'❌ Error downloading {filename}: {e}')
    return False

print('📸 Downloading images for Student Business Directory...')
print(f'Total images needed: {len(image_filenames)}\n')

success_count = 0
for i, filename in enumerate(image_filenames, 1):
    print(f'[{i}/{len(image_filenames)}] ', end='')
    if download_image(filename):
        success_count += 1
    time.sleep(0.5)  # Small delay to avoid overwhelming the server

print(f'\n✨ Done! Downloaded {success_count}/{len(image_filenames)} images to static/uploads/')
print('Run the app to see the images on your business cards!')