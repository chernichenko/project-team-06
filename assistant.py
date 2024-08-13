import os
import setup_path
from datetime import datetime, timedelta
from contact import Contact
from note import Note
from utils import validate_phone, validate_email

class PersonalAssistant:
    def __init__(self):
        self.contacts = []
        self.notes = []
        self.load_data()

    def save_data(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        contacts_path = os.path.join(current_dir, 'contacts.txt')
        notes_path = os.path.join(current_dir, 'notes.txt')

        with open(contacts_path, 'w') as f:
            for contact in self.contacts:
                f.write(contact.to_str() + '\n')

        with open(notes_path, 'w') as f:
            for note in self.notes:
                f.write(note.to_str() + '\n')

    def load_data(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        contacts_path = os.path.join(current_dir, 'contacts.txt')
        notes_path = os.path.join(current_dir, 'notes.txt')

        if os.path.exists(contacts_path):
            with open(contacts_path, 'r') as f:
                lines = f.readlines()
                self.contacts = [Contact.from_str(line.strip()) for line in lines if line.strip()]

        if os.path.exists(notes_path):
            with open(notes_path, 'r') as f:
                lines = f.readlines()
                self.notes = [Note.from_str(line.strip()) for line in lines if line.strip()]

    def add_contact(self, name, address, phone, email, birthday):
        if not validate_phone(phone):
            print("Invalid phone number.")
            return
        if not validate_email(email):
            print("Invalid email address.")
            return
        contact = Contact(name, address, phone, email, birthday)
        self.contacts.append(contact)
        self.save_data()
        print("Contact added successfully.")

    def search_contacts(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower()]
        for contact in results:
            print(contact.to_str())

    def edit_contact(self, index, name=None, address=None, phone=None, email=None, birthday=None):
        if index < 0 or index >= len(self.contacts):
            print("Contact not found.")
            return
        contact = self.contacts[index]
        if phone and not validate_phone(phone):
            print("Invalid phone number.")
            return
        if email and not validate_email(email):
            print("Invalid email address.")
            return
        if name:
            contact.name = name
        if address:
            contact.address = address
        if phone:
            contact.phone = phone
        if email:
            contact.email = email
        if birthday:
            contact.birthday = datetime.strptime(birthday, "%Y-%m-%d").date()
        self.save_data()
        print("Contact updated successfully.")

    def delete_contact(self, index):
        if index < 0 or index >= len(self.contacts):
            print("Contact not found.")
            return
        del self.contacts[index]
        self.save_data()
        print("Contact deleted successfully.")

    def list_contacts_by_birthday(self, days):
        today = datetime.today().date()
        future_date = today + timedelta(days=days)
        results = [contact for contact in self.contacts if today <= contact.birthday <= future_date]
        for contact in results:
            print(contact.to_str())

    def add_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)
        self.save_data()
        print("Note added successfully.")

    def search_notes(self, query):
        results = [note for note in self.notes if query.lower() in note.title.lower()]
        for note in results:
            print(note.to_str())

    def edit_note(self, index, title=None, content=None):
        if index < 0 or index >= len(self.notes):
            print("Note not found.")
            return
        note = self.notes[index]
        if title:
            note.title = title
        if content:
            note.content = content
        self.save_data()
        print("Note updated successfully.")

    def delete_note(self, index):
        if index < 0 or index >= len(self.notes):
            print("Note not found.")
            return
        del self.notes[index]
        self.save_data()
        print("Note deleted successfully.")
