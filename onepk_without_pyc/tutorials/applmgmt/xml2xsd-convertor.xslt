<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:cli_ext="http://www.cisco.com/onep/cli_ext:0.1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ext="http://exslt.org/common">
    <xsl:output method="text" indent="yes"/>
    <xsl:strip-space elements="*"/>
    <xsl:variable name="ns-uri" select="namespace-uri(/*[local-name()='application'])"/>
    <xsl:template match="/*[local-name()='application']">&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"  xmlns="<xsl:value-of select="//@app-namespace"/>:<xsl:value-of select="//@version"/>" xmlns:<xsl:value-of select="//@app-namespace-prefix"/>="<xsl:value-of select="//@app-namespace"/>:<xsl:value-of select="//@version"/>" xmlns:cli_ext="<xsl:value-of select="$ns-uri"/>" targetNamespace="<xsl:value-of select="//@app-namespace"/>:<xsl:value-of select="//@version"/>" elementFormDefault="qualified" attributeFormDefault="unqualified"  xml:lang="en"&gt;
    <xsl:call-template name="import"/>
    &lt;xs:element name="<xsl:value-of select="//@app-name"/>"&gt;
    &lt;xs:annotation&gt;
        &lt;xs:documentation&gt;<xsl:value-of select="//@description"/>&lt;/xs:documentation&gt;
    &lt;/xs:annotation&gt;
    &lt;xs:complexType&gt;
        &lt;xs:sequence&gt;
    
    <xsl:apply-templates select="*[local-name()='config-cmds']"/>
   
     &lt;xs:element name="exec" minOccurs="0"&gt;
        &lt;xs:complexType&gt;
            &lt;xs:sequence&gt;
                &lt;xs:choice maxOccurs="unbounded"&gt;
                <xsl:call-template name="node-info-cmd"/>
        <xsl:apply-templates select="*[local-name()='show-cmds']"/>
        <xsl:apply-templates select="*[local-name()='exec-cmds']"/>
                 &lt;/xs:choice&gt;
            &lt;/xs:sequence&gt;
        &lt;/xs:complexType&gt;
     &lt;/xs:element&gt;

        &lt;/xs:sequence&gt;
        &lt;xs:attribute name="version" use="optional" fixed="<xsl:value-of select="//@version"/>"/&gt;
        &lt;xs:attribute name="app-mode-prompt-prefix" use="optional" fixed="<xsl:value-of select="//@app-mode-prompt-prefix"/>"/&gt;
    &lt;/xs:complexType&gt;
    &lt;/xs:element&gt;
    <xsl:call-template name="node_info_type"/>
        <xsl:call-template name="key_param_with_restriction"/>
    &lt;/xs:schema&gt;
    </xsl:template>
    <!--start template config-cmds-->
    <xsl:template match="*[local-name()='config-cmds']">
     &lt;!--start config-cmds--&gt;
    &lt;xs:element name="config_data" minOccurs="0"&gt;
    &lt;xs:complexType&gt;
        &lt;xs:sequence&gt;
         <xsl:call-template name="onep-node-cmd"/>
            &lt;xs:choice minOccurs="0" maxOccurs="unbounded"&gt;
    <xsl:for-each select="*[local-name()='scalar-cmd']">
            <xsl:apply-templates select="."/>
        </xsl:for-each>
        <xsl:for-each select="*[local-name()='list-cmd']">
            <xsl:apply-templates select="."/>
        </xsl:for-each>
            &lt;/xs:choice&gt;
        &lt;/xs:sequence&gt;      
    &lt;/xs:complexType&gt;
    &lt;/xs:element&gt;
     &lt;!--end config-cmds--&gt;
</xsl:template>
    <!--end template config-cmds-->
    <!--start template show-cmds-->
    <xsl:template match="*[local-name()='show-cmds']">
     &lt;!--start show-cmds --&gt;
    <xsl:for-each select="*[local-name()='exec-cmd']">
    &lt;xs:element name="<xsl:value-of select="@name"/>" minOccurs="0"&gt;
    &lt;xs:complexType&gt;
        &lt;xs:sequence&gt;
        <xsl:call-template name="show-keyword"/>
            <xsl:apply-templates select="."/>
       
       &lt;/xs:sequence&gt;      
    &lt;/xs:complexType&gt;
     &lt;/xs:element&gt;  
    </xsl:for-each>
     &lt;!--end show-cmds --&gt;
</xsl:template>
    <!--end template show-cmds-->
    <!--start template exec-cmds-->
    <xsl:template match="*[local-name()='exec-cmds']">
     &lt;!--start exec-cmds--&gt;
    <xsl:for-each select="*[local-name()='exec-cmd']">
    &lt;xs:element name="<xsl:value-of select="@name"/>" minOccurs="0"&gt;
    &lt;xs:complexType&gt;
        &lt;xs:sequence&gt;
       <xsl:apply-templates select="."/>
       
       &lt;/xs:sequence&gt;      
    &lt;/xs:complexType&gt;
     &lt;/xs:element&gt;  
    </xsl:for-each>
     &lt;!--end exec-cmds--&gt;
