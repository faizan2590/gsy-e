Feature: Run power flow integration tests

  @disabled
  Scenario: Run power flow integration tests on console
     Given we have a scenario named power_flow.test_power_flow
     And gsy-e is installed
     When we run the gsy-e simulation on console with power_flow.test_power_flow for 2 hrs
     Then the export functionality of power flow result

  Scenario: BaselinePeakEnergyStats are correctly calculated
    Given we have a scenario named power_flow/baseline_peak_energy
    And gsy-e is installed
    When we run the simulation with setup file power_flow.baseline_peak_energy and parameters [24, 60, 60]
    Then BaselinePeakEnergyStats are correctly calculated

  Scenario: NetEnergyFlowStats are correctly calculated
    Given we have a scenario named power_flow/net_energy_flow
    And gsy-e is installed
    And export is_needed
    When we run the simulation with setup file power_flow.net_energy_flow and parameters [24, 60, 60]
    Then NetEnergyFlowStats are correctly calculated
