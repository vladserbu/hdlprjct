Feature: Test user can login on Hudl
  Scenario: test_user_can_successfully_login
    Given user is on the login page
    When user is successfully logged in as "vlad.serbu@icloud.com"
    Then user is redirected to the profile dashboard

    Scenario: test_user_cannot_login_without_email_password
    Given user is on the login page
    When user signs in without email and password
    Then an error message "We didn't recognize that email and/or password. Need help?" will be displayed

  Scenario Outline: test_user_cannot_login_with_invalid_or_missing_parameters
    Given user is on the login page
    When user signs in with "<email>" and "<password>"
    Then an error message "We didn't recognize that email and/or password. Need help?" will be displayed

    Examples: emails and messages
    | case | email | password |
    | Invalid email | invalidemail.com | pass |
    | Invalid password | vlad.serbu@icloud.com | 123456789 |