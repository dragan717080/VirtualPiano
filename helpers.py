import json
import glob
import importlib.util
from db_models import User, Message, MusicSheet, Artist
from abc import ABC

class Helpers(ABC):

    @staticmethod
    def read_json_file(file_name, file_path='data/'):
        with open(f'{file_path}/{file_name}.json',  'r') as file:
            data = json.load(file)
        return data

    # Import variables ending with '_pages from files
    @staticmethod
    def get_blueprints(folder_path = 'routing/'):
        file_paths = glob.glob(folder_path + '*.py')

        blueprints = []
        for file_path in file_paths:
            file_name = file_path[:-3].split('/')[-1]  # Extract the file name without the '.py' extension
            module_name = file_name.replace('.', '_')  # Convert the file name to a valid module name
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Filter and retrieve variables that end with '_pages'
            blueprints.append([getattr(module, var) for var in dir(module) if var.endswith('_pages')][0])
        
        return blueprints
        
    # Get inbox messages for user with the given id
    @staticmethod
    def get_inbox_messages(id):
        messages = Message.query.filter_by(recipient_id = id).all()

        return [[{**Message.to_dict(message), 'author': message.author.username,
            'avatar': message.author.avatar.image.decode('latin-1') if message.author.avatar else None,
            'avatar_format': message.author.avatar.image_format if message.author.avatar else None}
            for message in messages
        ]]

    @staticmethod
    def get_latest_sheets():
        sheets = [item.to_dict(item) for item in MusicSheet.get_latest()]
        return [{**sheet, 'author': User.get(id=sheet['author_id']).username} 
            for sheet in sheets]

    # Get users that have submitted the most music sheets
    @staticmethod
    def get_most_active_users(limit = None):
        return sorted([
            {
                'username': user.username,
                'sheets': len(user.music_sheets),
                'comments': len(user.comments),
                'avatar': user.avatar.image if user.avatar else None,
                'avatar_format': user.avatar.image_format if user.avatar else None
            }
            for user in User.query.all()
            if len(user.music_sheets) > 0
        ], key=lambda i: i['sheets'], reverse=True)[:limit]

    @classmethod
    def save_sheet_with_known_artist(cls, uploaded_sheet_title, artist_name, sheet_params):
        sheet_params['title'] = \
            cls.find_substr_between_two_str(uploaded_sheet_title, ' - ', '.txt')
        artist = Artist.get(name=artist_name)
        sheet = MusicSheet(**sheet_params)

        # Artist is not in database
        if not artist:
            artist = Artist(name=artist_name)
            artist.save()
            sheet.artist_id = artist.id
        # Artist is in database
        else:
            sheet.artist_id = artist.id
        sheet.save()
        
    # Example: 'Garbage - Cup of Coffee.txt' returns 'Cup of Coffee'
    @staticmethod
    def find_substr_between_two_str(input_str, start_marker, end_marker):
        start_index = input_str.index(start_marker) + len(start_marker)
        end_index = input_str.index(end_marker)

        return input_str[start_index:end_index]
