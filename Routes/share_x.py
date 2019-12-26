from flask import Blueprint, request
import os, mimetypes, config

share_x = Blueprint(__name__, __name__)

@share_x.route('/share_x', methods=['POST'])
def run():
    # Get sent file, key, and name
    file = request.files['d']
    key = request.form.get('key')
    name = request.form.get('name')
    # Find file extension
    ext = mimetypes.guess_extension(file.content_type)

    # Check key agsint local key
    if key != config.SHAREX_KEY:
        return 'Unauthorized!', 401
    
    # TODO: Save into mongodb
    # Save file
    file.save(os.path.join(f'{os.path.abspath("./")}/Share_X_Test', f'{name}{ext}'))
    
    return f'{config.URL}/{name}{ext}', 200 
