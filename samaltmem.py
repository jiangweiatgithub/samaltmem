#!/usr/bin/env python3
"""
SamAltmem - Some Alt Translation Memory Creation
XLIFF alt-trans to TMX Converter (v4.0)
---------------------------------------------------------
✅ Individual mode (default): Each XLIFF → separate TMX
✅ Merge mode (--merge): All XLIFFs → one combined TMX
✅ Smart filename: includes file count and TU count (e.g., combined_5files_234tus.tmx)
✅ Detailed statistics: Shows contribution per file
✅ UTF-8 / UTF-16 (LE/BE) auto-detection
✅ Multiple extensions: .xlf, .xliff, .mxliff, .mqxliff, .sdlxliff
✅ Custom extension filtering (--ext)
✅ Recursive directory search (-r)
✅ Match-quality control (-m)
✅ srclang attribute in TMX header
✅ PyInstaller compatible
"""

import sys
import os
import time
import argparse
from pathlib import Path
from lxml import etree


# Supported XLIFF file extensions
XLIFF_EXTENSIONS = ['.xlf', '.xliff', '.mxliff', '.mqxliff', '.sdlxliff']


# === Utility: PyInstaller resource-safe path ===
def resource_path(relative_path):
    """Get absolute path to resource (works for PyInstaller and normal run)."""
    if hasattr(sys, '_MEIPASS'):
        return Path(os.path.join(sys._MEIPASS, relative_path))
    return Path(relative_path)


# === Utility: Countdown before closing ===
def countdown_before_exit(seconds=15):
    """Show countdown before closing console when run as .exe."""
    if sys.stdin and sys.stdin.isatty():
        print(f"\nConsole will close automatically in {seconds} seconds...")
        print("(Press Ctrl+C to exit immediately)")
        try:
            for i in range(seconds, 0, -1):
                print(f"  Closing in {i:2d}...", end="\r", flush=True)
                time.sleep(1)
            print(" " * 40, end="\r")  # Clear line
        except KeyboardInterrupt:
            print("\nExiting...", flush=True)


# === Find XLIFF files ===
def find_xliff_files(paths, recursive=False, extensions=None):
    """Find all XLIFF files from given paths."""
    if extensions is None:
        extensions = XLIFF_EXTENSIONS
    
    # Normalize extensions
    extensions = [ext.lower() if ext.startswith('.') else f'.{ext.lower()}' for ext in extensions]
    
    xliff_files = []
    seen_files = set()
    
    for path_str in paths:
        path = Path(path_str)
        
        if path.is_file():
            if path.suffix.lower() in extensions:
                abs_path = path.resolve()
                if abs_path not in seen_files:
                    xliff_files.append(path)
                    seen_files.add(abs_path)
        elif path.is_dir():
            # Search directory
            pattern = path.rglob('*') if recursive else path.glob('*')
            for file in pattern:
                if file.is_file() and file.suffix.lower() in extensions:
                    abs_path = file.resolve()
                    if abs_path not in seen_files:
                        xliff_files.append(file)
                        seen_files.add(abs_path)
        else:
            print(f"Warning: Path not found: {path}", file=sys.stderr)
    
    return sorted(xliff_files)