</xsl:template>
    <!--end template exec-cmds-->
    <!--start template scalar-cmd-->
    <xsl:template match="*[local-name()='scalar-cmd']" name="scalar-cmd">
            &lt;xs:element name="<xsl:value-of select="@name"/>"&gt;
                &lt;xs:complexType&gt;
                    &lt;xs:sequence&gt;
                        <xsl:call-template name="no-cmd"/>
        <xsl:for-each select="*">
            <xsl:call-template name="keyword"/>
            <xsl:call-template name="param"/>
        </xsl:for-each>
        <!--start if scalar-cmd has mode -->
        <xsl:if test="*[local-name()='mode']">
                        
                          &lt;xs:choice minOccurs="0" maxOccurs="unbounded" &gt;
                         <xsl:for-each select="*[local-name()='mode']/*[local-name()='scalar-cmd']">
                <xsl:apply-templates select="."/>
            </xsl:for-each>
            <xsl:for-each select="*[local-name()='mode']/*[local-name()='list-cmd']">
                <xsl:apply-templates select="."/>
            </xsl:for-each>             
                        
                        &lt;/xs:choice&gt;
                         </xsl:if>
        <!--end if scalar-cmd has mode -->
                &lt;/xs:sequence&gt;
                <xsl:if test="*[local-name()='mode']">
                    &lt;xs:attribute name="mode_prompt" type="xs:string" default="<xsl:value-of select="*[local-name()='mode']/@mode-prompt"/>"/&gt;
                </xsl:if>
            &lt;/xs:complexType&gt;
        &lt;/xs:element&gt;
         
</xsl:template>
    <!--end template scalar-cmd-->
    <!--start template list-cmd -->
    <xsl:template match="*[local-name()='list-cmd']" name="list-cmd">
        &lt;!--start list-cmd <xsl:value-of select="@name"/>--&gt;
        &lt;xs:element name="<xsl:value-of select="@name"/>" maxOccurs="unbounded"&gt;
            &lt;xs:complexType&gt;
                &lt;xs:sequence&gt;
            <xsl:call-template name="no-cmd"/>
        <xsl:for-each select="*">
            <xsl:call-template name="keyword"/>
            <xsl:call-template name="key-param"/>
        </xsl:for-each>
        <!--start if list-cmd has mode -->
        <xsl:if test="*[local-name()='mode']">
              &lt;xs:choice minOccurs="0" maxOccurs="unbounded" &gt;
             <xsl:for-each select="*[local-name()='mode']/*[local-name()='scalar-cmd']">
                <xsl:apply-templates select="."/>
            </xsl:for-each>
            <xsl:for-each select="*[local-name()='mode']/*[local-name()='list-cmd']">
                <xsl:apply-templates select="."/>
            </xsl:for-each>             
            &lt;/xs:choice&gt;
             </xsl:if>
        <!--end if list-cmd has mode -->
                    &lt;/xs:sequence&gt;
                    <xsl:if test="*[local-name()='mode']">
                    &lt;xs:attribute name="mode_prompt" type="xs:string" default="<xsl:value-of select="*[local-name()='mode']/@mode-prompt"/>"/&gt;
                     </xsl:if>
                &lt;/xs:complexType&gt;
            &lt;/xs:element&gt;
      
        <!--</xsl:for-each>-->
        <!--&lt;/xs:choice&gt;-->
     &lt;!--end list-cmd <xsl:value-of select="@name"/>--&gt;
