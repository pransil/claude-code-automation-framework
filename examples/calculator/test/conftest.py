"""
Test configuration and fixtures.
"""

import sys
from pathlib import Path

# Add src directory to Python path for imports
test_dir = Path(__file__).parent
src_dir = test_dir.parent / 'src'
sys.path.insert(0, str(src_dir))