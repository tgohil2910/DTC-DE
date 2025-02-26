from google.cloud import bigquery
import matplotlib.pyplot as plt
import pandas as pd

# Construct a BigQuery client object.
client = bigquery.Client()

query = """
   SELECT event_name,
   COUNT(*) AS event_count
   FROM `dtc-de-course-450915.GitCommitsDataset.GASourceTable`
   WHERE PARSE_DATE('%Y%m%d', event_date) BETWEEN DATE('2020-12-25') AND DATE('2021-12-25')
   GROUP BY 1
   ORDER BY 2 DESC;
   """
query_job = client.query(query)  # Make an API request.

# Convert the results to a Pandas DataFrame.
df = query_job.to_dataframe()

# Create a bar chart using Matplotlib.
plt.figure(figsize=(10, 6))  # Adjust figure size as needed
plt.bar(df['event_name'], df['event_count'])
plt.xlabel("Event Name")
plt.ylabel("Event Count")
plt.title("Event Counts")
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels if needed
plt.tight_layout() # Adjust layout to prevent labels from overlapping
plt.savefig("event_counts.pdf", dpi=300) # Save as PDF

# Show the plot (optional)
plt.show()

# Now you can include event_counts.pdf in your paper and refer to it in your text.