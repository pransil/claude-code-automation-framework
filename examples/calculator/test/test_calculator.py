"""
Consolidated Calculator Tests
Essential tests for calculator functionality.
"""

import pytest
from src.calculator_engine import CalculatorEngine
from src.calculator_app import CalculatorApp


class TestCalculatorEngine:
    """Test calculator engine functionality."""
    
    def setup_method(self):
        """Setup test fixtures."""
        self.engine = CalculatorEngine()
    
    def test_basic_arithmetic(self):
        """Test basic arithmetic operations."""
        assert self.engine.evaluate_expression("2 + 3") == "5"
        assert self.engine.evaluate_expression("10 - 4") == "6" 
        assert self.engine.evaluate_expression("6 * 7") == "42"
        assert self.engine.evaluate_expression("15 / 3") == "5"
    
    def test_decimal_operations(self):
        """Test decimal number operations."""
        assert self.engine.evaluate_expression("2.5 + 1.5") == "4"
        assert self.engine.evaluate_expression("3.14159 * 2") == "6.28318"
        assert self.engine.evaluate_expression("7.5 / 2.5") == "3"
    
    def test_parentheses(self):
        """Test parentheses grouping."""
        assert self.engine.evaluate_expression("(2 + 3) * 4") == "20"
        assert self.engine.evaluate_expression("2 * (3 + 4)") == "14"
        assert self.engine.evaluate_expression("((2 + 3) * 4) / 2") == "10"
    
    def test_operator_precedence(self):
        """Test mathematical operator precedence."""
        assert self.engine.evaluate_expression("2 + 3 * 4") == "14"
        assert self.engine.evaluate_expression("10 - 6 / 2") == "7"
        assert self.engine.evaluate_expression("2 * 3 + 4 * 5") == "26"
    
    def test_negative_numbers(self):
        """Test negative number handling."""
        assert self.engine.evaluate_expression("-5") == "-5"
        assert self.engine.evaluate_expression("-3 + 7") == "4"
        assert self.engine.evaluate_expression("5 + (-3)") == "2"
    
    def test_division_by_zero(self):
        """Test division by zero error handling."""
        assert self.engine.evaluate_expression("5 / 0") == "?"
        assert self.engine.evaluate_expression("0 / 0") == "?"
    
    def test_invalid_expressions(self):
        """Test invalid expression handling."""
        assert self.engine.evaluate_expression("") == "?"
        assert self.engine.evaluate_expression("   ") == "?"
        assert self.engine.evaluate_expression("2 +") == "?"
        assert self.engine.evaluate_expression("* 3") == "?"
        assert self.engine.evaluate_expression("2 ++ 3") == "?"
    
    def test_too_small_numbers(self):
        """Test very small number handling."""
        assert self.engine.evaluate_expression("0.000000001") == "Too Small"
        assert self.engine.evaluate_expression("1 / 1000000000") == "Too Small"
    
    def test_decimal_precision(self):
        """Test decimal precision formatting."""
        result = self.engine.evaluate_expression("1 / 3")
        # Should be formatted with max 8 decimal places
        assert len(result.split('.')[-1]) <= 8 if '.' in result else True
    
    def test_input_validation(self):
        """Test input character validation."""
        assert self.engine.is_valid_input_character('5')
        assert self.engine.is_valid_input_character('+')
        assert self.engine.is_valid_input_character('.')
        assert self.engine.is_valid_input_character('(')
        assert not self.engine.is_valid_input_character('a')
        assert not self.engine.is_valid_input_character('$')
    
    def test_expression_validation(self):
        """Test expression validation."""
        assert self.engine.validate_expression("2 + 3")
        assert self.engine.validate_expression("(2 + 3) * 4")
        assert not self.engine.validate_expression("2 + a")
        assert not self.engine.validate_expression("(2 + 3")  # Unbalanced
        assert not self.engine.validate_expression("")


class TestCalculatorApp:
    """Test calculator application functionality."""
    
    def setup_method(self):
        """Setup test fixtures."""
        from PyQt6.QtWidgets import QApplication
        import sys
        
        # Create QApplication if it doesn't exist
        if not QApplication.instance():
            self.app = QApplication(sys.argv)
        else:
            self.app = QApplication.instance()
            
        self.calculator = CalculatorApp()
    
    def test_history_functionality(self):
        """Test in-memory history management."""
        # Test saving calculations
        self.calculator._save_calculation("2 + 3", "5")
        self.calculator._save_calculation("10 - 4", "6")
        
        assert len(self.calculator.history_items) == 2
        assert self.calculator.history_items[0]['expression'] == "10 - 4"  # Most recent first
        assert self.calculator.history_items[1]['expression'] == "2 + 3"
    
    def test_history_limit(self):
        """Test history item limit (10 items max)."""
        # Add more than 10 items
        for i in range(15):
            self.calculator._save_calculation(f"{i} + 1", str(i + 1))
        
        # Should only keep 10 most recent
        assert len(self.calculator.history_items) == 10
        assert self.calculator.history_items[0]['expression'] == "14 + 1"  # Most recent
        assert self.calculator.history_items[9]['expression'] == "5 + 1"   # 10th most recent