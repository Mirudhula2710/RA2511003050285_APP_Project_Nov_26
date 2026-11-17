# WATER -- THE ELIXIR OF LIFE

A campus water-leakage detection and monitoring system designed to
monitor water-flow data across four campus zones: **Hostels,
Laboratories, Administration, and Canteen**.

> **Project scope:** The current implementation uses simulated
> sensor/flow data. Physical IoT sensors and automatic valves have not
> been deployed. Valve shutoff is demonstrated as a simulated response.

**Course:** 21CSC203P -- Advanced Programming Practices  
**Team Leader:** Mirudhula B (RA2511003050285)  
**Section / Academic Year:** II CSE E / 2026--2027  
**Mentor:** Dr. S. Shargunam, Assistant Professor

## 1. Project Overview

Water leakage can lead to significant water wastage when it is not
detected quickly. This project provides a software-based monitoring
system that analyses water-flow readings, identifies unusual flow
behaviour, generates alerts, and supports maintenance follow-up.

The system combines flow-physics calculations based on **Torricelli's
Law** with machine-learning-based detection. It provides monitoring
interfaces, stores relevant data, and can send notifications through
Telegram.

## 2. Objectives

-   Monitor water-flow readings across four campus zones.
-   Identify possible leakage or abnormal flow conditions.
-   Apply physics-based calculations and machine-learning detection.
-   Store readings, alerts, users, complaints, and maintenance-related
    information.
-   Present monitoring information through dashboard interfaces.
-   Support timely maintenance through alerts and ticket generation.

## 3. Main Features

-   Four-zone water-flow monitoring.
-   Simulated sensor data generation.
-   Flow analysis based on Torricelli's Law.
-   Machine-learning-based anomaly/leak detection.
-   Alert generation for abnormal readings.
-   Maintenance ticket and complaint management.
-   Dashboard-based monitoring.
-   AI-assisted explanations using the Google Gemini API.
-   Telegram notifications.
-   Simulated critical-response/valve-shutoff behaviour.

## 4. Zones Covered

1.  Hostels
2.  Laboratories
3.  Administration
4.  Canteen

## 5. Technology Stack

  -----------------------------------------------------------------------
  Category                            Technologies
  ----------------------------------- -----------------------------------
  Programming languages               Python, Java 17, TypeScript

  Development tool                    Visual Studio Code

  Front end                           Angular 18; Tkinter desktop
                                      interface (where included in the
                                      implemented build)

  Backend frameworks                  Flask, Spring Boot 3

  Databases                           MySQL 8.0, SQLite

  Database connectivity               MySQL Connector/Python, Spring Data
                                      JPA

  Libraries and APIs                  SymPy, Google Gemini API, Telegram
                                      Bot API

  Machine learning                    Logistic Regression, SVC (RBF),
                                      Random Forest, MLP, Decision Tree

  Version control                     Git and GitHub
  -----------------------------------------------------------------------

## 6. System Architecture

The project is organised into four broad layers:

1.  **Flow simulation and physics layer** -- generates simulated flow
    readings and applies flow calculations based on Torricelli's Law.
2.  **Processing and detection layer** -- uses Python processing, SymPy,
    and machine-learning models to analyse readings and identify
    abnormal behaviour.
3.  **Data and notification layer** -- stores project data in MySQL and
    authentication-related data in SQLite; integrates Gemini
    explanations and Telegram notifications.
4.  **Application layer** -- provides user-facing dashboards and APIs
    through Angular, Flask, and Spring Boot.

## 7. Machine Learning

The project evaluates the following models:

  Model                   Reported accuracy
  --------------------- -------------------
  Logistic Regression               100.00%
  SVC (RBF)                          99.88%
  Random Forest                      99.75%
  MLP                                99.12%
  Decision Tree                      99.00%

**SVC (RBF)** is selected as the production model in the project, even
though Logistic Regression has the highest reported accuracy in the
evaluation.

Additional reported SVC metrics: - Macro F1-score: **0.9974** -
Five-fold stratified cross-validation mean macro-F1: **0.9990**

