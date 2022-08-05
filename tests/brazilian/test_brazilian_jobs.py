from src.brazilian_jobs import read_brazilian_file

path = "tests/mocks/brazilians_jobs.csv"


def test_brazilian_jobs():
    jobs = read_brazilian_file(path)
    for job in jobs:
        assert "title" in job
        assert "salary" in job
        assert "type" in job
