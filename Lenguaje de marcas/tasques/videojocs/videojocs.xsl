<?xml version="1.0" encoding="UTF-8"?>
   <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
        <xsl:output method="html"/>

        <xsl: template match="/pizzes">
            <html>
               <head>
                   <title>Menu de videjocs</title>
               </head>
               <body>
                   <h2>Taula</h2>
                   <table border="1">
                       <tr>
                           <th>Titol</th>
                           <th>Plataforma</th>
                           <th>Any</th>
                           <th>Preu</th>
                       </tr>
                       <!-- Iteració sobre cada element "pizza" -->
                       <xsl:for-each select="pizza">
                           <tr>
                               <td><xsl:value-of select="titulo"/></td>
                               <td><xsl:value-of select="plataforma"/></td>
                               <td><xsl:value-of select="any"/></td>
                               <td><xsl:value-of select="precio"/></td>
                           </tr>
                       </xsl:for-each>
                   </table>
               </body>
           </html>
        </xsl:template>
    </xsl:stylesheet>