# === Convert single XLIFF to TMX ===
def convert_xliff_to_tmx(xliff_path, export_match_quality=False, verbose=False):
    """
    Convert single XLIFF file to TMX format.
    Returns tuple: (tmx_root_element, tu_count) or (None, 0) on error
    """
    try:
        if verbose:
            print(f"  Reading: {xliff_path.name}", file=sys.stderr)
        
        # Robust encoding detection - try multiple encodings
        content = None
        detected_encoding = None
        
        # First, check for BOM
        with open(xliff_path, 'rb') as f:
            bom = f.read(4)
        
        # Detect encoding from BOM
        if bom.startswith(b'\xff\xfe\x00\x00'):
            encodings = ['utf-32-le']
        elif bom.startswith(b'\x00\x00\xfe\xff'):
            encodings = ['utf-32-be']
        elif bom.startswith(b'\xff\xfe'):
            encodings = ['utf-16-le', 'utf-16']
        elif bom.startswith(b'\xfe\xff'):
            encodings = ['utf-16-be', 'utf-16']
        elif bom.startswith(b'\xef\xbb\xbf'):
            encodings = ['utf-8-sig', 'utf-8']
        else:
            # No BOM detected, try common encodings
            encodings = ['utf-8', 'utf-16', 'utf-16-le', 'utf-16-be', 'latin-1']
        
        # Try each encoding
        for enc in encodings:
            try:
                with open(xliff_path, 'r', encoding=enc) as f:
                    content = f.read()
                detected_encoding = enc
                if verbose and enc != 'utf-8':
                    print(f"    Detected {enc.upper()} encoding", file=sys.stderr)
                break
            except (UnicodeDecodeError, UnicodeError):
                continue
        
        if content is None:
            raise ValueError(f"Could not decode file with any known encoding. Tried: {', '.join(encodings)}")
        
        # Normalize XML declaration to UTF-8
        encodings_to_normalize = [
            "UTF-16", "UTF-16LE", "UTF-16BE", "utf-16", "utf-16le", "utf-16be",
            "UTF-32", "UTF-32LE", "UTF-32BE", "utf-32", "utf-32le", "utf-32be",
            "utf-8-sig"
        ]
        for enc in encodings_to_normalize:
            content = content.replace(f"encoding='{enc}'", "encoding='UTF-8'")
            content = content.replace(f'encoding="{enc}"', 'encoding="UTF-8"')
        
        xliff_doc = etree.fromstring(content.encode('utf-8'))
        
        # Load XSLT (resource-safe for PyInstaller)
        xslt_path = resource_path('xliff_alttrans_to_tmx_parameterized.xsl')
        if not xslt_path.exists():
            raise FileNotFoundError(f"XSLT file not found: {xslt_path}")
        
        xslt_doc = etree.parse(str(xslt_path))
        transform = etree.XSLT(xslt_doc)
        
        # Set parameters
        params = {}
        if export_match_quality:
            params['export-match-quality'] = "'true'"
        
        # Transform
        result = transform(xliff_doc, **params)
        tu_count = len(result.xpath('//tu'))
        
        if verbose:
            print(f"    Extracted: {tu_count} TUs", file=sys.stderr)
        
        return result.getroot(), tu_count
        
    except Exception as e:
        print(f"  ❌ Error processing {xliff_path.name}: {e}", file=sys.stderr)
        if verbose:
            import traceback
            traceback.print_exc(file=sys.stderr)
        return None, 0


# === Individual mode: Convert each file separately ===
def convert_individual(xliff_files, export_match_quality=False, verbose=False):
    """Convert each XLIFF to its own TMX file."""
    success_count = 0
    total_tus = 0
    
    print(f"\n{'='*70}", file=sys.stderr)
    print(f"INDIVIDUAL MODE: Converting {len(xliff_files)} file(s)", file=sys.stderr)
    print(f"{'='*70}", file=sys.stderr)
    
    file_stats = []
    
    for i, xliff_path in enumerate(xliff_files, 1):
        print(f"\n[{i}/{len(xliff_files)}] {xliff_path}", file=sys.stderr)
        
        # Convert
        tmx_root, tu_count = convert_xliff_to_tmx(xliff_path, export_match_quality, verbose)
        
        if tmx_root is not None:
            # Write individual TMX file
            output_path = xliff_path.with_suffix('.tmx')
            output_bytes = etree.tostring(tmx_root, 
                                         pretty_print=False, 
                                         xml_declaration=True, 
                                         encoding='UTF-8')
            with open(output_path, 'wb') as f:
                f.write(output_bytes)
            
            print(f"  ✅ Output: {output_path.name} ({tu_count} TUs)", file=sys.stderr)
            success_count += 1
            total_tus += tu_count
            file_stats.append((xliff_path.name, output_path.name, tu_count))
        else:
            print(f"  ❌ Failed", file=sys.stderr)
            file_stats.append((xliff_path.name, "FAILED", 0))
    
    # Summary
    print(f"\n{'='*70}", file=sys.stderr)
    print(f"SUMMARY - INDIVIDUAL MODE", file=sys.stderr)
    print(f"{'='*70}", file=sys.stderr)
    print(f"Files processed:  {success_count}/{len(xliff_files)}", file=sys.stderr)
    print(f"Total TUs:        {total_tus}", file=sys.stderr)
    
    if file_stats:
        print(f"\nDetailed Statistics:", file=sys.stderr)
        print(f"  {'Input File':<40} {'Output File':<40} {'TUs':>6}", file=sys.stderr)
        print(f"  {'-'*40} {'-'*40} {'-'*6}", file=sys.stderr)
        for inp, out, tus in file_stats:
            status = "✅" if tus > 0 else "❌"
            print(f"  {status} {inp:<38} {out:<38} {tus:>6}", file=sys.stderr)
    
    return success_count == len(xliff_files)


