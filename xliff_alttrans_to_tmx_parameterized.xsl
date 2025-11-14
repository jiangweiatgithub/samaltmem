<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xliff="urn:oasis:names:tc:xliff:document:1.1"
    exclude-result-prefixes="xliff">
    
    <!-- PARAMETER: Export match-quality property (default: false) -->
    <xsl:param name="export-match-quality" select="'false'"/>
    
    <!-- Ultra-minimal: no indentation, newlines only between structural elements -->
    <xsl:output method="xml" indent="no" encoding="UTF-8"/>
    
    <!-- Root template -->
    <xsl:template match="/">
        <xsl:text>&#10;</xsl:text>
        <tmx version="1.4">
            <xsl:text>&#10;</xsl:text>
            <header 
                creationtool="XLIFF-to-TMX-Converter" 
                creationtoolversion="2.2" 
                segtype="sentence" 
                o-tmf="XLIFF"
                adminlang="en"
                datatype="xml">
                <xsl:attribute name="srclang">
                    <xsl:value-of select="//xliff:file/@source-language"/>
                </xsl:attribute>
            </header>
            <xsl:text>&#10;</xsl:text>
            <body>
                <xsl:text>&#10;</xsl:text>
                <!-- Process all alt-trans elements -->
                <xsl:apply-templates select="//xliff:alt-trans"/>
            </body>
            <xsl:text>&#10;</xsl:text>
        </tmx>
        <xsl:text>&#10;</xsl:text>
    </xsl:template>
    
    <!-- Template for each alt-trans element -->
    <xsl:template match="xliff:alt-trans">
        <tu>
            <xsl:text>&#10;</xsl:text>
            <!-- Dynamically capture ALL attributes from alt-trans element -->
            <xsl:for-each select="@*">
                <xsl:choose>
                    <!-- Handle match-quality attribute based on parameter -->
                    <xsl:when test="name() = 'match-quality'">
                        <xsl:if test="$export-match-quality = 'true' or $export-match-quality = 'yes' or $export-match-quality = '1'">
                            <prop type="match-quality">
                                <xsl:value-of select="."/>
                            </prop>
                            <xsl:text>&#10;</xsl:text>
                        </xsl:if>
                    </xsl:when>
                    <!-- Skip xml namespace attributes as they're not standard properties -->
                    <xsl:when test="namespace-uri() = 'http://www.w3.org/XML/1998/namespace'">
                        <prop type="xml-{local-name()}">
                            <xsl:value-of select="."/>
                        </prop>
                        <xsl:text>&#10;</xsl:text>
                    </xsl:when>
                    <!-- All other attributes become properties -->
                    <xsl:otherwise>
                        <prop type="{name()}">
                            <xsl:value-of select="."/>
                        </prop>
                        <xsl:text>&#10;</xsl:text>
                    </xsl:otherwise>
                </xsl:choose>
            </xsl:for-each>
            
            <!-- Add trans-unit ID and other parent attributes for reference -->
            <xsl:if test="../@id">
                <prop type="trans-unit-id">
                    <xsl:value-of select="../@id"/>
                </prop>
                <xsl:text>&#10;</xsl:text>
            </xsl:if>
            
            <!-- Capture other trans-unit attributes if present -->
            <xsl:for-each select="../@*[name() != 'id']">
                <prop type="trans-unit-{name()}">
                    <xsl:value-of select="."/>
                </prop>
                <xsl:text>&#10;</xsl:text>
            </xsl:for-each>
            
            <!-- Source language variant - ALL ON ONE LINE -->
            <tuv>
                <xsl:attribute name="xml:lang">
                    <xsl:value-of select="ancestor::xliff:file/@source-language"/>
                </xsl:attribute>
                <seg>
                    <!-- Preserve inline elements WITHOUT namespaces -->
                    <xsl:apply-templates select="xliff:source/node()" mode="copy-content-no-namespace"/>
                </seg>
            </tuv>
            <xsl:text>&#10;</xsl:text>
            
            <!-- Target language variant - ALL ON ONE LINE -->
            <tuv>
                <xsl:attribute name="xml:lang">
                    <xsl:value-of select="ancestor::xliff:file/@target-language"/>
                </xsl:attribute>
                <!-- Capture all target attributes dynamically -->
                <xsl:for-each select="xliff:target/@*">
                    <xsl:choose>
                        <xsl:when test="namespace-uri() = 'http://www.w3.org/XML/1998/namespace'">
                            <xsl:attribute name="xml:{local-name()}">
                                <xsl:value-of select="."/>
                            </xsl:attribute>
                        </xsl:when>
                        <xsl:otherwise>
                            <xsl:attribute name="{name()}">
                                <xsl:value-of select="."/>
                            </xsl:attribute>
                        </xsl:otherwise>
                    </xsl:choose>
                </xsl:for-each>
                <seg>
                    <!-- Preserve inline elements WITHOUT namespaces -->
                    <xsl:apply-templates select="xliff:target/node()" mode="copy-content-no-namespace"/>
                </seg>
            </tuv>
            <xsl:text>&#10;</xsl:text>
        </tu>
        <xsl:text>&#10;</xsl:text>
    </xsl:template>
    
    <!-- Template to copy content with inline elements preserved BUT WITHOUT namespaces -->
    <xsl:template match="node()" mode="copy-content-no-namespace">
        <xsl:choose>
            <!-- For text nodes, just output the text -->
            <xsl:when test="self::text()">
                <xsl:value-of select="."/>
            </xsl:when>
            <!-- For elements, recreate them WITHOUT namespace -->
            <xsl:otherwise>
                <xsl:element name="{local-name()}">
                    <!-- Copy all attributes WITHOUT namespace prefixes -->
                    <xsl:for-each select="@*">
                        <xsl:choose>
                            <xsl:when test="namespace-uri() = 'http://www.w3.org/XML/1998/namespace'">
                                <xsl:attribute name="xml:{local-name()}">
                                    <xsl:value-of select="."/>
                                </xsl:attribute>
                            </xsl:when>
                            <xsl:otherwise>
                                <xsl:attribute name="{local-name()}">
                                    <xsl:value-of select="."/>
                                </xsl:attribute>
                            </xsl:otherwise>
                        </xsl:choose>
                    </xsl:for-each>
                    <!-- Recursively process child nodes -->
                    <xsl:apply-templates select="node()" mode="copy-content-no-namespace"/>
                </xsl:element>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>
    
</xsl:stylesheet>
