# I need to clean this up because it starts the same way as a different test
Feature: Submitting a form
  Scenario: User can send the contact me form
    Given I am on the homepage checking the form
    When I click the "Learn More" button
    And I enter "John" in the "firstname" field
    And I enter "Doe" in the "lastname" field
    And I enter "123-456-7890" in the "phone" field
    And I enter "thisisatest32894523@gmail.com" in the "workEmail" field
    And I enter "Test Company" in the "companyName" field
    And I press the "Get Started" button
    Then I see "Thank you for reaching out to us. A representative will contact you shortly"
