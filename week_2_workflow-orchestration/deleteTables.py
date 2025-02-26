DECLARE table_list ARRAY<STRING>;

SET table_list = (
  SELECT ARRAY_AGG(TABLE_NAME)
  FROM `dtc-de-course-450915.zoomcamp.INFORMATION_SCHEMA.TABLES`
  WHERE TABLE_NAME LIKE 'fhv_tripdata_2019_%_ext'
     OR TABLE_NAME LIKE 'fhv_tripdata_2020_%_ext'
     OR TABLE_NAME LIKE 'fhv_tripdata_2021_%_ext'
);

FOR table_name IN (SELECT * FROM UNNEST(table_list)) DO
  EXECUTE IMMEDIATE FORMAT("""
    DROP TABLE `dtc-de-course-450915.zoomcamp.%s`;
  """, table_name);
END FOR;
