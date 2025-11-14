# XLIFF to TMX Parameterized Conversion - Parameters Guide

## Overview
This XSLT stylesheet converts XLIFF alt-trans elements to TMX format with flexible configuration options.

## Parameters

### 1. `tmx-version` (default: `1.0`)
Controls the TMX version in the output.

**Usage:**
```bash
xsltproc --stringparam tmx-version "1.4" xliff_alttrans_to_tmx_parameterized.xsl input.xliff > output.tmx
```

**Valid values:** `1.0`, `1.1`, `1.2`, `1.3`, `1.4`, etc.

---

### 2. `tu-attributes-mode` (default: `attributes`)
Controls how translation unit (TU) attributes are represented in the output.

**Mode: `attributes` (default)**
- Alt-trans attributes become attributes of the `<tu>` element
- Trans-unit attributes become attributes of the `<tu>` element with `trans-unit-` prefix

**Example output:**
```xml
<tu origin="tm" match-quality="85" trans-unit-id="123">
  <tuv xml:lang="en"><seg>Hello</seg></tuv>
  <tuv xml:lang="nl"><seg>Hallo</seg></tuv>
</tu>
```

**Mode: `prop`**
- Alt-trans attributes become `<prop>` child elements
- Trans-unit attributes become `<prop>` child elements with `trans-unit-` prefix

**Example output:**
```xml
<tu>
  <prop type="origin">tm</prop>
  <prop type="match-quality">85</prop>
  <prop type="trans-unit-id">123</prop>
  <tuv xml:lang="en"><seg>Hello</seg></tuv>
  <tuv xml:lang="nl"><seg>Hallo</seg></tuv>
</tu>
```

**Usage:**
```bash
# Use as attributes (default)
xsltproc xliff_alttrans_to_tmx_parameterized.xsl input.xliff > output.tmx

# Use as prop elements
xsltproc --stringparam tu-attributes-mode "prop" xliff_alttrans_to_tmx_parameterized.xsl input.xliff > output.tmx
```

---

### 3. `tuv-attributes-mode` (default: `attributes`)
Controls how translation unit variant (TUV) attributes are represented in the output.

**Mode: `attributes` (default)**
- Source and target element attributes become attributes of the corresponding `<tuv>` element

**Example output:**
```xml
<tuv xml:lang="en"><seg>Hello</seg></tuv>
<tuv xml:lang="nl" state="translated"><seg>Hallo</seg></tuv>
```

**Mode: `prop`**
- Source and target element attributes become `<prop>` child elements of the corresponding `<tuv>` element

**Example output:**
```xml
<tuv xml:lang="en"><seg>Hello</seg></tuv>
<tuv xml:lang="nl">
  <prop type="state">translated</prop>
  <seg>Hallo</seg>
</tuv>
```

**Usage:**
```bash
# Use as attributes (default)
xsltproc xliff_alttrans_to_tmx_parameterized.xsl input.xliff > output.tmx

# Use as prop elements
xsltproc --stringparam tuv-attributes-mode "prop" xliff_alttrans_to_tmx_parameterized.xsl input.xliff > output.tmx
```

---

### 4. `export-match-quality` (default: `false`)
Controls whether the match-quality attribute is included in the output.

**Usage:**
```bash
# Include match-quality
xsltproc --stringparam export-match-quality "true" xliff_alttrans_to_tmx_parameterized.xsl input.xliff > output.tmx
```

**Valid values:** `true`, `yes`, `1` (to enable) or `false`, `no`, `0` (to disable)

---

## Combining Parameters

You can combine multiple parameters in a single command:

```bash
xsltproc \
  --stringparam tmx-version "1.4" \
  --stringparam tu-attributes-mode "prop" \
  --stringparam tuv-attributes-mode "attributes" \
  --stringparam export-match-quality "true" \
  xliff_alttrans_to_tmx_parameterized.xsl \
  input.xliff > output.tmx
```

---

## Example Scenarios

### Scenario 1: TMX 1.4 with all attributes as attributes (most compact)
```bash
xsltproc --stringparam tmx-version "1.4" xliff_alttrans_to_tmx_parameterized.xsl input.xliff > output.tmx
```

### Scenario 2: TMX 1.0 with all metadata as prop elements (most explicit)
```bash
xsltproc \
  --stringparam tmx-version "1.0" \
  --stringparam tu-attributes-mode "prop" \
  --stringparam tuv-attributes-mode "prop" \
  xliff_alttrans_to_tmx_parameterized.xsl \
  input.xliff > output.tmx
```

### Scenario 3: TMX 1.4 with TU as prop but TUV as attributes
```bash
xsltproc \
  --stringparam tmx-version "1.4" \
  --stringparam tu-attributes-mode "prop" \
  --stringparam tuv-attributes-mode "attributes" \
  xliff_alttrans_to_tmx_parameterized.xsl \
  input.xliff > output.tmx
```
