# pyrestest
This repository provides some working boilerplate code for building automated test suites on top of the lemoncheesecake test framework and uses the "component-tests" model for functional testing of RESTful APIs.

### Below are some of the features of this test framework:
  - Uses [lemoncheesecake](http://lemoncheesecake.io/) as a core functional test framework
  - Provides pre-configured Slack reporting requiring only `SLACK_AUTH_TOKEN` and channel name
  - Provides a way to define different base URL based test environment configurations
  - Provides a way to run one or more of your test suites in a single run serially

### Below is the explanation of the key files/directories/modules in the code:
- The `components` module contains all the individual component files, e.g. `user.py`. The scope of a component file is to define various HTTP methods pertaining to an individual REST entity under test.
- The `core` module contains various other directories like `common`, `conf`, `utils`, etc.
-- The `common` module contains files like `endpoint_constants.py` (used to define various HTTP endpoints to be tested and used in a component file), `header.py` (used to define a `Header` class for passing request headers while making a HTTP request in a component file), `init.py` (used to initialise all the base URLs of APIs under test using a `Config` object) and `request.py` (a wrapper around Python's `requests` module's HTTP methods with additional `lemoncheesecake` logging).
-- The `conf` module contains an `environment` module, which lets you define various test environments (base URLs for the most part). Note that the `config.py` uses Python's `importlib` module to define a `config` object using the `TEST_ENV` environment variable set while running the tests.
-- The `utilities` module lets you define various utility functions.
- The `scripts` directory contains various ad-hoc scripts, e.g. `test_ping.py` (used to check if all the endpoints under test are up).
- The `tests` module contains the actual API tests.
- The `entrypoint.sh` script does reporting related tasks and uses another `run.sh` script which is run per test suite. You must edit various variables like `SLACK_AUTH_TOKEN`, `SLACK_CHANNEL`, `ALL_TEST_SUITES` as per your needs.
- In the `run.sh` script, your must edit various variables like `SERVER_URL`, `WWW_REPORTS_DIR`, `VENV_NAME` as per your needs.

### Getting a Slack API access token
You can obtain a Slack API access token for your workspace by following the steps below:
1. In your Slack Workspace, click the Apps section.
2. In the Apps page, click Manage apps.
3. The App Directory page shows up, in this page, make a search using the keyword “bots” in the top text box Search App Directory.
4. Click Bots app > Add configuration.
5. Set Username and click Add bot integration.
6. You’ll get the API access token in Integration Settings.

### Examples
This repository contains below examples to run some simple API tests from the endpoints from https://jsonplaceholder.typicode.com/ in the test suite file `tests/user_tests.py`. The required base URLs and actual endpoints can be found in `core/conf/environments/default.py` and `core/common/endpoint_constants.py` files respectively.
1. `verify_get_all_users` - Makes a GET API call to the `/users` endpoint and checks if the number of users returned in the response in greater than 1.
2. `verify_get_user_details` - Makes a GET API call to the `/users` endpoint by passing a given `userId` in the path parameters of the API request and checks if the `id` returned in the response is same as that in the request.
3. `verify_create_user` - Makes a POST API call to the `/users` endpoint by passing the required payload to the request and checks if the user gets created successfully.

### Setting up and running tests
1. Once you have cloned this repository, you should create a virtual environment using the `virtualenv` tool in the root directory of the project. Note that the name of this virtual environment should be the same as that in the `run.sh` and `.gitignore` files.
`$ virtualenv venv_name`
2. Activate the virtual environment with `$ source venv_name/bin/activate`
3. Install all the project dependencies with `$ pip install -r requirements.txt`
4. Set `PYTHONPATH` to the project's root directory.
5. Set `TEST_ENV` to a suitable configuration defined in the `environment` module. Not setting this will make the test framework use the `default` configuration defined in the `environment` module since we have defined this under `config.py`.
6. Run tests with `entrypoint.sh`. Providing no arguments to this script will run all the test suites defined in the `ALL_TEST_SUITES` shell variable in the given order. In order to run one or more test suites in a custom order, you can use `entrypoint.sh my_test_suite_1 my_test_suite_2` (note no `.py` extension in the test suite names).

That's all folks. Happy testing!
