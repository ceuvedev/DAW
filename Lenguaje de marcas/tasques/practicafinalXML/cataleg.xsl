<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="/">
        <html>
            <head>
                <meta charset="UTF-8"/>
                <title>Catálogo de Productos</title>
                <link rel="stylesheet" href="style.css"/>
            </head>
            <body>
                <h1>Catálogo de Productos</h1>
                <xsl:for-each select="//plataforma">
                    <xsl:sort select="@nombre"/>
                    <h2><xsl:value-of select="@nombre"/></h2>
                    <table>
                        <thead>
                            <tr>
                                <th>Producto</th>
                                <th>Precio</th>
                                <th>Estado</th>
                            </tr>
                        </thead>
                        <tbody>
                            <xsl:for-each select="producto">
                                <xsl:sort select="precio" data-type="number"/>
                                <tr>
                                    <td><xsl:value-of select="nombre"/></td>
                                    <td><xsl:value-of select="precio"/>€</td>
                                    <td>
                                        <xsl:choose>
                                            <xsl:when test="stock = '0'">
                                                <span class="agotado">Agotado</span>
                                            </xsl:when>
                                            <xsl:otherwise>
                                                <span class="disponible">Disponible</span>
                                            </xsl:otherwise>
                                        </xsl:choose>
                                    </td>
                                </tr>
                            </xsl:for-each>
                        </tbody>
                    </table>
                </xsl:for-each>
            </body>
        </html>
    </xsl:template>

</xsl:stylesheet>
