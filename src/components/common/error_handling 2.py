"""Error handling system for NAMMI components."""

import logging
from enum import Enum
from typing import Any, Dict, Optional

class ErrorSeverity(Enum):
    """Severity levels for errors."""
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

class NAMMIError(Exception):
    """Base exception for all NAMMI errors."""
    def __init__(self, message: str, severity: ErrorSeverity = ErrorSeverity.ERROR):
        self.message = message
        self.severity = severity
        super().__init__(self.message)

class VoiceoverError(NAMMIError):
    """Raised when there's an issue with voiceover generation."""
    pass

class AnimationError(NAMMIError):
    """Raised when there's an issue with animations."""
    pass

class ValidationError(NAMMIError):
    """Raised when input validation fails."""
    pass

class ScrollError(NAMMIError):
    """Raised when there's an issue with text scrolling."""
    pass

class ErrorReporter:
    """Handles error reporting and logging."""
    
    def __init__(self, log_file: str = 'nammi.log'):
        self.logger = logging.getLogger('nammi')
        self.setup_logging(log_file)
        
    def setup_logging(self, log_file: str):
        """Configure logging settings."""
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
    def report_error(self, error: Exception, context: Optional[Dict[str, Any]] = None):
        """Report an error with context."""
        error_context = context or {}
        error_context['error_type'] = type(error).__name__
        
        if isinstance(error, NAMMIError):
            self.logger.error(
                f"NAMMI Error: {str(error)}",
                extra={'context': error_context}
            )
        else:
            self.logger.error(
                f"Unexpected Error: {str(error)}",
                extra={'context': error_context}
            )

class MathValidator:
    """Validates mathematical inputs and expressions."""
    
    @staticmethod
    def validate_equation(equation: str) -> bool:
        """Validates mathematical equation format."""
        if not equation:
            raise ValidationError("Equation cannot be empty")
        if not isinstance(equation, str):
            raise ValidationError("Equation must be a string")
        # Add more validation rules as needed
        return True
    
    @staticmethod
    def validate_coordinates(x: float, y: float) -> bool:
        """Validates coordinate values."""
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValidationError("Coordinates must be numbers")
        if x < -10 or x > 10 or y < -10 or y > 10:
            raise ValidationError("Coordinates out of valid range")
        return True
    
    @staticmethod
    def validate_slope(rise: float, run: float) -> bool:
        """Validates slope values."""
        if not isinstance(rise, (int, float)) or not isinstance(run, (int, float)):
            raise ValidationError("Slope values must be numbers")
        if run == 0:
            raise ValidationError("Run cannot be zero (undefined slope)")
        return True

class ErrorRecovery:
    """Handles error recovery and fallback mechanisms."""
    
    def __init__(self, error_reporter: ErrorReporter):
        self.error_reporter = error_reporter
    
    def handle_voiceover_error(self, text: str) -> str:
        """Handle voiceover errors by falling back to text display."""
        self.error_reporter.report_error(
            VoiceoverError("Voiceover generation failed"),
            {'text': text}
        )
        return f"Text Display: {text}"
    
    def handle_scroll_error(self, scene: Any) -> None:
        """Handle scroll errors by resetting scroll position."""
        self.error_reporter.report_error(
            ScrollError("Scroll operation failed"),
            {'scene': type(scene).__name__}
        )
        # Reset scroll position logic here
    
    def handle_animation_error(self, animation: Any) -> None:
        """Handle animation errors by providing a fallback animation."""
        self.error_reporter.report_error(
            AnimationError("Animation failed"),
            {'animation': type(animation).__name__}
        )
        # Fallback animation logic here 