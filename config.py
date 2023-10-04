out_dir = "./out"
legs = dict(
    l13 = dict(
        url = 'https://app.parlamento.pt/webutils/docs/doc.xml?path=fjQQWCHFKukLz6%2bbYc8zWnKR4di7VFBCOk8cWazJzNDzUvPIooyr6w8vU9pCP9DqZMqpSka%2b9Ik3RzbaGvchuqH%2frymfDA0H7mqZpjEUqdZNCwJAoG5FzMak4RDOf0W8zD8guFj%2bbxuyua85OI0sTT2yMBmwdeQKSVeFo5sUTXxpY1OiOVg0zswwQsdJSiCwrEHGCLyXf3%2fWXdXAMEG538Ob5RNhl4mq2JkAwMDhoYCZPbMktDpNLoxfBZhsK0YzkOxbja7c%2b4%2fJqAJQ1%2f1hNLo%2fEoSy9fwEs2C3eQSy9KrKgDiWJlU3kzY1D1gTfSCNjSwFSFrN4XrXIUEuW6Oizq9x9PSxpvefpy%2fUA1DqW7A%3d&fich=IniciativasXIII.xml&Inline=true',
        extra_fields = ['BE', 'PCP' ,'PEV', 'Paulo Trigo Pereira (Ninsc)','PS', 'PAN', 'PSD','CDS-PP']),
    l14 = dict(
        url = 'https://app.parlamento.pt/webutils/docs/doc.xml?path=BpPefzltp4hl1vHGoH%2f4%2frnKjKVpQAanLYu0VOc7jD9CT5e0y06eFVuYNM92ewB7d2mgKLFjE3Phm%2b7fqnrLq1X9Acxrs4pPhZKZdRkCb7ckbUzr468DE8HPp3856az%2bVQ1%2bIePaiaQO86JML0zGm8PCom7rdvLSrqkQqrSB9vP2t6zN6L%2b90SrSKvuXdI5Qe5n%2ft4u6EMGRwlAcpsIkEOOVpG2NiididWND2l533pTtn7abqKWFYKnBtS63O1tHktXbM6h4szOsI%2fDcK%2fHPZ76qcVc3%2fAEmH2812ZEMrzVq7vMDGDJPoBrM1A9sMMFwR%2bM4MhwljzD8RYH2H5O2HajcEPIpbTa1m8glscXFZKsJkRT2MSvT%2fMcLq8ISAleJ&fich=IniciativasXIV.xml&Inline=true',
        extra_fields = ['BE', 'PCP', 'PEV', 'L', 'Joacine Katar Moreira (Ninsc)', 'PS', 'PAN','Cristina Rodrigues (Ninsc)','PSD','IL', 'CH']),
    l15 = dict(
        url = 'https://app.parlamento.pt/webutils/docs/doc.xml?path=xtvpkfG2pThOVQkLipwvvagL%2fixK8SGYd%2fALIEnc%2fp2H1v232J8LSqm%2f7j1hb8iYIp82MQoX%2fnKcthWrxGjG7qXR8fAp30gbm3%2fYNVs%2bsNlHlmFAF3JH%2f%2b9N9APW4cYYuw5bxwFBUkcQu1wNIh9DJTWdiwmA8aFDabzfz0TWmTt%2bG7G12mkCQLGEW3tyeuteFSLIL1gnT7Fy8to22KxF0%2fsNevTTceO4KdhIqc1t%2bCvdH%2f9wO3kmyYqPCdRWc1YRueA8PAaCuYsuuCc1jwxHO9JTlquKvqIbImFg5xVZ9gYkxUiw28XumjPEHuf9ki%2f%2fDjMWAAaFf6x6TFfmSsPAkHSyccdysKWiLVZo7EDVlb%2bwkISrb6uL3eumfUtpd1bk&fich=IniciativasXV.xml&Inline=true',
        extra_fields = ['BE', 'PCP', 'L', 'PS', 'PAN','PSD','IL', 'CH'])
    )

common_fields = ["data","ano","leg","Tipo","fase","iniNr","iniTipo","iniDescTipo","iniLeg","iniSel","dataInicioleg","dataFimleg","iniTitulo","iniTextoSubst","iniLinkTexto","iniEventos","iniAutorOutros","iniId","iniAutorGruposParlamentares","iniTextoSubstCampo","id","resultado","descricao","reuniao","tipoReuniao","ausencias","unanime"]
