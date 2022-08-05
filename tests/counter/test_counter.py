from src.counter import count_ocurrences

path = "src/jobs.csv"


def test_counter():
    assert count_ocurrences(path, "PYtHoN")
    assert count_ocurrences(path, "python")
    assert count_ocurrences(path, "JavaScript")
    assert count_ocurrences(path, "jaVASCript")
