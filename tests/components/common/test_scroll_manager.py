"""Tests for the scroll manager component."""

import pytest
from manim import *
from src.components.common.scroll_manager import ScrollManager

class TestScrollManager:
    """Test suite for ScrollManager class."""
    
    @pytest.fixture
    def equations(self):
        """Create test equations."""
        return [
            MathTex("y = mx + b"),
            MathTex("y = 2x + 3"),
            MathTex("y = -x + 5")
        ]
    
    @pytest.fixture
    def scroll_manager(self, equations):
        """Create a test scroll manager instance."""
        return ScrollManager(equations)
    
    def test_initialization(self, scroll_manager, equations):
        """Test that scroll manager initializes correctly."""
        assert isinstance(scroll_manager, ScrollManager)
        assert scroll_manager.equations == equations
        assert scroll_manager.current_position == 0
        assert scroll_manager.last_in_view == 0
    
    def test_prepare_next(self, scroll_manager):
        """Test preparing next equation."""
        scroll_manager.prepare_next()
        assert scroll_manager.current_position == 1
    
    def test_scroll_down(self, scroll_manager):
        """Test scrolling down."""
        scroll_manager.prepare_next()
        scroll_manager.scroll_down(None)
        assert scroll_manager.last_in_view == 1 