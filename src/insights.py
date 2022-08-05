from src.jobs import read


def get_unique_job_types(path):
    result = set()
    jobs = read(path)
    for job in jobs:
        if job["job_type"] != "":
            result.add(job["job_type"])

    return result


def filter_by_job_type(jobs, job_type):
    filtered = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered.append(job)

    return filtered


def get_unique_industries(path):
    result = set()
    jobs = read(path)
    for job in jobs:
        if job["industry"] != "":
            result.add(job["industry"])

    return result


def filter_by_industry(jobs, industry):
    filtered = []
    for job in jobs:
        if job["industry"] == industry:
            filtered.append(job)

    return filtered


def get_max_salary(path):
    salaries = []
    jobs = read(path)
    for job in jobs:
        # https://www.w3schools.com/python/ref_string_isnumeric.asp
        if job["max_salary"].isnumeric():
            salaries.append(int(job["max_salary"]))

    return max(salaries)


def get_min_salary(path):
    salaries = []
    jobs = read(path)
    for job in jobs:
        if job["min_salary"].isnumeric():
            salaries.append(int(job["min_salary"]))

    return min(salaries)


def matches_salary_range(job, salary):
    # will try to convert all the necessary data to int
    try:
        max_salary = int(job["max_salary"])
        min_salary = int(job["min_salary"])
        salary = int(salary)
    # it may cause TypeError, bc param not number
    except TypeError:
        raise ValueError("invalid param, must be an integer")
    # or KeyError, bc job doesn't have one or both key
    except KeyError:
        raise ValueError("invalid job, missing salary")

    # if min_salary it's bigger than max_salary, it's invalid
    if min_salary > max_salary:
        raise ValueError("invalid job salary")

    return min_salary <= salary <= max_salary


def filter_by_salary_range(jobs, salary):
    result = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                result.append(job)
        except ValueError:
            print(ValueError("invalid params, must be an integer"))

    return result
