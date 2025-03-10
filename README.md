# Nammi Math Tutorials

An interactive math tutorial system built with Manim, featuring:
- Beautiful animations
- Clear explanations with voiceovers
- Step-by-step problem solving
- Interactive components

## Setup

1. Clone the repository:
```bash
git clone [your-repository-url]
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

## Running Tutorials

To run a tutorial, use the following command format:
```bash
cd src/topics/[subject]/scenes
manim -pqh [tutorial_file].py [SceneName]
```

For example, to run the linear equations tutorial:
```bash
cd src/topics/algebra/scenes
manim -pqh linear_equations_find_equation.py LinearEquationsFindEquation
```

## Project Structure

```
nammi/
├── src/
│   ├── components/
│   │   ├── common/          # Shared components and utilities
│   │   └── styles/          # Common styles and constants
│   └── topics/
│       ├── algebra/         # Algebra tutorials
│       └── [other_subjects] # Other math subjects
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request

## License

[Your chosen license] 