# QA_test_task
innitial commit

Here are some of the key points this project:

*code was written in Python 3.6 using Selenium WebDriver framework and "unittest" built-in Python's library to assert data<br />
*tests are launched in Google Chrome browser, using Chrome webdriver<br />
*elements of the Page Object Pattern were implemented during creating the project, recurring elements were splitted into separated classes<br />
*in order to launch the test suite you can run the class named "TestSuite" within the Tests/TestSuite.py in any Python's IDE
or you can do it using the "pystest" lib https://docs.pytest.org/en/latest/ via the command-line.


To launch it via the Pytest and generate test report:

Required packages preinstalled:

*pytest<br />
*pytest-html<br />
*pytest-xdist (for distributed testing) - optional<br />

Example command to execute in the command-line:

pytest -vv <path_to_testsuite> -n=<number of CPU's, can be set up on AUTO> --html=<path_where_report_would_be_generated> --self-contained-html

If you have any further questions regarding the tests or any other, feel free to contact me oleksij.gnatiuk@gmail.com
