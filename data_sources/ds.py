from tecton import HiveConfig, DatetimePartitionColumn, BatchSource

datetime_partition_columns = [
    DatetimePartitionColumn(column_name="partition_0", datepart="year", zero_padded=True),
    DatetimePartitionColumn(column_name="partition_1", datepart="month", zero_padded=True),
    DatetimePartitionColumn(column_name="partition_2", datepart="day", zero_padded=True),
]

hive_config = HiveConfig(
    database="gursoy_fraud_simple", 
    table="txn",
    timestamp_field="timestamp",
    datetime_partition_columns=datetime_partition_columns,
    # data_delay=timedelta(minutes=45) # experiment this to see how _effective_timestamp changes
)

txn_batch = BatchSource(
    name="txn_batch",
    batch_config=hive_config,
    owner="gursoy@tecton.ai"
)