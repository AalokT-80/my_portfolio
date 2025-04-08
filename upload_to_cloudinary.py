import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

# ---------- Configure Cloudinary ----------
cloudinary.config(
    cloud_name='danqibpnf',       # replace with your cloud name
    api_key='692613755368349',             # replace with your API key
    api_secret='u4aiqrwqpp83_CcZ1pJ9YBytJ7A',       # replace with your API secret
    secure=True
)

# ---------- Define Media Directory ----------
MEDIA_DIR = 'media'

# ---------- Traverse and Upload ----------
def upload_media_to_cloudinary():
    for root, dirs, files in os.walk(MEDIA_DIR):
        for file in files:
            local_path = os.path.join(root, file)

            # Relative folder path in Cloudinary (e.g., certificates, resumes)
            relative_folder = os.path.relpath(root, MEDIA_DIR).replace("\\", "/")

            print(f"Uploading {local_path} to folder: {relative_folder}...")

            try:
                response = cloudinary.uploader.upload(
                    local_path,
                    folder=relative_folder
                )
                print(f"✅ Uploaded: {response['secure_url']}\n")
            except Exception as e:
                print(f"❌ Failed to upload {file}: {str(e)}\n")

# ---------- Run It ----------
if __name__ == '__main__':
    upload_media_to_cloudinary()
