URLS = {
    "tokyo_xs": "https://drive.google.com/file/d/19vrphwImf7lpoaVlKgHhN07AWj_EfhjR/view?usp=drive_link",
    "sf_xs": "https://drive.google.com/file/d/1JaM1y16fArlSF0KPRqCjggMQCIRwXzJm/view?usp=drive_link",
    "gsv_xs": "https://drive.google.com/file/d/12Zm-VT3f7kCQOLdSJoZh-53Bm2cMj19x/view?usp=drive_link",
    "svox": "https://drive.google.com/file/d/1cpXTLfQ94IcAFQkxCnUjROTVdkwgq23a/view?usp=drive_link"
}

import os
import gdown
import shutil

os.makedirs("data", exist_ok=True)
for dataset_name, url in URLS.items():
    print(f"Downloading {dataset_name}")
    zip_filepath = f"data/{dataset_name}.zip"
    gdown.download(url, zip_filepath, fuzzy=True)
    shutil.unpack_archive(zip_filepath, extract_dir="data")
    os.remove(zip_filepath)
