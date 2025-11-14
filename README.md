# SamAltmem
```
 ___                 _ _                     
/ __| __ _ _ __  __ _| | |_ _ __  ___ _ __  
\__ \/ _` | '  \/ _` | |  _| '  \/ -_) '  \ 
|___/\__,_|_|_|_\__,_|_|\__|_|_|_\___|_|_|_|
```
### **S**ome **Alt**ernative Translation **Mem**ory Creation

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Mac%20%7C%20Linux-lightgrey)](https://github.com/jiangweiatgithub/samaltmem)

Extract alternative translations (alt-trans) from XLIFF files and convert them to TMX format. Build comprehensive translation memories from fuzzy matches, machine translation suggestions, and other alternative translations stored in your CAT tool exports.

**Perfect for:** Translators • Translation Agencies • LSPs • Localization Managers

**Works with:** memoQ • SDL Trados • Wordfast • All TMX 1.4 tools

## ✨ Features

### Core Capabilities
- **Extract all alt-trans elements** from XLIFF files
- **Preserve all attributes** (origin, match-quality, tool, tool-id, etc.)
- **Inline formatting support** (bpt, ept, ph elements preserved)
- **Automatic language detection** from XLIFF headers
- **Optional match-quality export** (can be toggled on/off)

### Advanced Features
- **Two operation modes:**
  - **Individual mode** (default): Each XLIFF → separate TMX file
  - **Merge mode** (`--merge`): All XLIFFs → one combined TMX
- **Recursive directory processing** with `-r` flag
- **Multiple file extensions** supported automatically:
  - `.xlf`, `.xliff`, `.mxliff`, `.mqxliff`, `.sdlxliff`
- **Custom extension filtering** with `--ext` option
- **Smart filename generation** in merge mode:
  - Includes file count and TU count (e.g., `combined_5files_234tus.tmx`)
- **Detailed statistics:**
  - Per-file contribution breakdown
  - Percentage calculations
  - Success/failure reporting

### Encoding Support
- ✅ UTF-8 (with or without BOM)
- ✅ UTF-16 (LE/BE, with or without BOM)
- ✅ UTF-32 (LE/BE)
- ✅ Robust BOM detection
- ✅ Automatic encoding conversion

### CAT Tool Compatibility
- ✅ memoQ (fixed namespace issues)
- ✅ SDL Trados
- ✅ Wordfast
- ✅ memoSource
- ✅ All TMX 1.4 compliant tools

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/jiangweiatgithub/samaltmem.git
cd samaltmem

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```bash
# Individual mode (default) - each XLIFF → separate TMX
python xliff_to_tmx_hybrid.py /path/to/xliff/files/ -r -v

# Merge mode - all XLIFFs → one combined TMX
python xliff_to_tmx_hybrid.py /path/to/xliff/files/ -r --merge -v

# With match-quality
python xliff_to_tmx_hybrid.py /path/to/xliff/files/ -r -m --merge
```

## 📖 Documentation

### Command-Line Options

```
positional arguments:
  INPUT                 Input XLIFF file(s), directory(ies), or patterns

optional arguments:
  -h, --help            Show help message
  -o FILE, --output FILE Output TMX file (merge mode only)
  --merge               Merge all into one TMX (default: individual)
  -r, --recursive       Search directories recursively
  --ext EXT             Filter by file extension(s)
  -m, --export-match-quality
                        Include match-quality property
  -v, --verbose         Show detailed statistics
  --no-countdown        Skip countdown (for automation)
  --version             Show version number
