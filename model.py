import modelop.monitors.volumetrics as volumetrics
import modelop.utils as utils

logger = utils.configure_logger()


# modelop.init
def init():
    pass


# modelop.metrics
def metrics(df_1, df_2):
    # Initialize Volumetric monitor with 1st input DataFrame
    volumetric_monitor = volumetrics.VolumetricMonitor(df_1)

    # Run an OOTB test
    count_comparison = volumetric_monitor.count_comparison(df_2)

    # Add a custom test
    count_1 = df_1.shape[0]
    count_2 = df_2.shape[0]
    percent_difference = percent_different(count_1, count_2)
    percent_difference_comparison = {
        "test_category": "volumetrics",
        "test_id": "volumetrics_count_percent_difference_comparison",
        "test_name": "Count Percent Difference",
        "test_type": "count_comparison",
        "values": {
            "percent_difference": percent_difference,
        },
    }

    result = {
        # Boolean top-level metric
        "record_count_difference": count_comparison["values"][
            "record_count_difference"
        ],
        "percent_difference": percent_difference,
        # Complete test results
        "volumetrics": [
            count_comparison,
            percent_difference_comparison,
        ],
    }
    yield result


def percent_different(count_1, count_2):
    top = abs(count_1 - count_2)
    bottom = (count_1 + count_2) / 2
    return top / bottom


if __name__ == "__main__":
    import pandas

    baseline = pandas.read_json("df_baseline_scored.json", lines=True)
    sample = pandas.read_json("df_sample_scored.json", lines=True)

    from pprint import pprint

    pprint(next(metrics(baseline, sample)))
