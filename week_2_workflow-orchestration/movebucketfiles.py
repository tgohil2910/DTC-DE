from google.cloud import storage

def move_files_between_buckets(source_bucket_name, destination_bucket_name, file_prefix=""):
    """
    Moves multiple files from one GCS bucket to another without preserving folder structure.

    :param source_bucket_name: Name of the source GCS bucket.
    :param destination_bucket_name: Name of the destination GCS bucket.
    :param file_prefix: (Optional) Prefix of files to move. Defaults to empty string to capture all files.
    """
    client = storage.Client()
    source_bucket = client.bucket(source_bucket_name)
    destination_bucket = client.bucket(destination_bucket_name)
    
    blobs = source_bucket.list_blobs(prefix=file_prefix)
    
    for blob in blobs:
        source_blob_name = blob.name
        if not source_blob_name.endswith('.csv'):
            print(f"Skipping {source_blob_name}, not a CSV file.")
            continue
        destination_blob_name = f"{source_blob_name.split('/')[-1]}"  # Avoid name conflicts
        destination_blob = destination_bucket.blob(destination_blob_name)
        
        print(f"Processing: {source_blob_name} -> {destination_blob_name}")
        
        # Copy the blob to the destination bucket
        source_bucket.copy_blob(blob, destination_bucket, new_name=destination_blob_name)
        
        # Delete the blob from the source bucket
        # blob.delete()
        
        print(f"Moved {source_blob_name} from {source_bucket_name} to {destination_bucket_name}/{destination_blob_name}")

if __name__ == "__main__":
    source_bucket = "tushar-gohil-week3"
    destination_bucket = "tushar-gohil-codespace-kestra"
    file_prefix = "yellow-csv/yellow_tripdata_202"  # Ensure this is the correct folder prefix
    
    move_files_between_buckets(source_bucket, destination_bucket, file_prefix)

# gs://tushar-gohil-week3/green-csv/green_tripdata_2019-01.csv