```

### Usage Examples

#### Single File Conversion
```bash
python xliff_to_tmx_hybrid.py document.xlf -o output.tmx -m
```

#### Directory Processing (Individual)
```bash
# Each XLIFF → separate TMX
python xliff_to_tmx_hybrid.py /project/translations/ -r -v
```

#### Directory Processing (Merged)
```bash
# All XLIFFs → one combined TMX
python xliff_to_tmx_hybrid.py /project/translations/ -r --merge -v
```

#### Custom Extensions
```bash
# Process only memoQ files
python xliff_to_tmx_hybrid.py /project/ -r --ext .mxliff --ext .mqxliff --merge
```

#### Multiple Projects
```bash
# Combine multiple client projects
python xliff_to_tmx_hybrid.py /clients/*/translations/ -r -m --merge -o master_tm.tmx
```

## 🎯 Use Cases

### For Freelance Translators
- Extract fuzzy matches from XLIFF files
- Build personal translation memories
- Organize TMs by project

### For Translation Agencies
- Build master TMs from multiple projects
- Track contribution per project/translator
- Automate TM maintenance workflows

### For LSPs
- Daily batch processing of incoming files
- Create reference TMs for specific domains
- Maintain separate TMs per client

## 📊 Output Examples

### Individual Mode
```
======================================================================
INDIVIDUAL MODE: Converting 3 file(s)
======================================================================

[1/3] project/file1.xlf
  ✅ Output: file1.tmx (12 TUs)

[2/3] project/file2.xliff
  ✅ Output: file2.tmx (23 TUs)

[3/3] project/subfolder/file3.xlf
  ✅ Output: file3.tmx (18 TUs)

======================================================================
SUMMARY - INDIVIDUAL MODE
======================================================================
Files processed:  3/3
Total TUs:        53

Detailed Statistics:
  Input File                               Output File                                 TUs
  ---------------------------------------- ---------------------------------------- ------
  ✅ file1.xlf                              file1.tmx                                  12
  ✅ file2.xliff                            file2.tmx                                  23
  ✅ file3.xlf                              file3.tmx                                  18
```

### Merge Mode
```
======================================================================
MERGE MODE: Combining 3 file(s) into one TMX
======================================================================

[1/3] project/file1.xlf
  ✅ Added 12 TUs

[2/3] project/file2.xliff
  ✅ Added 23 TUs

[3/3] project/subfolder/file3.xlf
  ✅ Added 18 TUs

======================================================================
SUMMARY - MERGE MODE
======================================================================
Files combined:   3
Total TUs:        53
Output file:      combined_3files_53tus.tmx

Contribution per file:
  Status File Name                                               TUs      %
  ------ -------------------------------------------------- -------- ------
  ✅      file1.xlf                                                12  22.6%
  ✅      file2.xliff                                              23  43.4%
  ✅      file3.xlf                                                18  34.0%

✅ Combined TMX saved to: combined_3files_53tus.tmx
```

## 🔧 Technical Details

### Architecture
- **Core engine:** XSLT transformation with lxml
- **Encoding detection:** BOM-based with fallback
- **Output format:** TMX 1.4 compliant
- **Namespace handling:** Clean output (memoQ compatible)

### Requirements
- Python 3.6 or higher
- lxml library
- XSLT stylesheet (included)

### Files Structure
```
samaltmem/
├── samaltmem.py                            # Main script (branded name) ⭐
├── xliff_to_tmx_hybrid.py                  # Same script (technical name)
├── xliff_alttrans_to_tmx_parameterized.xsl # XSLT transformer
├── requirements.txt                         # Python dependencies
├── README.md                               # This file
├── LICENSE                                 # MIT License
├── CHANGELOG.md                            # Version history
├── CONTRIBUTING.md                         # Contribution guidelines
└── BRANDING.md                             # Brand identity guide
```

## 🐛 Troubleshooting

### UTF-16 Encoding Errors
The script automatically detects and handles UTF-16 files. If you encounter encoding errors:
```bash
# Use verbose mode to see encoding detection
python xliff_to_tmx_hybrid.py file.xlf -v
```

### No Files Found
```bash
# Check extensions being searched
python xliff_to_tmx_hybrid.py /folder/ -v

# Use recursive search
python xliff_to_tmx_hybrid.py /folder/ -r

# Specify custom extension
python xliff_to_tmx_hybrid.py /folder/ --ext .yourext
```

### memoQ Import Issues
- ✅ Namespace issues are fixed in current version
- ✅ Output is TMX 1.4 compliant
- ✅ Inline elements properly formatted

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
```bash
# Clone repository
git clone https://github.com/jiangweiatgithub/samaltmem.git
cd samaltmem

# Install dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Your Name**
- GitHub: [@jiangweiatgithub](https://github.com/jiangweiatgithub)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Thanks to all contributors and users
- Inspired by the needs of the translation industry
- Built with Python and lxml

## 📈 Version History

### v4.0 (Current - Hybrid Version)
- Individual and merge modes
- Smart filename with statistics
- Detailed contribution reporting
- Enhanced UTF-16 support
- PyInstaller compatibility

### v3.0 (Enhanced)
- Directory processing
- Recursive search
- Multiple extension support
- Custom extension filtering

### v2.2 (Basic)
- Initial public release
- Basic XLIFF to TMX conversion
- Match-quality control

## 🔗 Links

- [Documentation](docs/)
- [Issue Tracker](https://github.com/jiangweiatgithub/samaltmem/issues)
- [Changelog](CHANGELOG.md)

## ⭐ Star History

If you find this tool useful, please consider giving it a star!

---

**Made with ❤️ for the translation community**
