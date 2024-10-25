# Movehouse.ai

Movehouse.ai is a multi-agent system powered by CAMEL AI, designed to simplify and automate the process of finding and booking houses when relocating. The system uses a team of collaborative AI agents to gather, assess, and select properties that fit a user's specific requirements, streamlining the house-hunting process end-to-end.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
- [Agents](#agents)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Movehouse.ai was created to tackle the complexities of moving to a new location. By leveraging the CAMEL AI framework, Movehouse.ai enables AI agents to autonomously collaborate, filter, and shortlist housing options based on user-specified criteria, providing a seamless relocation experience.

## Features
- Automated property discovery through web scraping
- Customisable filters for location, budget, property size, and amenities
- Agent-based collaboration for parallel task execution
- Decision-making capabilities to suggest top options based on user preferences
- Automated booking integration with partner platforms

## System Architecture

The core of Movehouse.ai relies on a multi-agent system, built with CAMEL AI, that allows independent agents to communicate and collaborate, completing tasks in a structured workflow.

- **User Input Parsing** – interprets user’s needs and defines criteria
- **Property Discovery Agent** – uses Firecrawl for web scraping across various platforms
- **Filtering Agent** – applies user-defined criteria to narrow down results
- **Evaluation Agent** – prioritises properties based on scoring metrics
- **Booking Agent** – initiates booking actions for selected properties

## Getting Started

To get Movehouse.ai running locally, follow these instructions.

### Prerequisites
- Python 3.9 or higher
- CAMEL AI framework
- Firecrawl web scraping tool

### Installation

Clone the repository:
```bash
git clone https://github.com/your-username/movehouse.ai.git
cd movehouse.ai
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### Configuration

Set up CAMEL AI tokens in `.env`:
```makefile
CAMEL_API_KEY=your_api_key_here
```

Configure Firecrawl in `config.yaml`:
```yaml
firecrawl:
  user_agent: "your_user_agent_here"
  base_url: "https://firecrawl.io"
```

Update user preferences in `user_config.json`:
```json
{
  "location": "London",
  "budget": 1500,
  "property_type": "flat",
  "move_in_date": "2024-11-01"
}
```

### Usage

Run the main script:
```bash
python main.py
```

Specify preferences when prompted, or edit `user_config.json` to customise your search criteria.

The system will return a shortlist of properties that match the specified requirements.

## Agents

Movehouse.ai uses specialised agents to perform distinct tasks in the system, each focused on a particular function:

- **Input Parser Agent** – reads and interprets user input
- **Discovery Agent** – gathers housing data from online sources
- **Filter Agent** – removes properties that don’t meet minimum criteria
- **Evaluation Agent** – ranks properties based on user preference
- **Booking Agent** – executes bookings and sends notifications

## Contributing

We welcome contributions! Please fork this repository, create a new branch, and submit a pull request for any changes.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