These are evaluation results from the project report and should not be
interpreted as a guarantee of performance on live campus sensor data.

## 8. Reported Performance and Testing

The project report records the following measurements:

  Measurement                            Reported result
  ------------------------------------ -----------------
  Physics calculation time                       2.10 μs
  Machine-learning inference time                6.96 ms
  TCP packet ingestion round-trip              0.9264 ms
  Listed test cases (TC-01 to TC-10)           100% pass
  Spring Boot tests                           6/6 passed
  Python test suites                          2/2 passed

Results may vary depending on the execution environment and test setup.

## 9. Installation and Execution

The exact commands depend on the source-code folder structure and the
configuration files in the submitted project. The following are the
general prerequisites; use the project-specific instructions and
dependency files where available.

### Prerequisites

-   Python
-   Java 17
-   Node.js and npm (for the Angular frontend)
-   MySQL 8.0
-   Visual Studio Code (recommended)
-   Git

### Setup checklist

1.  Clone or download the project repository.
2.  Install the Python dependencies from the project's
    `requirements.txt`, if provided.
3.  Configure the MySQL database and update the database connection
    settings.
4.  Configure any required SQLite database path.
5.  Configure the Java/Spring Boot backend using the project's build
    configuration.
6.  Install Angular dependencies from the frontend directory using
    `npm install`.
7.  Add required API credentials, such as Gemini or Telegram tokens,
    through local environment/configuration settings.
8.  Start each application component using the run instructions provided
    in its respective folder.

**Note:** Do not commit passwords, API keys, bot tokens, or other
secrets to GitHub. Use environment variables or a local configuration
file excluded from version control.

## 10. Configuration

Before running the application, check the project configuration for:

-   MySQL host, port, database name, username, and password.
-   SQLite database location.
-   Gemini API key, if AI explanations are enabled.
-   Telegram bot token and chat ID, if Telegram notifications are
    enabled.
-   Backend and frontend service URLs/ports.

Use placeholder values in shared documentation. Keep actual credentials
private.

## 11. Limitations

-   Sensor readings are simulated; physical sensor deployment is outside
    the current implementation.
-   Automatic valve shutoff is simulated; no physical valve is
    controlled by the current system.
-   Results from simulated data may differ from results in a real campus
    environment.
-   Telegram notifications and Gemini-based features depend on network
    access and valid API credentials.

## 12. Future Enhancements

-   Integrate physical flow sensors using ESP32 or STM32.
-   Add acoustic leak localisation.
-   Deploy edge processing using Raspberry Pi devices.
-   Explore LSTM-based forecasting.
-   Integrate water-quality sensors.
-   Validate the system using real campus water-flow data.

## 13. Course, Team, and Project Details

-   **Project title:** WATER -- THE ELIXIR OF LIFE
-   **Project focus:** Campus water leakage detection and monitoring
-   **Course code:** 21CSC203P
-   **Course name:** Advanced Programming Practices
-   **Project category:** APP
-   **Team leader:** Mirudhula B
-   **Team leader register number:** RA2511003050285
-   **Department:** Computer Science and Engineering
-   **Section:** II CSE E
-   **Academic year:** 2026--2027
-   **Institution:** SRM Institute of Science and Technology, Tiruchirappalli
-   **School:** School of Computing
-   **Faculty:** Faculty of Engineering and Technology

### Team Members

| Role | Name | Register Number |
|---|---|---|
| Team Leader | Mirudhula B | RA2511003050285 |
| Team Member | Janani Ulaganathan | RA2511003050296 |
| Team Member | Sandhiya G | RA2511003050299 |
| Team Member | Keerthana N | RA2511003050300 |

### Project Mentor

-   **Name:** Dr. S. Shargunam
-   **Designation:** Assistant Professor
-   **Department:** Computer Science and Engineering

## 14. References

Refer to the project report for the complete bibliography, research
papers, API documentation, and technical references used during
development.

------------------------------------------------------------------------
