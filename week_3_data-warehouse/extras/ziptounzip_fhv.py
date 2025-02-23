from google.cloud import storage
import gzip
import shutil
from io import BytesIO  # Import BytesIO

def unzip_gz_files_in_gcs(bucket_name, file_names, destination_folder):
    client = storage.Client(project="dtc-de-course-450915")  # Set your project ID
    bucket = client.bucket(bucket_name)

    for file_name in file_names:
        print("Working on " + file_name)
        # Download the .gz file
        blob = bucket.blob("fhv/" + file_name)
        gz_content = blob.download_as_bytes()
        
        
        # Unzip the file
        with gzip.GzipFile(fileobj=BytesIO(gz_content), mode='rb') as gz_file:
            uncompressed_data = gz_file.read()

        destination_blob_name = destination_folder + "/" + file_name.replace(".gz", "")
        
        # Upload the unzipped file back to GCS
        new_blob = bucket.blob(destination_blob_name)
        new_blob.upload_from_string(uncompressed_data)

        print(f"Unzipped and uploaded: {destination_blob_name}")


file_names = [
    "fhv_tripdata_2019-02.csv.gz",
    "fhv_tripdata_2019-03.csv.gz",
    "fhv_tripdata_2019-04.csv.gz",
    "fhv_tripdata_2019-05.csv.gz",
    "fhv_tripdata_2019-06.csv.gz",
    "fhv_tripdata_2019-07.csv.gz",
    "fhv_tripdata_2019-08.csv.gz",
    "fhv_tripdata_2019-09.csv.gz",
    "fhv_tripdata_2019-10.csv.gz",
    "fhv_tripdata_2019-11.csv.gz",
    "fhv_tripdata_2019-12.csv.gz",
    "fhv_tripdata_2020-01.csv.gz",
    "fhv_tripdata_2020-02.csv.gz",
    "fhv_tripdata_2020-03.csv.gz",
    "fhv_tripdata_2020-04.csv.gz",
    "fhv_tripdata_2020-05.csv.gz",
    "fhv_tripdata_2020-06.csv.gz",
    "fhv_tripdata_2020-07.csv.gz",
    "fhv_tripdata_2020-08.csv.gz",
    "fhv_tripdata_2020-09.csv.gz",
    "fhv_tripdata_2020-10.csv.gz",
    "fhv_tripdata_2020-11.csv.gz",
    "fhv_tripdata_2020-12.csv.gz",
    "fhv_tripdata_2021-01.csv.gz",
    "fhv_tripdata_2021-02.csv.gz",
    "fhv_tripdata_2021-03.csv.gz",
    "fhv_tripdata_2021-04.csv.gz",
    "fhv_tripdata_2021-05.csv.gz",
    "fhv_tripdata_2021-06.csv.gz",
    "fhv_tripdata_2021-07.csv.gz",
]
destination_folder = "fhv-csv"  # Change to the folder where you want unzipped files

unzip_gz_files_in_gcs("tushar-gohil-week3", file_names, destination_folder)
