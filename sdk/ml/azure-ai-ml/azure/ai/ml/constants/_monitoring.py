# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from enum import Enum

from azure.core import CaseInsensitiveEnumMeta

from azure.ai.ml._utils._experimental import experimental


ALL_FEATURES = "all_features"


AZMONITORING = "azmonitoring"

DEPLOYMENT_MODEL_INPUTS_NAME_KEY = "data_collector.collections.model_inputs.data.name"
DEPLOYMENT_MODEL_INPUTS_VERSION_KEY = "data_collector.collections.model_inputs.data.version"
DEPLOYMENT_MODEL_OUTPUTS_NAME_KEY = "data_collector.collections.model_outputs.data.name"
DEPLOYMENT_MODEL_OUTPUTS_VERSION_KEY = "data_collector.collections.model_outputs.data.version"
DEPLOYMENT_MODEL_INPUTS_COLLECTION_KEY = "data_collector.collections.model_inputs.enabled"
DEPLOYMENT_MODEL_OUTPUTS_COLLECTION_KEY = "data_collector.collections.model_outputs.enabled"


SPARK_INSTANCE_TYPE_KEY = "compute.spark.resources.instance_type"
SPARK_RUNTIME_VERSION = "compute.spark.resources.runtime_version"


@experimental
class MonitorSignalType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    DATA_DRIFT = "data_drift"
    DATA_QUALITY = "data_quality"
    PREDICTION_DRIFT = "prediction_drift"
    MODEL_PERFORMANCE = "model_performance"
    FEATURE_ATTRIBUTION_DRIFT = "feature_attribution_drift"
    CUSTOM = "custom"


@experimental
class MonitorMetricName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    JENSEN_SHANNON_DISTANCE = "jensen_shannon_distance"
    NORMALIZED_WASSERSTEIN_DISTANCE = "normalized_wasserstein_distance"
    POPULATION_STABILITY_INDEX = "population_stability_index"
    TWO_SAMPLE_KOLMOGOROV_SMIRNOV_TEST = "two_sample_kolmogorov_smirnov_test"
    PEARSONS_CHI_SQUARED_TEST = "pearsons_chi_squared_test"
    NULL_VALUE_RATE = "null_value_rate"
    DATA_TYPE_ERROR_RATE = "data_type_error_rate"
    OUT_OF_BOUND_RATE = "out_of_bounds_rate"
    NORMALIZED_DISCOUNTED_CUMULATIVE_GAIN = "normalized_discounted_cumulative_gain"
    ACCURACY = "accuracy"
    PRECISION = "precision"
    RECALL = "recall"
    F1_SCORE = "f1_score"
    MAE = "MAE"
    MSE = "MSE"
    RMSE = "RMSE"


@experimental
class MonitorModelType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    CLASSIFICATION = "classification"
    REGRESSION = "regression"


@experimental
class MonitorFeatureType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    NUMERICAL = "numerical"
    CATEGORICAL = "categorical"
    NOT_APPLICABLE = "not_applicable"
    ALL_FEATURE_TYPES = "all_feature_types"


@experimental
class MonitorDatasetContext(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    MODEL_INPUTS = "model_inputs"
    MODEL_OUTPUTS = "model_outputs"
    TRAINING = "training"
    TEST = "test"
    VALIDATION = "validation"
    GROUND_TRUTH_DATA = "ground_truth"


class DefaultMonitorSignalNames(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    DATA_DRIFT_SIGNAL = "data-drift-signal"
    PREDICTION_DRIFT_SIGNAL = "prediction-drift-signal"
    DATA_QUALITY_SIGNAL = "data-quality-signal"
