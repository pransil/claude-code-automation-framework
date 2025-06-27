"""
Calculator Engine
Simple and safe calculation logic using sanitized eval.
"""

import re
from typing import Union


class CalculatorEngine:
    """Simple calculator engine with safe expression evaluation."""
    
    def __init__(self):
        """Initialize calculator engine."""
        self.max_decimal_places = 8
        self.min_representable = 1e-8
    
    def is_valid_input_character(self, char: str) -> bool:
        """Check if character is allowed in calculator input."""
        return char in '0123456789+-*/.() '
    
    def validate_expression(self, expression: str) -> bool:
        """Validate if expression contains only allowed characters and is balanced."""
        if not expression or not expression.strip():
            return False
            
        # Check for allowed characters only
        if not all(self.is_valid_input_character(char) for char in expression):
            return False
        
        # Check for balanced parentheses
        return expression.count('(') == expression.count(')')
    
    def evaluate_expression(self, expression: str) -> Union[float, str]:
        """Safely evaluate mathematical expression."""
        if not expression or not expression.strip():
            return "?"
        
        clean_expr = expression.strip()
        
        if not self.validate_expression(clean_expr):
            return "?"
        
        try:
            # Sanitize expression - only allow safe mathematical operations
            clean_expr = self._sanitize_expression(clean_expr)
            
            # Evaluate safely
            result = eval(clean_expr, {"__builtins__": {}}, {})
            
            # Handle special cases
            if isinstance(result, (int, float)):
                if abs(result) < self.min_representable and result != 0:
                    return "Too Small"
                
                # Format result
                if isinstance(result, float):
                    formatted = f"{result:.{self.max_decimal_places}f}".rstrip('0').rstrip('.')
                    if '.' not in formatted and abs(result) < 1e15:
                        return str(int(result))
                    return formatted
                else:
                    return str(result)
            
            return str(result)
            
        except (SyntaxError, ValueError, TypeError, ZeroDivisionError, OverflowError):
            return "?"
        except Exception:
            return "?"
    
    def _sanitize_expression(self, expression: str) -> str:
        """Sanitize expression to prevent code injection while allowing math."""
        # Remove spaces
        clean = re.sub(r'\s+', '', expression)
        
        # Check for invalid sequences
        if re.search(r'[+*/]{2,}', clean) or re.search(r'[-]{3,}', clean):
            raise ValueError("Invalid operator sequence")
        
        # Replace display operators with Python operators
        clean = clean.replace('×', '*').replace('÷', '/')
        
        # Handle implicit multiplication (e.g., 2(3) -> 2*(3))
        clean = re.sub(r'(\d)\(', r'\1*(', clean)
        clean = re.sub(r'\)(\d)', r')*\1', clean)
        clean = re.sub(r'\)\(', r')*(', clean)
        
        return clean
    
    def format_number_input(self, current_input: str, new_char: str) -> str:
        """Handle number input formatting including decimal points."""
        if new_char == '.':
            # Find the current number being typed
            operators = '+-*/()' 
            last_operator_pos = -1
            
            for i in range(len(current_input) - 1, -1, -1):
                if current_input[i] in operators:
                    last_operator_pos = i
                    break
            
            current_number = current_input[last_operator_pos + 1:]
            if '.' in current_number:
                return current_input  # Don't add another decimal point
            
            # Add leading zero if decimal point is first character
            if not current_number or current_number[-1] in operators:
                return current_input + '0.'
        
        return current_input + new_char