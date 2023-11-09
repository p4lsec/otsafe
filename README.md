# [![OTsafe Logo](./images/otsafe.png) OTsafe: Securing Critical Processes](https://otsafe.org)

![Black wide smol](https://github.com/p4lsec/otsafe/assets/34799788/969cd683-09a0-4bd0-8e4f-9b52a279683b)

OTsafe is a Python-based framework designed to enhance the visibility and security of safety-critical functions in operational technology (OT) environments. It offers capabilities to model, detect, and assist in responding to cyber-physical threats, whether they arise from intentional actions or accidents.

A primary aim of OTsafe is to prevent "control loop compromises" - instances where components of a control loop within a system are influenced beyond safe operating parameters, either accidentally or maliciously. By abstracting the complexities of industrial processes, OTsafe empowers teams to model their control systems, enabling a concentrated focus on building systems that are both safe and secure.

One of OTsafe's core strengths is its ability to model real-world systems and apply various data sources to bring these models to life. Through the ingestion of resources like PCAPs, asset inventory databases, and more, it provides a real-time cross-sectional view of various data sources, detecting unsafe, suspicious, or anomalous conditions, regardless of their cause or intent. A key objective is to address the gaps in monitoring and detecting unsafe conditions, particularly at Purdue Levels 0-2.

The abstraction layer of OTsafe ensures that users can account for the unique, implementation-specific details of their control networks. This allows for a more in-depth focus on the functions and interactions of system components. Consequently, users can develop detections and automation strategies centered on aspects such as unsafe conditions, attacker TTPs, and beyond.

## Use Cases

OTsafe can be applied across a variety of scenarios for bolstering the safety measures of physical processes, and ensuring that people, equipment, and environments are protected. Here are a few use cases:

- **Highly secured OT Environments**: OTsafe is ideal for organizations that operate in highly secure environments, such as critical infrastructure, where any deviation from normal operating parameters could have significant implications. OTsafe's comprehensive monitoring and control measures can help understand the safety implications of a control network.  OTsafe's ultimate goal is to detect and respond to anomalies before they cause damage.

- **Insider Threats**:  The impact of an insider threat in a control environment has already proven to be catastrophic (see [this article about a disgruntled water employee here](hhttps://www.waterisac.org/portal/updated-october-21-2021-insider-threat-–-former-employee-indicted-unauthorized-computer)).  OTsafe can provide protection against insider threats by operating as a tamper-proof layer of visibility and control.

- **Accident Investigators**: Teams that are investigating industrial accidents and near-misses can use OTsafe to model the control system, allowing them to quickly and clearly see what went wrong, and when.

- **Safety Prioritization**: Organizations that prioritize safety and want an additional layer of controls can benefit from OTsafe. It offers a comprehensive set of tools to monitor and manage equipment, ensuring safe operation and compliance with safety standards.

- **Risk Assessment and Mitigation**: Engineers conducting Failure Mode and Effects Analysis (FMEA) can leverage OTsafe to incorporate cyber risk scenarios into their assessments. By simulating potential threats and analyzing their impacts, teams can build more robust mitigation strategies.

- **Integrated Operations Centers**: For organizations that seek to ensure the safety of people, equipment, and the environment, OTsafe could serve as a technical hub for various remediation efforts. It helps connect and correlate data from disparate sources, enabling more comprehensive monitoring and response.

- **Compliance Teams**: CISOs and internal compliance teams aiming to demonstrate compliance with, and even applying an auditable layer of controls can benefit from OTsafe. It facilitates clear documentation of safety measures, providing a trail for internal and external audits.

- **Health, Safety, and Environmental (HSE) Staff**: HSE teams can use OTsafe as a crucial tool in their Process Safety Management (PSM) programs. By standardizing and indexing required data such as safe operating parameters, OTsafe can operationalize this intelligence. Furthermore, OTsafe's modeling and simulation capabilities can aid HSE staff in predicting and preventing potential safety incidents, further strengthening the organization's commitment to a proactive safety culture.

- **Data Integration**: For those working on connecting disparate data sources and capabilities, like historians, inventory management systems, detection engines, and playbooks, OTsafe provides a common platform to integrate these sources and create comprehensive views of processes.

- **Safety Engineering**: Team responsible for the safety engineering of systems can use OTsafe to assist in building safe, reliable procedures and environments.  This includes FMEA, FTA, and HAZOP analysis.  These realms are not typically/fully inclusive of cybersecurity-related incidents or mitigations. 

- **Community Development**: Those interested in making a positive impact on safety practices in the industry can use OTsafe as a springboard for their ideas. With its open-source nature, OTsafe encourages contributions and collaborations.
Please note that OTsafe may not be suitable for small teams with limited resources, or in scenarios where a comprehensive safety-oriented solution is not necessary.

## Components

The three main elements of OTsafe include:

- A [core library](#core-library) that establishes common syntax for any industrial component
- An extensible detection framework which allows teams to test and apply custom detections and responses. (Contact me if you want to collaborate on this! Need more hardware testing)
- Implementation automation hub, centered around Jenkins. This helps you build, test, and deploy your specific implementation. 

## Core Library

The core library of OTsafe is a Python API, enabling users to model pertinent components of a cyber-physical process. It allows real-time sensor readings, emulates noisy sensors, and offers a wide array of features for realistically representing industrial components. 

## Detections

OTsafe enables the building of detections for unsafe conditions. Detections can be built in pure Python or can be codified in YAML files (everything-as-code FTW!). 

Detections can be tested against historic data (via PCAPs), or via live process telemetry and data via a local network interface.  As always, be smart about what you connect to your control network.  Use of a data diode or span port is highly recommended.  

## Automation capabilities

OTsafe utilizes Jenkins for orchestration, allowing for easy deployment, scalability, and serving as an automation platform. It enables system-wide defensive measures in the event of a disruption.

## Install

This package will not be published on PyPI. To install the core library using pip, you can run the following command:

```
python3 -m pip install https://github.com/p4lsec/otsafe.git@main
```

To install and use from source:

```
git clone git@github.com:p4lsec/otsafe.git
cd otsafe
python3 -m venv ot-venv
source ot-venv/bin/activate
python3 -m pip install -e .
```

To install the full tooling (Jenkins, nginx, Postgres, Redis, etc):

```
git clone git@github.com:p4lsec/otsafe.git
cd otsafe
python3 -m venv ot-venv
source ot-venv/bin/activate
python3 -m pip install -e .
vim docker-compose.yml # update this file with your postgres values
docker-compose up
```

## Using OTsafe

For a comprehensive demo, please see [this Jupyter notebook](otsafe/demo/demo.ipynb) for an interactive demo and guide. 

## Roadmap

As OTsafe continues to grow and evolve, our roadmap includes several exciting updates and features. Please find below some of the enhancements we are looking to incorporate:

- **Mapping to IEC 62443**: One of our primary roadmap items is to map the features and capabilities of OTsafe to IEC 62443, an international series of standards on "Industrial communication networks - Network and system security." The goal is to provide clear guidance on how OTsafe can assist in achieving compliance with these widely-recognized standards, thereby boosting the credibility of your cybersecurity initiatives and assuring stakeholders of the robustness of your defenses.

- **Integration with Additional Data Sources**: We plan to expand OTsafe's ability to integrate with additional data sources, enabling you to gain a more comprehensive understanding of your industrial processes and systems. This will improve anomaly detection capabilities and provide a more complete picture of your system's status.

- **Improved User Interface**: We're continuously working on enhancing the user experience and making the system more intuitive and user-friendly. This includes improvements to the dashboard, notifications system, and process modeling capabilities.

- **Advanced Detection Capabilities**: We aim to enhance OTsafe's detection engine by incorporating more sophisticated algorithms and machine learning techniques. This will allow us to better identify patterns and detect anomalies, thereby enhancing the system's ability to prevent accidents and security incidents.

- **Customization Features**: We understand that every industrial system is unique, and our aim is to allow users to customize OTsafe to best fit their needs. This includes the ability to define custom thresholds, alerts, and responses. Plans are in place to introduce default dashboards. 

- **Further Automation Capabilities**: We're planning on expanding OTsafe's automation capabilities to include more scenarios and response actions, with the aim to increase operational efficiency and speed up incident response times. Jenkins is optionally available as the project hub. Examples showing how to automate detection engineering testing/deployment via CI/CD pipelines will be included. This is a capability your SOC should seek to have! 

## Community

ICS security has been an industry that continually stands on the shoulders of giants. We encourage feedback and contributions from you! Your input is vital in shaping the future of OTsafe. If you would like to get more involved in writing code, testing the application and capabilites of this code, etc, please reach out. 

## Disclaimers

- This project should be considered a research and development project, and should not be relied upon to provide immediate life-saving reliability. This is not built or designed to be used in a safety-critical situation.  OTsafe is intended as an additional layer of protection, supplementing existing and adequate Safety Instrumented Systems (SIS).

- Python was chosen as the primary language due to its wide ecosystem and ease of use. While not the best language in many cases, Python's wide adoption, versatility, and the anticipated performance improvements via its evolving ecosystem made it suitable for this research project. 
