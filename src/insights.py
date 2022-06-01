from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    data = read(path)
    types_job = set()
    for job in data:
        types_job.add(job["job_type"])
    return [types for types in types_job]


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided list jobs by type
    """
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    data = read(path)
    industries = set()
    for industry in data:
        industries.add(industry["industry"])
    return [industry for industry in industries if len(industry) > 0]


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return [row for row in jobs if row["industry"] == industry]


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    data = read(path)
    wage = set()
    for value in data:
        wage.add(value["max_salary"])
    salary = [float(salary) for salary in wage if salary.isdigit()]
    max_salary = 0
    for value in salary:
        if max_salary < value:
            max_salary = value
    return max_salary


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    data = read(path)
    wage = set()
    for value in data:
        wage.add(value["min_salary"])
    salary = [float(salary) for salary in wage if salary.isdigit()]
    min_salary = 0
    for value in salary:
        if min_salary == 0:
            min_salary = value
        if value < min_salary:
            min_salary = value
    return min_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    if not isinstance(
        job["min_salary"], int
    ) or not isinstance(
        job["max_salary"], int
    ):
        raise ValueError
    if type(salary) != int or job["min_salary"] > job["max_salary"]:
        raise ValueError
    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
    return False


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    list_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list_jobs.append(job)
        except ValueError:
            pass
    return list_jobs

# Ref (isinstance): https://www.w3schools.com/python/ref_func_isinstance.asp
