#!/usr/bin/env python3
"""
Calculator Application
Professional calculator with real-time calculation and history.
"""

import sys
from PyQt6.QtWidgets import QApplication
from calculator_app import CalculatorApp


def main():
    """Run the calculator application."""
    # Create application
    app = QApplication(sys.argv)
    app.setApplicationName("Professional Calculator")
    app.setApplicationVersion("1.0")
    
    # Create and show calculator window
    calculator = CalculatorApp()
    calculator.show()
    
    # Run application
    sys.exit(app.exec())


if __name__ == "__main__":
    main()