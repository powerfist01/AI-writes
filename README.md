# AI Writes

AI Writes is a project that leverages Google's Gemini Pro Model to generate creative content such as stories, poems, limericks, jokes, and more. Users can receive personalized content by entering their email and clicking the "Send Me" button.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- Generate creative content using Google's Gemini Pro Model.
- User-friendly interface for entering email and receiving personalized content.

## Technologies Used

- Python Flask
- WTF (WTForms)
- Celery
- Google's Gemini Pro Model
- Flower (Celery monitoring tool)
- Docker
- Docker Compose
- CI/CD with GitHub Actions

## Installation

1. Clone the repository:

```bash
git clone https://github.com/powerfist01/AI-writes.git
cd AI-writes
```

2. Start the application:

```bash
docker-compose up --build -d
```

3. Open the application in your browser:

```bash
http://localhost:5000
```

## Usage

1. Enter your email and click the "Send Me" button.
2. Check your email for your personalized content.

## Contributing

Contributions are always welcome!


## License

[Apace License 2.0](http://www.apache.org/licenses/LICENSE-2.0.txt)

## Contact

- GitHub [@powerfist01]