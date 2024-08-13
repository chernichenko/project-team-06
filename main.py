import setup_path
from assistant import PersonalAssistant
import argparse

def main():
    parser = argparse.ArgumentParser(description="Personal Assistant CLI")
    subparsers = parser.add_subparsers(dest='command')

    # Contact commands
    contact_parser = subparsers.add_parser('contact', help='Manage contacts')
    contact_subparsers = contact_parser.add_subparsers(dest='contact_command')

    contact_parser_add = contact_subparsers.add_parser('add', help='Add a new contact')
    contact_parser_add.add_argument('name', help='Name of the contact')
    contact_parser_add.add_argument('address', help='Address of the contact')
    contact_parser_add.add_argument('phone', help='Phone number of the contact')
    contact_parser_add.add_argument('email', help='Email of the contact')
    contact_parser_add.add_argument('birthday', help='Birthday of the contact (YYYY-MM-DD)')

    contact_parser_search = contact_subparsers.add_parser('search', help='Search for contacts')
    contact_parser_search.add_argument('query', help='Search query')

    contact_parser_edit = contact_subparsers.add_parser('edit', help='Edit an existing contact')
    contact_parser_edit.add_argument('index', type=int, help='Index of the contact to edit')
    contact_parser_edit.add_argument('--name', help='New name of the contact')
    contact_parser_edit.add_argument('--address', help='New address of the contact')
    contact_parser_edit.add_argument('--phone', help='New phone number of the contact')
    contact_parser_edit.add_argument('--email', help='New email of the contact')
    contact_parser_edit.add_argument('--birthday', help='New birthday of the contact (YYYY-MM-DD)')

    contact_parser_delete = contact_subparsers.add_parser('delete', help='Delete a contact')
    contact_parser_delete.add_argument('index', type=int, help='Index of the contact to delete')

    contact_parser_list = contact_subparsers.add_parser('list', help='List contacts by upcoming birthdays')
    contact_parser_list.add_argument('days', type=int, help='Number of days to check for upcoming birthdays')

    # Note commands
    note_parser = subparsers.add_parser('note', help='Manage notes')
    note_subparsers = note_parser.add_subparsers(dest='note_command')

    note_parser_add = note_subparsers.add_parser('add', help='Add a new note')
    note_parser_add.add_argument('title', help='Title of the note')
    note_parser_add.add_argument('content', help='Content of the note')

    note_parser_search = note_subparsers.add_parser('search', help='Search for notes')
    note_parser_search.add_argument('query', help='Search query')

    note_parser_edit = note_subparsers.add_parser('edit', help='Edit a note')
    note_parser_edit.add_argument('index', type=int, help='Index of the note to edit')
    note_parser_edit.add_argument('--title', help='New title of the note')
    note_parser_edit.add_argument('--content', help='New content of the note')

    note_parser_delete = note_subparsers.add_parser('delete', help='Delete a note')
    note_parser_delete.add_argument('index', type=int, help='Index of the note to delete')

    args = parser.parse_args()
    assistant = PersonalAssistant()

    if args.command == 'contact':
        if args.contact_command == 'add':
            assistant.add_contact(args.name, args.address, args.phone, args.email, args.birthday)
        elif args.contact_command == 'search':
            assistant.search_contacts(args.query)
        elif args.contact_command == 'edit':
            assistant.edit_contact(args.index, args.name, args.address, args.phone, args.email, args.birthday)
        elif args.contact_command == 'delete':
            assistant.delete_contact(args.index)
        elif args.contact_command == 'list':
            assistant.list_contacts_by_birthday(args.days)

    elif args.command == 'note':
        if args.note_command == 'add':
            assistant.add_note(args.title, args.content)
        elif args.note_command == 'search':
            assistant.search_notes(args.query)
        elif args.note_command == 'edit':
            assistant.edit_note(args.index, args.title, args.content)
        elif args.note_command == 'delete':
            assistant.delete_note(args.index)

if __name__ == "__main__":
    main()
