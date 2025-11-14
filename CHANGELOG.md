# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [4.0.0] - 2025-11-14

### Added
- **Hybrid mode**: Both individual and merge conversion modes
- **Smart filename generation**: Includes file count and TU count in merge mode
- **Detailed statistics**: Per-file contribution with percentages
- **Enhanced UTF-16 support**: Robust BOM detection for UTF-16 LE/BE
- **UTF-32 support**: Both LE and BE variants
- **PyInstaller compatibility**: Can be compiled to standalone executable
- **Auto-countdown feature**: User-friendly console closure
- **--no-countdown flag**: For automation workflows
- Contribution percentage calculations in merge mode
- Better error messages with encoding information

### Changed
- Unified script combining individual and merge approaches
- Improved encoding detection algorithm
- Enhanced verbose output with detailed tables
- Better file discovery with duplicate prevention

### Fixed
- UTF-16 encoding errors (0xFF 0xFE BOM)
- Encoding detection failures on edge cases
- memoQ namespace compatibility issues

## [3.0.0] - 2025-11-13

### Added
- **Directory processing**: Process entire folders
- **Recursive search**: `-r` flag for subdirectory traversal
- **Multiple extension support**: Auto-detects .xlf, .xliff, .mxliff, .mqxliff, .sdlxliff
- **Custom extension filtering**: `--ext` option
- **Mixed inputs**: Combine files, directories, and wildcards
- Detailed per-file statistics

### Changed
- Enhanced file discovery system
- Improved verbose output

## [2.2.0] - 2025-11-12

### Added
- **Parameterized XSLT**: Optional match-quality export
- **Match-quality control**: `-m` flag to toggle
- Basic UTF-16 encoding support
- Verbose mode with statistics
- Multiple file processing
- Wildcard support

### Fixed
- memoQ namespace issues in inline elements

## [2.0.0] - 2025-11-11

### Added
- Enhanced XSLT with dynamic attribute capture
- Inline formatting element preservation
- All attribute extraction (not just match-quality)

### Changed
- Improved XSLT transformation logic

## [1.0.0] - 2025-11-10

### Added
- Initial release
- Basic XLIFF to TMX conversion
- Match-quality and origin extraction
- Simple XSLT transformation

---

## Version Naming Convention

- **Major version (X.0.0)**: Breaking changes or major feature additions
- **Minor version (0.X.0)**: New features, backward compatible
- **Patch version (0.0.X)**: Bug fixes, backward compatible

## Upgrade Notes

### From v3.0 to v4.0
- All v3.0 commands work the same in individual mode
- Add `--merge` flag to use new merge functionality
- No breaking changes

### From v2.2 to v3.0
- Replace manual `cd` commands with directory paths
- Add `-r` for recursive processing
- No breaking changes in basic usage

### From v2.0 to v2.2
- Add `-m` flag if you want match-quality (previously always exported)
- No other changes required
