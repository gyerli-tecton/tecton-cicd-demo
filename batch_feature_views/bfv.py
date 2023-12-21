from tecton import (
    FeatureService,
    FeatureView,
    FilteredSource,
    Aggregation,
    materialization_context,
    batch_feature_view
)

from datetime import datetime, timedelta

from entities.entity import user
from data_sources.ds import txn_batch

@batch_feature_view(
    name="user_txns_time_window",
    sources=[FilteredSource(txn_batch)],
    entities=[user],
    mode="spark_sql",
    aggregation_interval=timedelta(days=1),
    aggregations=[
        Aggregation(column="txn", function="count", time_window=timedelta(days=2)),
        Aggregation(column="txn", function="count", time_window=timedelta(days=7)),
        Aggregation(column="txn", function="count", time_window=timedelta(days=10))
    ],
    online=True,
    offline=True,
    feature_start_time=datetime(2023, 8, 10)
)
def user_txns_time_window(txn_batch):
    return f"""
        select
            user_id,
            timestamp,
            1 as txn
        from {txn_batch}
    """