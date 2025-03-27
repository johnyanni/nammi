"""Tests for the base scene component."""

import pytest
from manim import *
from src.components.common.base_scene import MathTutorialScene

class TestMathTutorialScene:
    """Test suite for MathTutorialScene class."""
    
    @pytest.fixture
    def scene(self):
        """Create a test scene instance."""
        return MathTutorialScene()
    
    def test_scene_initialization(self, scene):
        """Test that scene initializes correctly."""
        assert isinstance(scene, MathTutorialScene)
        assert hasattr(scene, 'error_reporter')
        assert hasattr(scene, 'error_recovery')
        assert hasattr(scene, 'validator')
    
    def test_background_color(self, scene):
        """Test that background color is set correctly."""
        scene.setup()
        assert scene.camera.background_color == ManimColor("#121212")
    
    def test_voiceover_setup(self, scene):
        """Test that voiceover service is configured."""
        scene.setup()
        assert hasattr(scene, 'speech_service')
        assert scene.speech_service is not None 