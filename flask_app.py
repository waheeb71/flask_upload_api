from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
import uuid

app = Flask(__name__)


UPLOAD_FOLDER_IMAGES = 'uploads/images'
UPLOAD_FOLDER_VIDEOS = 'uploads/videos'
os.makedirs(UPLOAD_FOLDER_IMAGES, exist_ok=True)
os.makedirs(UPLOAD_FOLDER_VIDEOS, exist_ok=True)


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/')
def home():
    return '✅ السيرفر يعمل!'

@app.route('/delete', methods=['POST'])
def delete_file():
    data = request.get_json()
    if not data or 'file_url' not in data:
        return jsonify({'error': 'يرجى إرسال رابط الملف'}), 400

    file_url = data['file_url']
    base_url = 'https://USERNAME.pythonanywhere.com/'

    if not file_url.startswith(base_url):
        return jsonify({'error': 'رابط الملف غير صالح'}), 400

 
    relative_path = file_url.replace(base_url, '').strip('/')
    file_path = os.path.join(os.getcwd(), relative_path)

    if os.path.isfile(file_path):
        os.remove(file_path)
        return jsonify({'message': '✅ تم حذف الملف بنجاح'}), 200
    else:
        return jsonify({'error': 'الملف غير موجود'}), 404


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files or 'section' not in request.form:
        return jsonify({'error': 'يرجى إرسال ملف واسم القسم'}), 400

    file = request.files['file']
    section = request.form['section'].strip().lower()

    if file.filename == '':
        return jsonify({'error': 'اسم الملف فارغ'}), 400

    if file and allowed_file(file.filename):
        file_ext = file.filename.rsplit('.', 1)[1].lower()
        unique_filename = f"{uuid.uuid4()}.{file_ext}"

        # تحديد نوع الملف (فيديو/صورة)
        media_type = 'videos' if file_ext in ['mp4', 'mov'] else 'images'

        # بناء المسار: uploads/اسم_القسم/images/او/videos/
        section_folder = os.path.join('uploads', section, media_type)
        os.makedirs(section_folder, exist_ok=True)

        save_path = os.path.join(section_folder, unique_filename)
        file.save(save_path)


        base_url = 'https://USERNAME.pythonanywhere.com'//استبدل اسم المستخدم
        file_url = f"{base_url}/{save_path}"

        return jsonify({'url': file_url}), 200

    return jsonify({'error': 'نوع الملف غير مسموح به'}), 400


from flask import send_from_directory

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

if __name__ == '__main__':
    app.run(debug=True)
