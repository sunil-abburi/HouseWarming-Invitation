#!/usr/bin/env python3
"""
Abburi's Housewarming Invitation Sender
Simple WhatsApp invitation script
"""

import csv
import time
import webbrowser
from urllib.parse import quote

def load_guests(csv_file):
    """Load guests from CSV file"""
    guests = []
    try:
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                guests.append({
                    'name': row['Name'],
                    'phone': row['Phone'],
                    'email': row.get('Email', ''),
                    'url': row['Invitation URL']
                })
    except FileNotFoundError:
        print(f"Error: {csv_file} not found")
        return []
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []
    
    return guests

def send_whatsapp_message(phone, message):
    """Send WhatsApp message"""
    try:
        # Remove any non-digit characters except + at start
        clean_phone = ''.join(c for c in phone if c.isdigit() or c == '+')
        
        # Create WhatsApp URL
        whatsapp_url = f"https://wa.me/{clean_phone}?text={quote(message)}"
        
        # Open in browser
        webbrowser.open(whatsapp_url)
        
        print(f"Opened WhatsApp for {phone}")
        return True
        
    except Exception as e:
        print(f"Error sending to {phone}: {e}")
        return False

def create_invitation_message(name, url):
    """Create personalized invitation message"""
    message = f"""
Namaste!

Dear *{name}*,

You are warmly invited to
*Abburi's Housewarming Celebration*

• Muhurtham: 5th November 2026 (Thursday Night at 8:00 PM)
• Satyanarayana Vratham & Feast: 6th November 2026 (Friday)
• Venue: Kunduruvaripalem, Andhra Pradesh

✨ View your personal digital invitation here:
{url}

With Best Compliments & Love,
Abburi Family
"""
    return message.strip()

def main():
    """Main function"""
    csv_file = "housewarming_guests.csv"
    
    print("=== Abburi's Housewarming Invitation Sender ===")
    print()
    
    # Load guests
    guests = load_guests(csv_file)
    if not guests:
        print("No guests found. Please create housewarming_guests.csv first.")
        return
    
    print(f"Found {len(guests)} guests")
    print()
    
    # Send invitations
    for i, guest in enumerate(guests, 1):
        print(f"Sending invitation {i}/{len(guests)} to {guest['name']}...")
        
        # Create message
        message = create_invitation_message(guest['name'], guest['url'])
        
        # Send WhatsApp message
        success = send_whatsapp_message(guest['phone'], message)
        
        if success:
            print(f"  Sent to {guest['name']}")
        else:
            print(f"  Failed to send to {guest['name']}")
        
        # Wait between messages to avoid spam detection
        if i < len(guests):
            print("  Waiting 10 seconds before next message...")
            time.sleep(10)
    
    print()
    print("=== All invitations processed! ===")
    print(f"Total guests: {len(guests)}")
    print("Check your browser windows for each WhatsApp message.")

if __name__ == "__main__":
    main()