# === Merge mode: Combine all files into one TMX ===
def convert_merged(xliff_files, output_path=None, export_match_quality=False, verbose=False):
    """Combine all XLIFF files into one TMX file."""
    print(f"\n{'='*70}", file=sys.stderr)
    print(f"MERGE MODE: Combining {len(xliff_files)} file(s) into one TMX", file=sys.stderr)
    print(f"{'='*70}", file=sys.stderr)
    
    # Extract source language from first XLIFF file for TMX header
    srclang = "en"  # Default fallback
    try:
        with open(xliff_files[0], 'rb') as f:
            bom = f.read(4)
        
        # Detect encoding
        if bom.startswith(b'\xff\xfe\x00\x00'):
            encoding = 'utf-32-le'
        elif bom.startswith(b'\x00\x00\xfe\xff'):
            encoding = 'utf-32-be'
        elif bom.startswith(b'\xff\xfe'):
            encoding = 'utf-16'
        elif bom.startswith(b'\xfe\xff'):
            encoding = 'utf-16-be'
        elif bom.startswith(b'\xef\xbb\xbf'):
            encoding = 'utf-8-sig'
        else:
            encoding = 'utf-8'
        
        # Parse first file to get source language
        with open(xliff_files[0], 'r', encoding=encoding) as f:
            content = f.read()
        
        # Normalize encoding in XML declaration
        encodings_to_normalize = [
            "UTF-16", "UTF-16LE", "UTF-16BE", "utf-16", "utf-16le", "utf-16be",
            "UTF-32", "UTF-32LE", "UTF-32BE", "utf-32", "utf-32le", "utf-32be",
            "utf-8-sig"
        ]
        for enc in encodings_to_normalize:
            content = content.replace(f"encoding='{enc}'", "encoding='UTF-8'")
            content = content.replace(f'encoding="{enc}"', 'encoding="UTF-8"')
        
        first_doc = etree.fromstring(content.encode('utf-8'))
        
        # Try with namespace
        namespaces = {'xliff': 'urn:oasis:names:tc:xliff:document:1.1'}
        file_elem = first_doc.xpath('//xliff:file', namespaces=namespaces)
        
        # If namespace query fails, try without namespace
        if not file_elem:
            file_elem = first_doc.xpath('//file')
        
        if file_elem:
            srclang = file_elem[0].get('source-language', 'en')
            if verbose:
                print(f"  Source language: {srclang}", file=sys.stderr)
    except Exception as e:
        if verbose:
            print(f"  Warning: Could not extract source language ({e}), using default: en", file=sys.stderr)
    
    # Create root TMX structure with srclang
    tmx_root = etree.Element("tmx", version="1.4")
    etree.SubElement(tmx_root, "header",
                     creationtool="SamAltmem",
                     creationtoolversion="4.0",
                     segtype="sentence",
                     adminlang="en",
                     datatype="xml",
                     srclang=srclang)
    body = etree.SubElement(tmx_root, "body")
    
    total_tus = 0
    file_stats = []
    
    for i, xliff_path in enumerate(xliff_files, 1):
        print(f"\n[{i}/{len(xliff_files)}] {xliff_path}", file=sys.stderr)
        
        # Convert
        tmx_fragment, tu_count = convert_xliff_to_tmx(xliff_path, export_match_quality, verbose)
        
        if tmx_fragment is not None:
            # Extract TUs and append to body
            tus = tmx_fragment.xpath('//tu')
            for tu in tus:
                body.append(tu)
            
            print(f"  ✅ Added {tu_count} TUs", file=sys.stderr)
            total_tus += tu_count
            file_stats.append((xliff_path.name, tu_count, "✅"))
        else:
            print(f"  ❌ Failed", file=sys.stderr)
            file_stats.append((xliff_path.name, 0, "❌"))
    
    # Determine output filename with smart naming
    if output_path is None:
        # Default: use first file's directory
        base_dir = xliff_files[0].parent
        output_path = base_dir / f"combined_{len(xliff_files)}files_{total_tus}tus.tmx"
    else:
        # User specified output, but enhance with stats if it doesn't have them
        output_path = Path(output_path)
        stem = output_path.stem
        # Add stats if not already in filename
        if 'files' not in stem.lower() and 'tus' not in stem.lower():
            output_path = output_path.parent / f"{stem}_{len(xliff_files)}files_{total_tus}tus.tmx"
    
    # Write final TMX
    output_bytes = etree.tostring(tmx_root, 
                                  pretty_print=False, 
                                  xml_declaration=True, 
                                  encoding='UTF-8')
    with open(output_path, 'wb') as f:
        f.write(output_bytes)
    
    # Summary
    print(f"\n{'='*70}", file=sys.stderr)
    print(f"SUMMARY - MERGE MODE", file=sys.stderr)
    print(f"{'='*70}", file=sys.stderr)
    print(f"Files combined:   {len(xliff_files)}", file=sys.stderr)
    print(f"Total TUs:        {total_tus}", file=sys.stderr)
    print(f"Output file:      {output_path}", file=sys.stderr)
    
    if file_stats:
        print(f"\nContribution per file:", file=sys.stderr)
        print(f"  {'Status':<6} {'File Name':<50} {'TUs':>8} {'%':>6}", file=sys.stderr)
        print(f"  {'-'*6} {'-'*50} {'-'*8} {'-'*6}", file=sys.stderr)
        for fname, tus, status in file_stats:
            percentage = (tus / total_tus * 100) if total_tus > 0 else 0
            print(f"  {status:<6} {fname:<50} {tus:>8} {percentage:>5.1f}%", file=sys.stderr)
    
    print(f"\n✅ Combined TMX saved to: {output_path}", file=sys.stderr)
    
    return True


