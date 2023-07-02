import json
import glob
import importlib.util
from db_models import User, Message, Avatar

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Import variables ending with '_pages from files
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
def get_inbox_messages(id):
    messages = Message.query.filter_by(recipient_id = id).all()
    inbox_messages = []
    for message in messages:
        d = Message.to_dict(message)
        d['avatar'] = message.author.avatar.image.decode('latin-1') if message.author.avatar else None
        d['avatar_format'] = message.author.avatar.image_format if message.author.avatar else None
        inbox_messages.append(d)
    return inbox_messages
