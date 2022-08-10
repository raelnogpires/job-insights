from src.brazilian_jobs import read_brazilian_file

path = "tests/brazilian/brazilians_jobs_mock.csv"


def test_brazilian_jobs():
    jobs = read_brazilian_file(path)
    for job in jobs:
        assert "title" in job
        assert "salary" in job
        assert "type" in job