# === Main Program ===
def main():
    parser = argparse.ArgumentParser(
        description='SamAltmem (Some Alt Translation Memory) v4.0',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Individual mode (override default)
  %(prog)s input.xlf --no-merge
  %(prog)s folder/ -r --no-merge

  # Merge mode (default)
  %(prog)s input.xlf
  %(prog)s /project/ -r -m
  %(prog)s /project/ -r -m --merge
  %(prog)s folder1 folder2 --merge -o combined.tmx
        """
    )

    parser.add_argument(
        'inputs',
        nargs='+',
        metavar='INPUT',
        help='Input XLIFF file(s), directory(ies), or wildcard patterns'
    )

    parser.add_argument(
        '-o', '--output',
        metavar='FILE',
        help='Output TMX file (merge mode only). Auto-named if not specified.'
    )

    # ✅ merge ON by default
    parser.add_argument(
        '--merge',
        action='store_true',
        default=True,
        help='Enable merge mode (default: ON)'
    )

    # ✅ individual mode override
    parser.add_argument(
        '--no-merge',
        action='store_true',
        help='Disable merge mode (use individual conversion)'
    )

    # the rest of your arguments unchanged
    parser.add_argument('-r', '--recursive', action='store_true')
    parser.add_argument('--ext', '--extension', action='append', dest='extensions', metavar='EXT')
    parser.add_argument('-m', '--export-match-quality', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    parser.add_argument('--no-countdown', action='store_true')
    parser.add_argument('--version', action='version', version='%(prog)s 4.0 (Hybrid)')

    args = parser.parse_args()

    # =============================
    #   🔥 FINAL MERGE DECISION
    # =============================
    merge = args.merge and not args.no_merge

    # From here forward, the rest of your script remains unchanged
    extensions = args.extensions if args.extensions else XLIFF_EXTENSIONS
    xliff_files = find_xliff_files(args.inputs, recursive=args.recursive, extensions=extensions)

    if not xliff_files:
        print("❌ No XLIFF files found matching the criteria", file=sys.stderr)
        if not args.no_countdown:
            countdown_before_exit(15)
        sys.exit(1)

    try:
        if merge:
            success = convert_merged(xliff_files, args.output, args.export_match_quality, args.verbose)
        else:
            if args.output:
                print("Warning: -o/--output ignored in individual mode (use --merge to enable)", file=sys.stderr)
            success = convert_individual(xliff_files, args.export_match_quality, args.verbose)

        if not args.no_countdown:
            countdown_before_exit(15)
        sys.exit(0 if success else 1)

    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Fatal error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc(file=sys.stderr)
        if not args.no_countdown:
            countdown_before_exit(15)
        sys.exit(1)


if __name__ == '__main__':
    main()