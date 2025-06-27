# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **Claude Code Automation Framework** - a systematic development framework that guides Claude through building applications across multiple domains (web apps, APIs, CLI tools, ML systems, trading dashboards, desktop apps).

## Essential Commands

### Project Creation
```bash
python framework/tools/project_wizard.py
```
Interactive wizard for creating new projects with appropriate templates and tech stacks.

### Testing
```bash
# From calculator example
python test/run_tests.py
```
Generates timestamped test reports in `test/reports/test_results_YYYY-MM-DD-HH:MM.txt`.

### Development Setup (varies by tech stack)
```bash
# Python CLI Tools
python -m venv venv
source venv/bin/activate  # Unix/Mac
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
pip install -e .

# Web Apps  
npx create-react-app frontend --template typescript
python -m venv backend/venv
```

## Framework Architecture

### Core Development Workflow
The framework follows a **6-phase systematic approach**:

1. **Project Initialization**: Use project wizard to select application type and tech stack
2. **Requirements Definition**: Generate comprehensive PRD from domain-specific templates
3. **Development Planning**: Break down into TodoWrite tasks with clear deliverables
4. **Implementation**: Code with built-in quality standards and patterns
5. **Testing**: Multi-level testing with timestamped reports (>80% coverage required)
6. **Documentation**: Generate user and developer guides

### Directory Structure Pattern
All projects follow this structure:
```
{project_name}/
├── deliverables/           # All project outputs
│   ├── PRD.md             # Project Requirements Document  
│   ├── src/               # Source code
│   ├── test/              # Test code and reports
│   ├── docs/              # Documentation
│   └── requirements.txt   # Dependencies
```

### Key Components

**Templates System** (`templates/application_types/`):
- Domain-specific PRD templates with placeholder variables
- Structured requirements format with user stories and functional requirements
- Non-goals section to prevent scope creep

**Tech Stack Profiles** (`tech_stacks/`):
- YAML-defined technology combinations with dependencies
- Setup instructions and best practices
- Testing strategies and deployment guidance

**Project Wizard** (`tools/project_wizard.py`):
- Interactive project creation with tech stack selection
- Directory structure generation and PRD template instantiation

## Supported Application Types

| Type | Template File | Key Tech Stacks | Testing Strategy |
|------|---------------|-----------------|------------------|
| **Web Apps** | `web_app_prd_template.md` | React+Python, Vue+Node | Jest, pytest |
| **REST APIs** | `api_service_prd_template.md` | FastAPI, Express | pytest, supertest |
| **CLI Tools** | `cli_tool_prd_template.md` | Python Click | pytest + click.testing |
| **ML Systems** | `ml_system_prd_template.md` | scikit-learn, TensorFlow | pytest + model validation |
| **Trading Dashboards** | `trading_dashboard_prd_template.md` | Streamlit, React+D3 | pytest + financial calculations |
| **Desktop Apps** | Example: calculator | PyQt6, Electron | pytest + GUI testing |

## Development Standards

### TodoWrite Integration
- **ALWAYS** use TodoWrite for task planning and progress tracking
- Break complex features into specific, actionable items
- Mark tasks as in_progress/completed in real-time
- One task in_progress at a time

### Quality Gates
- **PRD Completeness**: All requirements from template must be addressed
- **Test Coverage**: >80% coverage required with timestamped reports
- **Error Handling**: Comprehensive validation and user-friendly error messages
- **Documentation**: Both user guides and developer documentation required

### Architecture Patterns
- **Template-Driven Development**: Use existing templates rather than starting from scratch
- **Domain-Specific Guidance**: Different application types have different requirements
- **Quality by Design**: Built-in standards prevent common mistakes
- **Systematic over Ad-hoc**: Follow the 6-phase workflow to eliminate decision paralysis

## Technology Stack Profiles

### Python CLI Tools (`python_cli_tool.yaml`)
- **Framework**: Click with rich for beautiful terminal output
- **Testing**: pytest + click.testing.CliRunner + pytest-cov
- **Distribution**: setuptools → PyPI
- **Features**: Progress bars, configuration files, multiple output formats

### FastAPI Microservices (`fastapi_microservice.yaml`)
- **Stack**: FastAPI + SQLAlchemy + PostgreSQL + Redis
- **Testing**: pytest + httpx for API testing
- **Features**: OpenAPI docs, rate limiting, authentication
- **Deployment**: Docker + container orchestration

### React+Python Web Apps (`web_fullstack_react_python.yaml`)
- **Frontend**: React + TypeScript + modern build tools
- **Backend**: FastAPI or Django with database integration
- **Testing**: Jest (frontend) + pytest (backend)
- **Features**: Responsive design, SEO optimization, performance monitoring

## Working Example

The **calculator example** (`examples/calculator/`) demonstrates complete implementation:
- Desktop application using PyQt6
- Comprehensive test suite with timestamped reports
- Professional documentation and user guides
- All quality gates implemented

## Framework Benefits

- **40% faster development** compared to ad-hoc approaches
- **Production-ready code** with proper architecture from start
- **Consistent quality** across different project types
- **Template-driven approach** eliminates common setup mistakes
- **Built-in task management** with TodoWrite integration

## Important Notes

- **Always follow the 6-phase workflow** - don't skip phases
- **Use templates** - don't create requirements from scratch
- **Leverage tech stack profiles** - they contain proven configurations
- **Maintain timestamped test reports** - use the provided test runners
- **Focus on quality gates** - each phase has specific deliverables required