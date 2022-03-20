Feature: Checking whether the navigation works correctly
  Scenario: I can see The Let's Connect popup
    Given I am on the homepage
    When I click the "Learn More" button
    Then I can see the "Let's Connect" popup
