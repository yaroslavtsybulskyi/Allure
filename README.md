# README
Allure is a powerful test reporting framework commonly used in software development, especially in the realm of automated testing. Allure enables the generation of detailed and visually appealing reports, offering valuable insights into test results. This facilitates easier analysis and understanding of test outcomes for developers and QA teams.

## Prerequisites
Before running the code, ensure that you have the following installed:
 - Allure
 - Requests
 - Pytest

## Usage

Follow these simple steps:

1. Open Terminal.
2. Navigate to the project directory.
3. Run Tests: Execute the following command to run the tests and save the results to the allure_result folder:
   
```
pytest --alluredir=allure_result tests
```  

4. Generate Visualization: After running the tests, generate a visualization of the results using the following command:
```
allure serve allure_result
```
This command will generate a dashboard where you can explore the detailed results of the test run.

As a result, you should see a similar dashboard view: 

[![Allure Dashboard](https://i.postimg.cc/sDnRXgZx/Screenshot-2024-02-17-at-15-06-05.png)](https://postimg.cc/2VBt9mGN)