</xsl:template>
    <!--end template list-cmd-->
    <!--start template exec-cmd-->
    <xsl:template match="*[local-name()='exec-cmd']">
        <xsl:for-each select="*">
            <xsl:call-template name="keyword"/>
            <xsl:call-template name="param"/>
        </xsl:for-each>
    </xsl:template>
    <!--end template exec-cmd-->
    <!--start template no-cmd-->
    <xsl:template name="no-cmd">
        &lt;xs:element name="no" minOccurs="0"&gt;
            &lt;xs:annotation&gt;
                &lt;xs:documentation&gt;Negate a command or set a command's default&lt;/xs:documentation&gt;
            &lt;/xs:annotation&gt;
            &lt;xs:complexType/&gt;
        &lt;/xs:element&gt;
    </xsl:template>
    <!--end template no-cmd-->
    <!--start template show-cmd-->
    <xsl:template name="show-keyword">
        &lt;xs:element name="show"&gt;
            &lt;xs:annotation&gt;
                &lt;xs:documentation&gt;Show running system information&lt;/xs:documentation&gt;
            &lt;/xs:annotation&gt;
            &lt;xs:complexType/&gt;
        &lt;/xs:element&gt;
    </xsl:template>
    <!--end template no-cmd-->
    <xsl:template name="keyword" match="*[local-name()='keyword']">
        <xsl:if test="self::*[local-name()='keyword']">
        &lt;xs:element name="<xsl:value-of select="*[local-name()='name']"/>" <xsl:if test="@is-optional = 'true'">minOccurs="0"</xsl:if>&gt;
        <xsl:if test="*[local-name()='help'] !='' ">
            &lt;xs:annotation&gt;
                &lt;xs:documentation&gt;<xsl:value-of select="*[local-name()='help']"/>&lt;/xs:documentation&gt;
            &lt;/xs:annotation&gt;
        </xsl:if>
            &lt;xs:complexType/&gt;
         &lt;/xs:element&gt; 
        </xsl:if>
    </xsl:template>
    <xsl:template name="param" match="*[local-name()='param']">
        <xsl:if test="self::*[local-name()='param']">
        &lt;xs:element name="<xsl:value-of select="*[local-name()='name']"/>"<xsl:if test=" count(*[local-name()='type']/*/*) = 0"> type="<xsl:apply-templates select="*[local-name()='type']"/>"</xsl:if>
            <xsl:if test="@is-optional = 'true'"> minOccurs="0"</xsl:if>&gt;
        <xsl:if test="*[local-name()='help'] !='' ">
            &lt;xs:annotation&gt;
                &lt;xs:documentation&gt;<xsl:value-of select="*[local-name()='help']"/>&lt;/xs:documentation&gt;
            &lt;/xs:annotation&gt; 
        </xsl:if>
            <xsl:if test="count(*[local-name()='type']/*/*) > 0">
                <xsl:apply-templates select="*[local-name()='type']"/>
            </xsl:if>
         &lt;/xs:element&gt; 
         </xsl:if>
    </xsl:template>
    <xsl:template name="key-param">
        <xsl:if test="self::*[local-name()='param']">
            &lt;xs:element name="<xsl:value-of select="*[local-name()='name']"/>"&gt;
             <xsl:if test="*[local-name()='help'] !='' ">
                &lt;xs:annotation&gt;
                    &lt;xs:documentation&gt;<xsl:value-of select="*[local-name()='help']"/>&lt;/xs:documentation&gt;
                &lt;/xs:annotation&gt;
           </xsl:if>
            <xsl:choose>
                <xsl:when test="count(*[local-name()='type']/*/*) > 0">
                &lt;xs:complexType&gt;
                    &lt;xs:simpleContent&gt;
                    <xsl:for-each select="*[local-name()='type']">
                        &lt;xs:restriction base="<xsl:value-of select="../../@name"/>_<xsl:value-of select="../*[local-name()='name']"/>_key"&gt;
                            <xsl:call-template name="type_restriction"/>
                        &lt;/xs:restriction&gt;
                        </xsl:for-each>
                    &lt;/xs:simpleContent&gt;
                &lt;/xs:complexType&gt;                
                </xsl:when>
                <xsl:otherwise>
                &lt;xs:complexType&gt;
                    &lt;xs:simpleContent&gt;
                        &lt;xs:extension base="<xsl:apply-templates select="*[local-name()='type']"/>"&gt;
                            &lt;xs:attribute name="key" type="xs:boolean" fixed="true"/&gt;
                        &lt;/xs:extension&gt;
                    &lt;/xs:simpleContent&gt;
                &lt;/xs:complexType&gt;
                </xsl:otherwise>
            </xsl:choose>
       &lt;/xs:element&gt; 
           </xsl:if>
    </xsl:template>
    <xsl:template name="import">
    &lt;xs:import namespace="<xsl:value-of select="$ns-uri"/>" schemaLocation="<xsl:call-template name="schemaLocation"/>"/&gt;  
    &lt;xs:annotation&gt;
        &lt;xs:appinfo&gt;xslt version 0.1&lt;/xs:appinfo&gt;
        &lt;xs:documentation&gt;
      This schema was by cli-extension ssl.
    &lt;/xs:documentation&gt;
    &lt;/xs:annotation&gt;
    </xsl:template>
    <xsl:template name="onep-node-cmd">
    
    &lt;xs:element name="node_info_cmd" minOccurs="0"&gt;
        &lt;xs:complexType&gt;
            &lt;xs:sequence&gt;
            
                <xsl:call-template name="no-cmd"/>
                
                &lt;xs:element name="node_info" type="node_info_type" /&gt;
              
            &lt;/xs:sequence&gt;
        &lt;/xs:complexType&gt;
    &lt;/xs:element&gt;
    </xsl:template>
    <xsl:template name="node-info-cmd">
                        &lt;xs:element name="node_info" type="node_info_type"/&gt;

    </xsl:template>
    <xsl:template name="node_info_type">
    &lt;xs:complexType name="node_info_type"&gt;
        &lt;xs:sequence&gt;
            &lt;xs:element name="v<xsl:value-of select="//@version"/>"&gt;
                &lt;xs:annotation&gt;
                    &lt;xs:documentation&gt;application version&lt;/xs:documentation&gt;
                &lt;/xs:annotation&gt;
                &lt;xs:complexType/&gt;
            &lt;/xs:element&gt;
       
           &lt;xs:element name="config-domain" type="xs:string"&gt;
                &lt;xs:annotation&gt;
                    &lt;xs:documentation&gt;Identifies where the application is running&lt;/xs:documentation&gt;
                &lt;/xs:annotation&gt;
            &lt;/xs:element&gt;
            
            &lt;xs:element name="instance-name" type="xs:string" minOccurs="0"&gt;
                &lt;xs:annotation&gt;
                    &lt;xs:documentation&gt;instance name&lt;/xs:documentation&gt;
                &lt;/xs:annotation&gt;
            &lt;/xs:element&gt;
        &lt;/xs:sequence&gt;
    &lt;/xs:complexType&gt;
    
    </xsl:template>
    <xsl:template name="simple-type">
        <xsl:choose>
            <xsl:when test="*[local-name()='string']">xs:string</xsl:when>
            <xsl:when test="*[local-name()='integer']">xs:int</xsl:when>
            <xsl:when test="*[local-name()='ipv4-address']">cli_ext:ipv4-address</xsl:when>
            <xsl:when test="*[local-name()='ipv6-address']">cli_ext:ipv6-address</xsl:when>
            <xsl:when test="*[local-name()='ipv4-mask']">cli_ext:ipv4-mask</xsl:when>
            <xsl:when test="*[local-name()='ipv6-mask']">cli_ext:ipv6-mask</xsl:when>
        </xsl:choose>
    </xsl:template>
    <xsl:template match="*[local-name()='type']">
        <xsl:choose>
            <xsl:when test="count(*/*) > 0">
            &lt;xs:simpleType&gt;
                &lt;xs:restriction base="<xsl:call-template name="simple-type"/>"&gt;
                <xsl:call-template name="type_restriction"/>
                &lt;/xs:restriction&gt;
            &lt;/xs:simpleType&gt;
            </xsl:when>
            <xsl:otherwise>
                <xsl:call-template name="simple-type"/>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>
    <xsl:template name="type_restriction">
        <xsl:choose>
            <xsl:when test="*[local-name()='string']/*[local-name()='pattern']">&lt;xs:pattern value="<xsl:value-of select="*[local-name()='string']/*[local-name()='pattern']"/>"/&gt;</xsl:when>
            <xsl:when test="*[local-name()='integer']">
                <xsl:for-each select="*[local-name()='integer']/*">
                    <xsl:choose>
                        <xsl:when test="local-name()='min'">&lt;xs:minInclusive value="<xsl:value-of select="."/>"/&gt;</xsl:when>
                        <xsl:when test="local-name()='max'">&lt;xs:maxInclusive value="<xsl:value-of select="."/>"/&gt;</xsl:when>
                    </xsl:choose>
                </xsl:for-each>
            </xsl:when>
        </xsl:choose>
    </xsl:template>
    <xsl:template name="key_param_with_restriction">
        <xsl:for-each select="//*[local-name()='list-cmd']/*[local-name()='param']/*[local-name()='type']">
            <xsl:if test="count(*/*) > 0 ">
    &lt;xs:complexType name="<xsl:value-of select="../../@name"/>_<xsl:value-of select="../*[local-name()='name']"/>_key"&gt;
        &lt;xs:simpleContent&gt;
            &lt;xs:extension base="<xsl:call-template name="simple-type"/>"&gt;
                &lt;xs:attribute name="key" type="xs:boolean" fixed="true"/&gt;
            &lt;/xs:extension&gt;
        &lt;/xs:simpleContent&gt;
    &lt;/xs:complexType&gt;
    </xsl:if>
        </xsl:for-each>
    </xsl:template>
    <xsl:template name="schemaLocation">
        <xsl:choose>
            <xsl:when test="string-length(//@xsi:schemaLocation) > string-length($ns-uri)">
                <xsl:value-of select="substring(//@xsi:schemaLocation, string-length($ns-uri)+2)"/>
            </xsl:when>
            <xsl:otherwise>
                <xsl:value-of select="//@xsi:schemaLocation"/>
            </xsl:otherwise>
        </xsl:choose>
    </xsl:template>
</xsl:stylesheet>
