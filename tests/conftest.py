import pytest


def pytest_addoption(parser):
    """
    Adds command line options to pytest.
    :param parser: pytest parser object
    :type parser: pytest.config.Parser
    """
    parser.addoption(
        '--base-url', action='store', default='https://jsonplaceholder.typicode.com',
        help='Base URL for the API datatests'
    )


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption('--base-url')


@pytest.fixture(scope="session")
def step_context():
    return {}
