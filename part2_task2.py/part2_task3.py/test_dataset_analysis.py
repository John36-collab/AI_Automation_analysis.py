# part2_task3/test_dataset_analysis.py
import pandas as pd
import pytest

@pytest.fixture
def load_dataset():
    df = pd.read_csv("part2_task3/dataset.csv")
    return df

def test_dataset_loaded(load_dataset):
    df = load_dataset
    assert not df.empty, "Dataset failed to load!"

def test_columns_exist(load_dataset):
    df = load_dataset
    expected_columns = {"sepal_length", "sepal_width", "petal_length", "petal_width", "species"}
    assert expected_columns.issubset(df.columns), "Missing columns in dataset"

def test_no_missing_values(load_dataset):
    df = load_dataset
    assert df.isnull().sum().sum() == 0, "Dataset contains missing values"