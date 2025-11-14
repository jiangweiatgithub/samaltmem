# Contributing to XLIFF to TMX Converter

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## 🤝 Ways to Contribute

- **Report bugs**: Open an issue describing the bug
- **Suggest features**: Open an issue with your feature request
- **Submit fixes**: Create a pull request with your changes
- **Improve documentation**: Help make our docs better
- **Share use cases**: Tell us how you're using the tool

## 🐛 Reporting Bugs

### Before Reporting
1. Check if the issue already exists
2. Test with the latest version
3. Gather relevant information

### Bug Report Template
```
**Description**
Clear description of the bug

**To Reproduce**
Steps to reproduce the behavior:
1. Run command '...'
2. With files '...'
3. See error

**Expected Behavior**
What you expected to happen

**Environment**
- OS: [e.g., Windows 10, macOS 12, Ubuntu 22.04]
- Python version: [e.g., 3.9.7]
- Script version: [e.g., 4.0.0]

**Sample Files**
If possible, attach sample XLIFF files (or anonymized versions)

**Error Output**
```
Paste full error message here
```
```

## 💡 Suggesting Features

### Feature Request Template
```
**Feature Description**
Clear description of the feature

**Use Case**
Why this feature would be useful

**Proposed Solution**
How you envision it working

**Alternatives Considered**
Other approaches you've thought about
```

## 🔧 Development Setup

### Prerequisites
- Python 3.6 or higher
- Git
- Text editor or IDE

### Setup Steps
```bash
# Fork the repository on GitHub

# Clone your fork
git clone https://github.com/YOUR_USERNAME/xliff-to-tmx.git
cd xliff-to-tmx

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
python xliff_to_tmx_hybrid.py --help
```

## 📝 Code Style

### Python Style Guide
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use 4 spaces for indentation
- Maximum line length: 100 characters
- Use descriptive variable names

### Documentation
- Add docstrings to functions
- Comment complex logic
- Update README when adding features

### Example
```python
def convert_xliff_to_tmx(xliff_path, export_match_quality=False, verbose=False):
    """
    Convert single XLIFF file to TMX format.
    
    Args:
        xliff_path (Path): Path to input XLIFF file
        export_match_quality (bool): Include match-quality in output
        verbose (bool): Print detailed information
    
    Returns:
        tuple: (tmx_root_element, tu_count) or (None, 0) on error
    """
    # Implementation...
```

## 🔀 Pull Request Process

### Before Submitting
1. **Test your changes** thoroughly
2. **Update documentation** if needed
3. **Follow code style** guidelines
4. **Keep commits atomic** (one logical change per commit)

### Commit Messages
Use clear, descriptive commit messages:
```
Good:
- "Fix UTF-16 encoding detection for BOM-less files"
- "Add --output-dir option for custom output location"
- "Update README with new examples"

Bad:
- "Fix bug"
- "Update"
- "Changes"
```

### Pull Request Template
```
**Description**
Brief description of changes

**Type of Change**
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

**Testing**
How you tested your changes

**Related Issues**
Fixes #123, Closes #456
```

### Review Process
1. Submit pull request
2. Automated checks will run
3. Maintainer will review
4. Address feedback if needed
5. Once approved, it will be merged

## 🧪 Testing

### Manual Testing
```bash
# Test with sample files
python xliff_to_tmx_hybrid.py test_samples/ -v

# Test individual mode
python xliff_to_tmx_hybrid.py test_samples/ -r -v

# Test merge mode
python xliff_to_tmx_hybrid.py test_samples/ -r --merge -v

# Test UTF-16 files
python xliff_to_tmx_hybrid.py utf16_samples/ -r -v
```

### Test Coverage Areas
- [ ] Individual mode conversion
- [ ] Merge mode conversion
- [ ] UTF-8 encoding
- [ ] UTF-16 encoding (LE/BE)
- [ ] Multiple extensions
- [ ] Recursive directory processing
- [ ] Error handling
- [ ] Match-quality export

## 📚 Documentation Guidelines

### README Updates
- Keep examples up-to-date
- Add new features to feature list
- Update command-line options table

### Code Documentation
- Document all public functions
- Explain complex algorithms
- Add type hints where helpful

### User Documentation
- Create examples for new features
- Update troubleshooting guide
- Add common use cases

## 🚀 Release Process

### Version Numbering
- **Major (X.0.0)**: Breaking changes
- **Minor (0.X.0)**: New features, backward compatible
- **Patch (0.0.X)**: Bug fixes

### Release Checklist
1. Update version number in script
2. Update CHANGELOG.md
3. Update README.md
4. Test all features
5. Create GitHub release
6. Tag release (e.g., v4.0.0)

## 💬 Community Guidelines

### Be Respectful
- Welcome newcomers
- Be patient with questions
- Provide constructive feedback
- Respect different perspectives

### Be Helpful
- Answer questions when you can
- Share your use cases
- Help improve documentation
- Report bugs you encounter

### Communication Channels
- **Issues**: Bug reports and feature requests
- **Pull Requests**: Code contributions
- **Discussions**: General questions and ideas

## 📋 Feature Development Workflow

### 1. Planning
- Open an issue to discuss the feature
- Get feedback from maintainers
- Plan implementation approach

### 2. Development
- Create a feature branch
- Implement the feature
- Add tests
- Update documentation

### 3. Review
- Submit pull request
- Address review comments
- Ensure all checks pass

### 4. Release
- Feature is merged
- Included in next release
- Documented in CHANGELOG

## 🎯 Priority Areas

We're especially interested in contributions for:
- [ ] Additional encoding support
- [ ] Performance optimizations
- [ ] Better error messages
- [ ] More comprehensive tests
- [ ] Additional CAT tool compatibility
- [ ] GUI wrapper
- [ ] Web interface
- [ ] Docker support

## 📞 Questions?

If you have questions about contributing:
- Open an issue with the "question" label
- Check existing documentation
- Reach out to maintainers

## 🙏 Thank You!

Thank you for contributing to making this tool better for the translation community!

---

**Remember**: No contribution is too small. Whether it's fixing a typo, reporting a bug, or adding a feature, all contributions are valued!
