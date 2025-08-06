


# 📁 Flask File Upload API

A lightweight Flask REST API for uploading images and videos, organizing them into folders by section, and generating unique filenames.

---

## 💡 Features

- Upload images and videos via `POST` requests
- Store files in separate folders by section
- Generate a unique filename for each uploaded file
- Hosted for free on [PythonAnywhere](https://www.pythonanywhere.com/)
- Easy integration with mobile apps (e.g., Flutter, Firebase, etc.)

---

## 🔧 How to Use

### 📤 Endpoint:

POST https://yourusername.pythonanywhere.com/upload
```

---

### 🐍 Uploading a file using Python

```python
import requests

url = 'https://yourusername.pythonanywhere.com/upload'
file_path = 'path/to/your/image.jpg'
section = 'cars'  # Folder name (section)

with open(file_path, 'rb') as f:
    files = {'file': f}
    data = {'section': section}
    response = requests.post(url, files=files, data=data)

if response.status_code == 200:
    print(" Uploaded successfully!")
    print("File URL:", response.json().get("url"))
else:
    print(" Upload failed:", response.text)
```

---

### 📱 Uploading from a Flutter App

```dart
import 'dart:io';
import 'package:http/http.dart' as http;
import 'package:path/path.dart';
import 'dart:convert';

Future<String?> uploadImageToServer(File imageFile, String section) async {
  final url = Uri.parse("https://yourusername.pythonanywhere.com/upload");

  var request = http.MultipartRequest('POST', url)
    ..fields['section'] = section
    ..files.add(await http.MultipartFile.fromPath('file', imageFile.path));

  var response = await request.send();

  if (response.statusCode == 200) {
    final responseData = await response.stream.bytesToString();
    final jsonData = jsonDecode(responseData);
    return jsonData['url']; // Image URL
  } else {
    print(" Upload failed: ${response.statusCode}");
    return null;
  }
}
```

---

## 📞 Contact

For support, feel free to reach out:

- Telegram: [@SyberSc71](https://t.me/SyberSc71)
- Telegram: [@WAT4F](https://t.me/WAT4F)
- GitHub: [waheeb71](https://github.com/waheeb71)
- GitHub2: [cyberlangdev](https://github.com/cyberlangdev)
- **Location:** I am from Yemen, Taiz.
- **YouTube Channel:** [Cyber Code](https://www.youtube.com/@cyber_code1)
- **X (formerly Twitter):** [@wa__cys](https://x.com/wa__cys)



---
## 📄 License

This project is released into the public domain under [The Unlicense](LICENSE).

---

# واجهة API لرفع الملفات باستخدام Flask

مشروع REST API بسيط باستخدام Flask لرفع الصور والفيديوهات وتخزينها في مجلدات حسب الأقسام، مع إنشاء اسم فريد لكل ملف.

---

## 💡 المميزات

- رفع الصور والفيديوهات عبر طلب `POST`
- تخزين الملفات في مجلدات منفصلة لكل قسم
- توليد اسم فريد لكل ملف
- رفع مجاني عبر [PythonAnywhere](https://www.pythonanywhere.com/)
- إمكانية ربطه مع التطبيقات مثل Flutter وFirebase

---

## 🔧 طريقة الاستخدام

### 📤 نقطة الوصول:
```
POST https://yourusername.pythonanywhere.com/upload
```

---

### 🐍 أولاً: رفع صورة باستخدام Python

```python
import requests

url = 'https://yourusername.pythonanywhere.com/upload'
file_path = 'path/to/your/image.jpg'
section = 'cars'  # القسم

with open(file_path, 'rb') as f:
    files = {'file': f}
    data = {'section': section}
    response = requests.post(url, files=files, data=data)

if response.status_code == 200:
    print("تم رفع الصورة بنجاح!")
    print("رابط الملف:", response.json().get("url"))
else:
    print(" فشل في الرفع:", response.text)
```

---

### 📱 ثانيًا: رفع صورة باستخدام Flutter

```dart
import 'dart:io';
import 'package:http/http.dart' as http;
import 'package:path/path.dart';
import 'dart:convert';

Future<String?> uploadImageToServer(File imageFile, String section) async {
  final url = Uri.parse("https://yourusername.pythonanywhere.com/upload");

  var request = http.MultipartRequest('POST', url)
    ..fields['section'] = section
    ..files.add(await http.MultipartFile.fromPath('file', imageFile.path));

  var response = await request.send();

  if (response.statusCode == 200) {
    final responseData = await response.stream.bytesToString();
    final jsonData = jsonDecode(responseData);
    return jsonData['url']; // رابط الصورة
  } else {
    print(" فشل رفع الصورة: ${response.statusCode}");
    return null;
  }
}
```

---

## 📞 التواصل

لأي استفسار أو دعم:

- تليجرام: [@SyberSc71](https://t.me/SyberSc71)
- تليجرام: [@WAT4F](https://t.me/WAT4F)
- جيت هاب: [waheeb71](https://github.com/waheeb71)
  جيب هاب2:[cyberlangdev](https://github.com/cyberlangdev)
- **قناة اليوتيوب:** [Cyber Code](https://www.youtube.com/@cyber_code1)
- **حسابي على منصة إكس (تويتر سابقًا):** [@wa__cys](https://x.com/wa__cys)



---
