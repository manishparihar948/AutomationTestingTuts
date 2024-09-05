Feature: Validate the OrangeHRM login feature

    Background:
        Given I launch the chrome browser
        When  Open the https://opensource-demo.orangehrmlive.com/ website
        Then The login portal has been opened

    @valid_login
    Scenario: Login with valid credentials
        And Provide the username "Admin" and password "admin123"
        And Click on the Login button
        Then Login is successful and dashboard is opened
        Then Close the browser

    Scenario Outline: Login with invalid credentials
        And Provide the username "<username>" and password "<password>"
        And Click on the Login button
        Then Login is failed and invalid credentials error is displayed
        Then Close the browser
        Examples:
            | username | password |
            | abcd     | 1234     |
            | 34567    | 34567    |

    Scenario: Login with empty username
        And Provide the password "admin123"
        And Click on the Login button
        Then Login is failed and empty username error is displayed
        Then Close the browser

    Scenario: Login with empty password
        And Provide the username "Admin"
        And Click on the Login button
        Then Login is failed and empty password error is displayed
        Then Close the browser