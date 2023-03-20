import os
import shutil

from PIL import Image

# Set the folder containing the photos to sort
folder = "./photos_to_sort"

# Create a new folder to store the sorted photos
sorted_folder = os.path.join("sorted")
os.makedirs(sorted_folder, exist_ok=True)

# Create a new folder to store the unrecognized photos
unrecognized_folder = os.path.join(sorted_folder, "unrecognized")
os.makedirs(unrecognized_folder, exist_ok=True)

# Get a list of all the files in the folder
files = os.listdir(folder)

# Loop through each file and check if it's a photo
for file in files:
    # Check if the file is a JPEG or PNG image
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        # Open the image file and read the EXIF data
        image_path = os.path.join(folder, file)
        print(image_path)
        try:
            with Image.open(image_path) as img:
                exif_data = img.getexif()
                print(exif_data)
            # Extract the GPS coordinates from the EXIF data
            if exif_data and 34853 in exif_data:
                gps_data = exif_data[34853]
                lat = gps_data[2][0] + gps_data[2][1] / 60 + gps_data[2][2] / 3600
                lng = gps_data[4][0] + gps_data[4][1] / 60 + gps_data[4][2] / 3600
                lat_ref = gps_data[1]
                lng_ref = gps_data[3]
                if lat_ref == "S":
                    lat = -lat
                if lng_ref == "W":
                    lng = -lng
                # Create a folder for the location with a tolerance of 1km
                location_folder = os.path.join(sorted_folder, f"location_{round(lat, 3)}_{round(lng, 3)}")
                os.makedirs(location_folder, exist_ok=True)
                # Move the photo to the location folder
                shutil.move(image_path, os.path.join(location_folder, file))
        except:
                # Move the photo to the unrecognized folder
                shutil.move(image_path, os.path.join(unrecognized_folder, file))
                print("No")
