from src.sorting import sort_by

list_mock = [
    {
        "max_salary": 3800,
        "min_salary": 3200,
        "data_posted": "16-11-2018"
    },
    {
        "max_salary": 4600,
        "min_salary": 3900,
        "data_posted": "04-07-2017"
    },
]

min_salary_mock = [
    {
        "max_salary": 3800,
        "min_salary": 3200,
        "data_posted": "16-11-2018"
    },
    {
        "max_salary": 4600,
        "min_salary": 3900,
        "data_posted": "04-07-2017"
    },
]

max_salary_mock = [
    {
        "max_salary": 4600,
        "min_salary": 3900,
        "data_posted": "04-07-2017"
    },
    {
        "max_salary": 3800,
        "min_salary": 3200,
        "data_posted": "16-11-2018"
    }
]

data_posted_mock = [
    {
        "max_salary": 3800,
        "min_salary": 3200,
        "data_posted": "16-11-2018"
    },
    {
        "max_salary": 4600,
        "min_salary": 3900,
        "data_posted": "04-07-2017"
    }
]


def test_sort_by_criteria():
    sort_by(list_mock, "max_salary")
    assert list_mock == max_salary_mock

    sort_by(list_mock, "min_salary")
    assert list_mock == min_salary_mock

    sort_by(list_mock, "date_posted")
    assert list_mock == data_posted_mock
