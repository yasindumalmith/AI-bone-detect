try:
    import multipart
    print("✅ python-multipart is installed (module 'multipart')")
except ImportError:
    print("❌ python-multipart NOT found (module 'multipart')")

try:
    from fastapi import UploadFile
    print("✅ FastAPI UploadFile imported")
except ImportError:
    print("❌ FastAPI NOT found")
