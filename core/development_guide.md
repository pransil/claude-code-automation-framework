# Claude Code Automation Framework

This framework enables Claude Code to systematically design, build, test, and deploy applications across multiple domains including web apps, APIs, CLI tools, ML systems, and trading dashboards.

## Quick Start
1. **Initialize Project**: Use project wizard to select application type
2. **Create PRD**: Generate requirements document from template
3. **Plan Tasks**: Break down development into manageable steps  
4. **Implement**: Build following framework standards
5. **Test**: Automated testing with timestamped reports
6. **Document**: Generate user and developer documentation

## Supported Application Types

| **Type** | **Examples** | **Tech Stacks** |
|----------|--------------|-----------------|
| **Web Applications** | E-commerce, dashboards, blogs | React/Vue + Node.js/Python/Django |
| **APIs & Services** | REST APIs, microservices | FastAPI, Express, Flask, Spring |
| **CLI Tools** | Utilities, automation scripts | Python Click, Node.js Commander |
| **ML Systems** | Prediction, classification | Python scikit-learn, TensorFlow, PyTorch |
| **Trading Dashboards** | Financial analysis, algorithmic trading | Python Streamlit, React + D3.js |
| **Desktop Applications** | Cross-platform apps | Electron, PyQt, Tkinter |

## Framework Directory Structure
```
{project_name}/
├── deliverables/           # All project outputs
│   ├── PRD.md             # Project Requirements Document  
│   ├── src/               # Source code
│   ├── test/              # Test code and reports
│   ├── docs/              # Documentation
│   └── requirements.txt   # Dependencies
```

## Development Workflow

### 1. Project Initialization Phase
**Goal**: Establish project scope and technology choices

**Process**:
- Run project wizard: `python framework/tools/project_wizard.py`
- Select application type from supported categories
- Choose technology stack profile
- Generate initial project structure
- Create PRD from application-specific template

**Outputs**: 
- Project directory structure
- Technology-specific boilerplate
- Initial PRD draft

### 2. Requirements Definition Phase  
**Goal**: Create comprehensive, testable requirements

**Process**:
- Use TodoWrite to plan PRD completion tasks
- Follow application-specific discovery questions
- Define user stories relevant to application type
- Specify functional requirements with acceptance criteria
- Set success metrics appropriate for application domain

**Quality Gates**:
- All discovery questions answered
- 5-8 user stories covering core functionality
- 8-15 testable functional requirements
- Clear non-goals to prevent scope creep

### 3. Development Planning Phase
**Goal**: Break down requirements into executable tasks

**Process**:
- Design system architecture appropriate for application type
- Use TodoWrite to create development task breakdown
- Order tasks by dependencies
- Include setup, implementation, testing, and documentation tasks
- Choose appropriate testing strategy for application type

**Outputs**:
- System architecture diagram/description
- Detailed task list with priorities
- Testing strategy plan

### 4. Implementation Phase
**Goal**: Build application following framework standards

**Process**:
For each development task:
- Mark todo as in_progress
- Follow application-type-specific coding standards
- Implement with proper error handling and validation
- Write code that is testable and maintainable
- Mark todo as completed when done

**Code Quality Standards**:
- Use application-appropriate design patterns
- Follow technology stack best practices
- Implement comprehensive error handling
- Include input validation and sanitization
- Follow security best practices for application type
- Write self-documenting code with clear naming

### 5. Testing Phase
**Goal**: Ensure application meets all requirements

**Testing Strategy by Application Type**:
- **Web Apps**: Unit tests, integration tests, E2E browser tests, accessibility tests
- **APIs**: Unit tests, integration tests, API contract tests, load tests
- **CLI Tools**: Unit tests, integration tests, command-line interface tests
- **ML Systems**: Unit tests, model validation tests, data pipeline tests, performance tests
- **Trading Systems**: Unit tests, backtesting, real-time data tests, financial calculations validation

**Process**:
- Use framework test runner: `python test/run_tests.py`
- Generate timestamped test reports
- Achieve >80% code coverage for critical paths
- Validate all PRD functional requirements
- Test application-specific performance criteria

### 6. Documentation Phase
**Goal**: Create comprehensive user and developer documentation

**Documentation Requirements**:
- **README.md**: Installation, basic usage, key features
- **User Guide**: Complete feature documentation with examples
- **Developer Guide**: Architecture, setup, contribution guidelines
- **API Documentation**: For applications with APIs
- **Deployment Guide**: Platform-specific deployment instructions

## Application-Specific Guidance

### Web Applications
**Key Considerations**: 
- Responsive design across devices
- Browser compatibility
- SEO optimization (if applicable)
- Performance and loading times
- User authentication and authorization

**Common Patterns**:
- Frontend-backend separation
- State management (Redux, Vuex, etc.)
- Component-based architecture
- RESTful API design

### APIs & Services
**Key Considerations**:
- RESTful design principles
- OpenAPI/Swagger documentation
- Rate limiting and throttling
- Authentication and authorization
- Error handling and status codes

**Common Patterns**:
- Microservices architecture
- Database abstraction layers
- Middleware for cross-cutting concerns
- API versioning strategies

### CLI Tools
**Key Considerations**:
- Command-line argument parsing
- Help documentation
- Error messages and user feedback
- Cross-platform compatibility
- Installation and distribution

**Common Patterns**:
- Command-subcommand structure
- Configuration file support
- Plugin/extension architecture
- Progress indicators for long operations

### ML Systems
**Key Considerations**:
- Data validation and preprocessing
- Model versioning and reproducibility
- Performance metrics and evaluation
- Feature engineering pipelines
- Model deployment and serving

**Common Patterns**:
- Data pipeline architecture
- Model training and evaluation loops
- Feature stores for data management
- MLOps for model lifecycle management

### Trading Dashboards
**Key Considerations**:
- Real-time data feeds
- Financial calculations accuracy
- Risk management and position sizing
- Backtesting capabilities
- Regulatory compliance

**Common Patterns**:
- Event-driven architecture for real-time updates
- Time series data handling
- Financial indicators and technical analysis
- Portfolio management systems

## Quality Validation Checklist

Before project completion, verify:
- ✅ All PRD functional requirements implemented
- ✅ User stories work end-to-end
- ✅ Success metrics are trackable
- ✅ Non-goals respected (scope maintained)
- ✅ All tests pass with >80% coverage
- ✅ Documentation complete and accurate
- ✅ Application-specific quality standards met
- ✅ Security best practices implemented
- ✅ Performance requirements satisfied
- ✅ Error handling comprehensive

## Task Management Integration

The framework integrates with TodoWrite for systematic task tracking:
- Use TodoWrite to break down PRD into implementation tasks
- Mark tasks as in_progress when starting work
- Complete tasks incrementally with regular updates
- Maintain visibility into project progress
- Ensure no requirements are missed

## Communication Guidelines
- Provide regular progress updates using TodoWrite
- Ask for clarification when requirements are ambiguous
- Suggest improvements while respecting PRD scope
- Flag potential issues early
- Validate application-specific assumptions with domain expertise

---

*This framework provides systematic automation for Claude Code to build high-quality applications across multiple domains while maintaining consistent development standards and quality gates.*