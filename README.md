# NAMMI - Math Tutorial Generator

NAMMI is a powerful tool for creating engaging math tutorials using Manim animations and Azure voiceover.

## Features

- Create beautiful math animations using Manim
- Generate natural-sounding voiceovers using Azure
- Smart colorization of mathematical expressions
- Scrollable text management
- Error handling and recovery
- Modular component system

## Installation

1. Clone the repository:
```bash
git clone https://github.com/johnyanni/nammi.git
cd nammi
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up Azure credentials:
- Create an Azure account
- Set up a Speech Service
- Add your Azure credentials to `.env`

## Project Structure

```
nammi/
├── src/
│   ├── components/
│   │   ├── common/         # Shared components
│   │   └── styles/         # Styling constants
│   └── topics/             # Math topics
│       └── linear_equations/
│           └── scenes/     # Tutorial scenes
├── tests/                  # Test files
├── docs/                   # Documentation
└── examples/              # Example tutorials
```

## Usage

1. Create a new tutorial scene:
```python
from src.components.common.base_scene import MathTutorialScene

class MyTutorial(MathTutorialScene):
    def construct(self):
        # Your tutorial code here
        pass
```

2. Run the tutorial:
```bash
manim -pql src/topics/your_topic/scenes/your_scene.py MyTutorial
```

## Development

1. Set up development environment:
```bash
pip install -r requirements-dev.txt
```

2. Run tests:
```bash
pytest
```

3. Run linting:
```bash
ruff check .
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Manim](https://github.com/ManimCommunity/manim) for animation capabilities
- [Azure Speech Services](https://azure.microsoft.com/en-us/services/cognitive-services/speech-services/) for voiceover
- All contributors and maintainers 