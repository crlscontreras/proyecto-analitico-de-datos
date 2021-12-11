
def region(codigo):
    nombreR = 'Sin información'
    if(codigo == '1'):
        nombreR = 'Región de Tarapacá'
    if(codigo == '2'):
        nombreR = 'Región de Antofagasta'
    if(codigo == '3'):
        nombreR = 'Región de Atacama'
    if(codigo == '4'):
        nombreR = 'Región de Coquimbo'
    if(codigo == '5'):
        nombreR = 'Región de Valparaíso'
    if(codigo == '6'):
        nombreR = "Region del libertador Gral. Bernardo O''Higgins"
    if(codigo == '7'):
        nombreR = 'Región del Maule'
    if(codigo == '8'):
        nombreR = 'Región del Biobío'
    if(codigo == '9'):
        nombreR = 'Región de la Araucanía'
    if(codigo == '10'):
        nombreR = 'Región de Los Lagos'
    if(codigo == '11'):
        nombreR = 'Región de Aysen'
    if(codigo == '12'):
        nombreR = 'Región de Magallanes y de la Antártica Chilena'
    if(codigo == '13'):
        nombreR = 'Región Metropolitana de Santiago'
    if(codigo == '14'):
        nombreR = 'Región de Los Ríos'
    if(codigo == '15'):
        nombreR = 'Región de Arica y Parinacota'
    if(codigo == '16'):
        nombreR = 'Región de Ñuble'
    if(codigo == '0'):
        nombreR = 'Sin información'    
    return nombreR

def provincias(codigo):
    nombreProvincia = 'Sin información' 
    if(codigo == '151'):
        nombreProvincia = 'Arica'
    if(codigo == '152'):
        nombreProvincia = 'Parinacota'
    if(codigo == '11'):
        nombreProvincia = 'Iquique'
    if(codigo == '14'):
        nombreProvincia = 'Tamarugal'
    if(codigo == '21'):
        nombreProvincia = 'Antofagasta'
    if(codigo == '22'):
        nombreProvincia = 'El Loa'
    if(codigo == '23'):
        nombreProvincia = 'Tocopilla'
    if(codigo == '31'):
        nombreProvincia = 'Copiapo'
    if(codigo == '32'):
        nombreProvincia = 'Chanaral'
    if(codigo == '33'):
        nombreProvincia = 'Huasco'
    if(codigo == '41'):
        nombreProvincia = 'Elqui'
    if(codigo == '42'):
        nombreProvincia = 'Choapa'
    if(codigo == '43'):
        nombreProvincia = 'Limari'
    if(codigo == '51'):
        nombreProvincia = 'Valparaiso'
    if(codigo == '52'):
        nombreProvincia = 'Isla de Pascua'
    if(codigo == '53'):
        nombreProvincia = 'Los Andes'
    if(codigo == '54'):
        nombreProvincia = 'Petorca'
    if(codigo == '55'):
        nombreProvincia = 'Quillota'
    if(codigo == '56'):
        nombreProvincia = 'San Antonio'
    if(codigo == '57'):
        nombreProvincia = 'San Felipe de Aconcagua'
    if(codigo == '58'):
        nombreProvincia = 'Marga Marga'
    if(codigo == '61'):
        nombreProvincia = 'Cachapoal'
    if(codigo == '62'):
        nombreProvincia = 'Cardenal Caro'
    if(codigo == '63'):
        nombreProvincia = 'Colchagua'
    if(codigo == '71'):
        nombreProvincia = 'Talca'
    if(codigo == '72'):
        nombreProvincia = 'Cauquenes'
    if(codigo == '73'):
        nombreProvincia = 'Curico'
    if(codigo == '74'):
        nombreProvincia = 'Linares'
    if(codigo == '81'):
        nombreProvincia = 'Concepcion'
    if(codigo == '82'):
        nombreProvincia = 'Arauco'
    if(codigo == '83'):
        nombreProvincia = 'Biobio'
    if(codigo == '84'):
        nombreProvincia = 'Ñuble'
    if(codigo == '91'):
        nombreProvincia = 'Cautin'
    if(codigo == '92'):
        nombreProvincia = 'Malleco'
    if(codigo == '141'):
        nombreProvincia = 'Valdivia'
    if(codigo == '142'):
        nombreProvincia = 'Ranco'
    if(codigo == '101'):
        nombreProvincia = 'Llanquihue'
    if(codigo == '102'):
        nombreProvincia = 'Chiloe'
    if(codigo == '103'):
        nombreProvincia = 'Osorno'
    if(codigo == '104'):
        nombreProvincia = 'Palena'
    if(codigo == '111'):
        nombreProvincia = 'Coihaique'
    if(codigo == '112'):
        nombreProvincia = 'Aisen'
    if(codigo == '113'):
        nombreProvincia = 'Capitan Prat'
    if(codigo == '114'):
        nombreProvincia = 'General Carrera'
    if(codigo == '121'):
        nombreProvincia = 'Magallanes'
    if(codigo == '122'):
        nombreProvincia = 'Antartica Chilena'
    if(codigo == '123'):
        nombreProvincia = 'Tierra del Fuego'
    if(codigo == '124'):
        nombreProvincia = 'Ultima Esperanza'
    if(codigo == '131'):
        nombreProvincia = 'Santiago'
    if(codigo == '132'):
        nombreProvincia = 'Cordillera'
    if(codigo == '133'):
        nombreProvincia = 'Chacabuco'
    if(codigo == '134'):
        nombreProvincia = 'Maipo'
    if(codigo == '135'):
        nombreProvincia = 'Melipilla'
    if(codigo == '136'):
        nombreProvincia = 'Talagante'
    if(codigo == '0'):
        nombreProvincia = 'Sin información'    
    return nombreProvincia


def depe(codigo):
    nombreDepe = 'nope'
    if(codigo == '1'):
        nombreDepe = 'Corporación Municipal'
    if(codigo == '2'):
        nombreDepe = 'Municipal DAEM'
    if(codigo == '3'):
        nombreDepe = 'Particular Subvencionado'
    if(codigo == '4'):
        nombreDepe = 'Particular Pagado (o no subvencionado)'
    if(codigo == '5'):
        nombreDepe = 'Corporación de Administración Delegada (DL 3166)'
    if(codigo == '6'):
        nombreDepe = 'Servicio Local de Educación'
    return nombreDepe

def estadoEstab(codigo):
    nombreEstado = 'nope'
    if(codigo == '1'):
        nombreEstado = 'Funcionando'
    if(codigo == '2'):
        nombreEstado = 'En receso'
    if(codigo == '3'):
        nombreEstado = 'Cerrado'
    if(codigo == '4'):
        nombreEstado = 'Autorizado sin matrícula'
    if(codigo == '0'):
        nombreEstado = 'Sin información'    
    return nombreEstado

def ense(codigo):
    nombreEnse = 'nope'
    if(codigo == '0'):
        nombreEnse = 'Sin información'
    if(codigo == '110'):
        nombreEnse = 'Enseñanza Básica'
    if(codigo == '160'):
        nombreEnse = 'Educación Básica Común Adultos (Decreto 584/2007)'
    if(codigo == '161'):
        nombreEnse = 'Educación Básica Especial Adultos'
    if(codigo == '163'):
        nombreEnse = 'Escuelas Cárceles (Básica Adultos)'
    if(codigo == '165'):
        nombreEnse = 'Educación Básica Adultos Sin Oficios (Decreto 584/2007)'
    if(codigo == '167'):
        nombreEnse = 'Educación Básica Adultos Con Oficios (Decreto 584/2007 y 999/2009)'
    if(codigo == '310'):
        nombreEnse = 'Enseñanza Media H-C niños y jóvenes'
    if(codigo == '360'):
        nombreEnse = 'Educación Media H-C adultos vespertino y nocturno (Decreto N°190/1975)'
    if(codigo == '361'):
        nombreEnse = 'Educación Media H-C adultos (Decreto N° 12/1987)'
    if(codigo == '362'):
        nombreEnse = 'Escuelas Cárceles (Media Adultos)'
    if(codigo == '363'):
        nombreEnse = 'Educación Media H-C Adultos (Decreto N°1000/2009)'
    if(codigo == '410'):
        nombreEnse = 'Enseñanza Media T-P Comercial Niños y Jóvenes'
    if(codigo == '460'):
        nombreEnse = 'Educación Media T-P Comercial Adultos (Decreto N° 152/1989)'
    if(codigo == '461'):
        nombreEnse = 'Educación Media T-P Comercial Adultos (Decreto N° 152/1989)'
    if(codigo == '463'):
        nombreEnse = 'Educación Media T-P Comercial Adultos (Decreto N° 1000/2009)'
    if(codigo == '510'):
        nombreEnse = 'Enseñanza Media T-P Industrial Niños y Jóvenes'
    if(codigo == '560'):
        nombreEnse = 'Educación Media T-P Industrial Adultos (Decreto N° 152/1989)'
    if(codigo == '561'):
        nombreEnse = 'Educación Media T-P Industrial Adultos (Decreto N° 152/1989)'
    if(codigo == '563'):
        nombreEnse = 'Educación Media T-P Industrial Adultos (Decreto N° 1000/2009)'
    if(codigo == '610'):
        nombreEnse = 'Enseñanza Media T-P Técnica Niños y Jóvenes'
    if(codigo == '660'):
        nombreEnse = 'Educación Media T-P Técnica Adultos (Decreto N° 152/1989)'
    if(codigo == '661'):
        nombreEnse = 'Educación Media T-P Técnica Adultos (Decreto N° 152/1989)'
    if(codigo == '663'):
        nombreEnse = 'Educación Media T-P Técnica Adultos (Decreto N° 1000/2009)'
    if(codigo == '710'):
        nombreEnse = 'Enseñanza Media T-P Agrícola Niños y Jóvenes'
    if(codigo == '760'):
        nombreEnse = 'Educación Media T-P Agrícola Adultos (Decreto N° 152/1989)'
    if(codigo == '761'):
        nombreEnse = 'Educación Media T-P Agrícola Adultos (Decreto N° 152/1989)'
    if(codigo == '763'):
        nombreEnse = 'Educación Media T-P Agrícola Adultos (Decreto N° 1000/2009)'
    if(codigo == '810'):
        nombreEnse = 'Enseñanza Media T-P Marítima Niños y Jóvenes'
    if(codigo == '860'):
        nombreEnse = 'Enseñanza Media T-P Marítima Adultos (Decreto N° 152/1989)'
    if(codigo == '861'):
        nombreEnse = 'Sin información'
    if(codigo == '863'):
        nombreEnse = 'Enseñanza Media T-P Marítima Adultos (Decreto N° 1000/2009)'
    if(codigo == '910'):
        nombreEnse = 'Enseñanza Media Artística Niños y Jóvenes'
    if(codigo == '963'):
        nombreEnse = 'Enseñanza Media Artística Adultos'
    return nombreEnse

def ense2(codigo):
    nombreEnse2 = 'nope'
    if(codigo == '2'):
        nombreEnse2 = 'Enseñanza Básica Niños.'
    if(codigo == '3'):
        nombreEnse2 = 'Educación Básica Adultos.'
    if(codigo == '5'):
        nombreEnse2 = 'Enseñanza Media Humanístico Científica Jóvenes.'
    if(codigo == '6'):
        nombreEnse2 = 'Educación Media Humanístico Científica Adultos.'
    if(codigo == '7'):
        nombreEnse2 = 'Enseñanza Media Técnico Profesional y Artística, Jóvenes.'
    if(codigo == '8'):
        nombreEnse2 = 'Educación Media Técnico Profesional y Artística, Adultos.'
    if(codigo == '0'):
        nombreEnse2 = 'Sin información'   
    if(codigo == '1'):
        nombreEnse2 = 'Sin información'        
    return nombreEnse2

def proRBD(codigoPro):
    nombrePro = 'nope'
    if(codigoPro == '11'):
        nombrePro = 'Provincia de Iquique'
    if(codigoPro == '14'):
        nombrePro = 'Provincia del Tamarugal'    
    if(codigoPro == '21'):
        nombrePro = 'Provincia de Antofagasta'
    if(codigoPro == '22'):
        nombrePro = 'Provincia de El Loa'
    if(codigoPro == '23'):
        nombrePro = 'Provincia de Tocopilla'
    if(codigoPro == '31'):
        nombrePro = 'Provincia de Copiapó'
    if(codigoPro == '32'):
        nombrePro = 'Provincia de Chañaral'
    if(codigoPro == '33'):
        nombrePro = 'Provincia de Huasco'
    if(codigoPro == '41'):
        nombrePro = 'Provincia de Elqui'
    if(codigoPro == '42'):
        nombrePro = 'Provincia de Choapa'
    if(codigoPro == '43'):
        nombrePro = 'Provincia de Limarí'
    if(codigoPro == '51'):
        nombrePro = 'Provincia de Valparaíso'
    if(codigoPro == '52'):
        nombrePro = 'Provincia de Isla de Pascua'
    if(codigoPro == '53'):
        nombrePro = 'Provincia de Los Andes'
    if(codigoPro == '54'):
        nombrePro = 'Provincia de Petorca'
    if(codigoPro == '55'):
        nombrePro = 'Provincia de Quillota'
    if(codigoPro == '56'):
        nombrePro = 'Provincia de San Antonio'
    if(codigoPro == '57'):
        nombrePro = 'Provincia de San Felipe de Aconcagua'
    if(codigoPro == '58'):
        nombrePro = 'Provincia de Marga Marga'
    if(codigoPro == '61'):
        nombrePro = 'Provincia de Cachapoal'
    if(codigoPro == '62'):
        nombrePro = 'Provincia de Cardenal Caro'
    if(codigoPro == '63'):
        nombrePro = 'Provincia de Colchagua'
    if(codigoPro == '71'):
        nombrePro = 'Provincia de Talca'
    if(codigoPro == '72'):
        nombrePro = 'Provincia de Cauquenes'
    if(codigoPro == '73'):
        nombrePro = 'Provincia de Curicó'
    if(codigoPro == '74'):
        nombrePro = 'Provincia de Linares'
    if(codigoPro == '81'):
        nombrePro = 'Provincia de Concepción'
    if(codigoPro == '82'):
        nombrePro = 'Provincia de Arauco'
    if(codigoPro == '83'):
        nombrePro = 'Provincia de Biobío'
    if(codigoPro == '84'):
        nombrePro = 'Provincia de Ñuble'
    if(codigoPro == '91'):
        nombrePro = 'Provincia de Cautín'
    if(codigoPro == '92'):
        nombrePro = 'Provincia de Malleco'
    if(codigoPro == '101'):
        nombrePro = 'Provincia de Llanquihue'
    if(codigoPro == '102'):
        nombrePro = 'Provincia de Chiloé'
    if(codigoPro == '103'):
        nombrePro = 'Provincia de Osorno'
    if(codigoPro == '104'):
        nombrePro = 'Provincia de Palena'
    if(codigoPro == '111'):
        nombrePro = 'Provincia de Coyhaique'
    if(codigoPro == '112'):
        nombrePro = 'Provincia de Aysén'
    if(codigoPro == '113'):
        nombrePro = 'Provincia de Capitán Prat'
    if(codigoPro == '114'):
        nombrePro = 'Provincia de General Carrera'
    if(codigoPro == '121'):
        nombrePro = 'Provincia de Magallanes'
    if(codigoPro == '122'):
        nombrePro = 'Provincia de Antártica Chilena'
    if(codigoPro == '123'):
        nombrePro = 'Provincia de Tierra del Fuego'
    if(codigoPro == '124'):
        nombrePro = 'Provincia de Última Esperanza'
    if(codigoPro == '131'):
        nombrePro = 'Provincia de Santiago'
    if(codigoPro == '132'):
        nombrePro = 'Provincia de Cordillera'
    if(codigoPro == '133'):
        nombrePro = 'Provincia de Chacabuco'
    if(codigoPro == '134'):
        nombrePro = 'Provincia de Maipo'
    if(codigoPro == '135'):
        nombrePro = 'Provincia de Melipilla'
    if(codigoPro == '136'):
        nombrePro = 'Provincia de Talagante'
    if(codigoPro == '141'):
        nombrePro = 'Provincia de Valdivia'
    if(codigoPro == '142'):
        nombrePro = 'Provincia de Ranco'
    if(codigoPro == '151'):
        nombrePro = 'Provincia de Arica'
    if(codigoPro == '152'):
        nombrePro = 'Provincia de Parinacota'
    if(codigoPro == '161'):
        nombrePro = 'Provincia de Diguillin'
    if(codigoPro == '162'):
        nombrePro = 'Provincia de Itata'
    if(codigoPro == '163'):
        nombrePro = 'Provincia de Punilla'
    if(codigoPro == '0'):
        nombrePro = 'Sin información'    
    return nombrePro

def gradp(codigoEnse,codigoG):
    nombreGrado = 'nope'
    if(codigoEnse == '110' and codigoG == '1'):
        nombreGrado = '1º Básico'
    if(codigoEnse == '110' and codigoG == '2'):
        nombreGrado = '2º Básico'
    if(codigoEnse == '110' and codigoG == '3'):
        nombreGrado = '3º Básico'
    if(codigoEnse == '110' and codigoG == '4'):
        nombreGrado = '4º Básico'
    if(codigoEnse == '110' and codigoG == '5'):
        nombreGrado = '5º Básico'
    if(codigoEnse == '110' and codigoG == '6'):
        nombreGrado = '6º Básico'
    if(codigoEnse == '110' and codigoG == '7'):
        nombreGrado = '7º Básico'
    if(codigoEnse == '110' and codigoG == '8'):
        nombreGrado = '8º Básico'
    
    if(codigoEnse == '160' and codigoG == '1'):
        nombreGrado = '1º Alfabetización'
    if(codigoEnse == '160' and codigoG == '2'):
        nombreGrado = 'Nivel Básico 1 (1º a 4º básico)'
    if(codigoEnse == '160' and codigoG == '3'):
        nombreGrado = 'Nivel Básico 2 (5º a 6º básico)'
    if(codigoEnse == '160' and codigoG == '4'):
        nombreGrado = 'Nivel Básico 3 (7º a 8º básico)'
    if(codigoEnse == '160' and codigoG == '5'):
        nombreGrado = 'Nivel Técnico'
    
    if(codigoEnse == '161' and codigoG == '1'):
        nombreGrado = 'Alfabetización'
    if(codigoEnse == '161' and codigoG == '2'):
        nombreGrado = 'Nivel Básico 1 (1º a 4º básico)'
    if(codigoEnse == '161' and codigoG == '3'):
        nombreGrado = 'Nivel Básico 2 (5º a 6º básico)'
    if(codigoEnse == '161' and codigoG == '4'):
        nombreGrado = 'Nivel Básico 3 (7º a 8º básico)'
    if(codigoEnse == '161' and codigoG == '5'):
        nombreGrado = 'Nivel Técnico'
        
    if(codigoEnse == '163' and codigoG == '1'):
        nombreGrado = 'Alfabetización'
    if(codigoEnse == '163' and codigoG == '2'):
        nombreGrado = 'Nivel Básico 1 (1º a 4º básico)'
    if(codigoEnse == '163' and codigoG == '3'):
        nombreGrado = 'Nivel Básico 2 (5º a 6º básico)'
    if(codigoEnse == '163' and codigoG == '4'):
        nombreGrado = 'Nivel Básico 3 (7º a 8º básico)'
    if(codigoEnse == '163' and codigoG == '5'):
        nombreGrado = 'Nivel Técnico'

    if(codigoEnse == '165' and codigoG == '1'):
        nombreGrado = 'Nivel Básico 1 (1º a 4º básico)'
    if(codigoEnse == '165' and codigoG == '2'):
        nombreGrado = 'Nivel Básico 2 (5º a 6º básico)'
    if(codigoEnse == '165' and codigoG == '3'):
        nombreGrado = 'Nivel Básico 3 (7º a 8º básico)'

    if(codigoEnse == '167' and codigoG == '2'):
        nombreGrado = 'Nivel Básico 2 (5º a 6º básico)'
    if(codigoEnse == '167' and codigoG == '3'):
        nombreGrado = 'Nivel Básico 3 (7º a 8º básico)'

    if(codigoEnse == '310' and codigoG == '1'):
        nombreGrado = '1º medio'
    if(codigoEnse == '310' and codigoG == '2'):
        nombreGrado = '2º medio'
    if(codigoEnse == '310' and codigoG == '3'):
        nombreGrado = '3º medio'
    if(codigoEnse == '310' and codigoG == '4'):
        nombreGrado = '4º medio'

    if(codigoEnse == '360' and codigoG == '1'):
        nombreGrado = '1º medio'
    if(codigoEnse == '360' and codigoG == '2'):
        nombreGrado = '2º medio'
    if(codigoEnse == '360' and codigoG == '3'):
        nombreGrado = '3º medio'
    if(codigoEnse == '360' and codigoG == '4'):
        nombreGrado = '4º medio'

    if(codigoEnse == '361' and codigoG == '1'):
        nombreGrado = 'Primer ciclo (1º y 2º medio)'
    if(codigoEnse == '361' and codigoG == '3'):
        nombreGrado = 'Segundo ciclo (3º y 4º medio)'

    if(codigoEnse == '363' and codigoG == '1'):
        nombreGrado = 'Primer nivel (1º y 2º medio)'
    if(codigoEnse == '363' and codigoG == '3'):
        nombreGrado = 'Segundo nivel (3º y 4º medio)'

    if(codigoEnse == '410' and codigoG == '1'):
        nombreGrado = '1º medio'
    if(codigoEnse == '410' and codigoG == '2'):
        nombreGrado = '2º medio'
    if(codigoEnse == '410' and codigoG == '3'):
        nombreGrado = '3º medio'
    if(codigoEnse == '410' and codigoG == '4'):
        nombreGrado = '4º medio'

    if(codigoEnse == '460' and codigoG == '1'):
        nombreGrado = 'Primer ciclo (1º y 2º medio)'
    if(codigoEnse == '460' and codigoG == '3'):
        nombreGrado = '3º medio'
    if(codigoEnse == '460' and codigoG == '4'):
        nombreGrado = '4º medio'

    if(codigoEnse == '461' and codigoG == '1'):
        nombreGrado = 'Primer ciclo (1º y 2º medio)'
    if(codigoEnse == '461' and codigoG == '3'):
        nombreGrado = '3º medio'
    if(codigoEnse == '461' and codigoG == '4'):
        nombreGrado = '4º medio'

    if(codigoEnse == '463' and codigoG == '1'):
        nombreGrado = 'Primer nivel (1º y 2º medio)'
    if(codigoEnse == '463' and codigoG == '3'):
        nombreGrado = 'Segundo nivel (3º medio)'
    if(codigoEnse == '463' and codigoG == '4'):
        nombreGrado = 'Tercero nivel (4º medio)'

    if(codigoEnse == '510' and codigoG == '1'):
        nombreGrado = '1º medio'
    if(codigoEnse == '510' and codigoG == '2'):
        nombreGrado = '2º medio'
    if(codigoEnse == '510' and codigoG == '3'):
        nombreGrado = '3º medio'
    if(codigoEnse == '510' and codigoG == '4'):
        nombreGrado = '4º medio'

    if(codigoEnse == '560' and codigoG == '1'):
        nombreGrado = 'Primer ciclo (1º y 2º medio)'
    if(codigoEnse == '560' and codigoG == '3'):
        nombreGrado = '3º medio'
    if(codigoEnse == '560' and codigoG == '4'):
        nombreGrado = '4º medio'

    if(codigoEnse == '561' and codigoG == '1'):
        nombreGrado = 'Primer ciclo (1º y 2º medio)'
    if(codigoEnse == '561' and codigoG == '3'):
        nombreGrado = '3º medio'
    if(codigoEnse == '561' and codigoG == '4'):
        nombreGrado = '4º medio'

    if(codigoEnse == '563' and codigoG == '1'):
        nombreGrado = 'Primer nivel (1º y 2º medio)'
    if(codigoEnse == '563' and codigoG == '3'):
        nombreGrado = 'Segundo nivel (3º medio)'
    if(codigoEnse == '563' and codigoG == '4'):
        nombreGrado = 'Tercero nivel (4º medio)'

    if(codigoEnse == '610' and codigoG == '1'):
        nombreGrado = '1º medio'
    if(codigoEnse == '610' and codigoG == '2'):
        nombreGrado = '2º medio'
    if(codigoEnse == '610' and codigoG == '3'):
        nombreGrado = '3º medio'
    if(codigoEnse == '610' and codigoG == '4'):
        nombreGrado = '4º medio'

    if(codigoEnse == '660' and codigoG == '1'):
        nombreGrado = 'Primer ciclo (1º y 2º medio)'
    if(codigoEnse == '660' and codigoG == '3'):
        nombreGrado = '3º medio'
    if(codigoEnse == '660' and codigoG == '4'):
        nombreGrado = '4º medio'

    if(codigoEnse == '661' and codigoG == '1'):
        nombreGrado = 'Primer ciclo (1º y 2º medio)'
    if(codigoEnse == '661' and codigoG == '3'):
        nombreGrado = '3º medio'
    if(codigoEnse == '661' and codigoG == '4'):
        nombreGrado = '4º medio'

    if(codigoEnse == '663' and codigoG == '1'):
        nombreGrado = 'Primer nivel (1º y 2º medio)'
    if(codigoEnse == '663' and codigoG == '3'):
        nombreGrado = 'Segundo nivel (3º medio)'
    if(codigoEnse == '663' and codigoG == '4'):
        nombreGrado = 'Tercero nivel (4º medio)'

    if(codigoEnse == '710' and codigoG == '1'):
        nombreGrado = '1º medio'
    if(codigoEnse == '710' and codigoG == '2'):
        nombreGrado = '2º medio'
    if(codigoEnse == '710' and codigoG == '3'):
        nombreGrado = '3º medio'
    if(codigoEnse == '710' and codigoG == '4'):
        nombreGrado = '4º medio'

    if(codigoEnse == '760' and codigoG == '1'):
        nombreGrado = 'Primer ciclo (1º y 2º medio)'
    if(codigoEnse == '760' and codigoG == '3'):
        nombreGrado = '3º medio'
    if(codigoEnse == '760' and codigoG == '4'):
        nombreGrado = '4º medio'

    if(codigoEnse == '761' and codigoG == '1'):
        nombreGrado = 'Primer ciclo (1º y 2º medio)'
    if(codigoEnse == '761' and codigoG == '3'):
        nombreGrado = '3º medio'
    if(codigoEnse == '761' and codigoG == '4'):
        nombreGrado = '4º medio'

    if(codigoEnse == '763' and codigoG == '1'):
        nombreGrado = 'Primer nivel (1º y 2º medio)'
    if(codigoEnse == '763' and codigoG == '3'):
        nombreGrado = 'Segundo nivel (3º medio)'
    if(codigoEnse == '763' and codigoG == '4'):
        nombreGrado = 'Tercero nivel (4º medio)'

    if(codigoEnse == '810' and codigoG == '1'):
        nombreGrado = '1º medio'
    if(codigoEnse == '810' and codigoG == '2'):
        nombreGrado = '2º medio'
    if(codigoEnse == '810' and codigoG == '3'):
        nombreGrado = '3º medio'
    if(codigoEnse == '810' and codigoG == '4'):
        nombreGrado = '4º medio'

    if(codigoEnse == '860' and codigoG == '1'):
        nombreGrado = 'Primer ciclo (1º y 2º medio)'
    if(codigoEnse == '860' and codigoG == '3'):
        nombreGrado = '3º medio'
    if(codigoEnse == '860' and codigoG == '4'):
        nombreGrado = '4º medio'

    if(codigoEnse == '861' and codigoG == '1'):
        nombreGrado = 'Primer ciclo (1º y 2º medio)' 
    if(codigoEnse == '861' and codigoG == '3'):
        nombreGrado = '3º medio'
    if(codigoEnse == '861' and codigoG == '4'):
        nombreGrado = '4º medio'
        
    if(codigoEnse == '863' and codigoG == '1'):
        nombreGrado = 'Primer nivel (1º y 2º medio)'
    if(codigoEnse == '863' and codigoG == '3'):
        nombreGrado = 'Segundo nivel (3º medio)'
    if(codigoEnse == '863' and codigoG == '4'):
        nombreGrado = 'Tercero nivel (4º medio)'

    if(codigoEnse == '910' and codigoG == '1'):
        nombreGrado = '1º medio'
    if(codigoEnse == '910' and codigoG == '2'):
        nombreGrado = '2º medio'
    if(codigoEnse == '910' and codigoG == '3'):
        nombreGrado = '3º medio'
    if(codigoEnse == '910' and codigoG == '4'):
        nombreGrado = '4º medio'

    if(codigoEnse == '963' and codigoG == '3'):
        nombreGrado = 'Segundo nivel (3º medio)'
    if(codigoEnse == '963' and codigoG == '4'):
        nombreGrado = 'Tercero nivel (4º medio)'
    return nombreGrado

def jornada(codigoJ):
    nombreJ = 'nope'
    if(codigoJ == '1'):
        nombreJ = 'Mañana'
    if(codigoJ == '2'):
        nombreJ = 'Tarde'
    if(codigoJ == '3'):
        nombreJ = 'Mañana y tarde'
    if(codigoJ == '4'):
        nombreJ = 'Vespertina / Nocturna'  
    if(codigoJ == '0'):
        nombreJ = 'Sin información'         
    return nombreJ

def tipoCurso(codigoTC):
    nombreTC = 'nope'
    if(codigoTC == '0'):
        nombreTC = 'Curso Simple'
    if(codigoTC == '1'):
        nombreTC = 'Curso Combinado'
    if(codigoTC == '2'):
        nombreTC = 'Curso Combinado'
    if(codigoTC == '3'):
        nombreTC = 'Curso Combinado'    
    if(codigoTC == '4'):
        nombreTC = 'Curso Combinado'  
    if(codigoTC == '5'):
        nombreTC = 'Curso Combinado'  
    if(codigoTC == '6'):
        nombreTC = 'Curso Combinado'     
    if(codigoTC == '99'):
        nombreTC = 'Sin información'           
    return nombreTC
    
def descCurso(codigoDC):
    nombreDC = 'nope'
    if(codigoDC == '0'):
        nombreDC = 'No aplica'
    if(codigoDC == '1'):
        nombreDC = 'Sólo Liceo'
    if(codigoDC == '2'):
        nombreDC = 'Dual'
    if(codigoDC == '3'):
        nombreDC = 'Otro'    
    return nombreDC
    
def generoAl(codigoGA):
    nombreGA = 'nope'
    if(codigoGA == '0'):
        nombreGA = 'Sin Información'
    if(codigoGA == '1'):
        nombreGA = 'Masculino'
    if(codigoGA == '2'):
        nombreGA = 'Femenino'   
    return nombreGA
    
def intAl(codigoIA):
    nombreIA = 'nope'
    if(codigoIA == '0'):
        nombreIA = 'No'
    if(codigoIA == '1'):
        nombreIA = 'Sí'
    if(codigoIA == '.'):
        nombreIA = 'Sin Información'   
    return nombreIA

def gdAl(codigoGDA):
    nombreGDA = 'nope'
    if(codigoGDA == '99'):
        nombreGDA = 'Sin Información'
    if(codigoGDA == '0'):
        nombreGDA = 'No está en grupo diferencial'
    if(codigoGDA == '1'):
        nombreGDA = 'Si está en grupo diferencial'
        
    return nombreGDA
    
def rama(codigoR):
    nombreR = 'nope'
    if(codigoR == '0'):
        nombreR = 'Ciclo General / Sin información'
    if(codigoR == '400'):
        nombreR = 'Comercial'
    if(codigoR == '500'):
        nombreR = 'Industrial'   
    if(codigoR == '600'):
        nombreR = 'Técnica'
    if(codigoR == '700'):
        nombreR = 'Agrícola' 
    if(codigoR == '800'):
        nombreR = 'Marítima'
    if(codigoR == '900'):
        nombreR = 'Artística'         
    return nombreR    
    
def sector(codigoSec):
    nombreSec = 'nope'
    if(codigoSec == '0'):
        nombreSec = 'Ciclo General / Sin información'
    if(codigoSec == '410'):
        nombreSec = 'Administración y Comercio'
    if(codigoSec == '510'):
        nombreSec = 'Construcción'
    if(codigoSec == '520'):
        nombreSec = 'Metalmecánico'
    if(codigoSec == '530'):
        nombreSec = 'Electricidad'
    if(codigoSec == '540'):
        nombreSec = 'Minero'
    if(codigoSec == '550'):
        nombreSec = 'Gráfica'
    if(codigoSec == '560'):
        nombreSec = 'Químico'
    if(codigoSec == '570'):
        nombreSec = 'Confección'
    if(codigoSec == '580'):
        nombreSec = 'Tecnología y Telecomunicaciones'
    if(codigoSec == '610'):
        nombreSec = 'Alimentación'
    if(codigoSec == '620'):
        nombreSec = 'Programas y Proyectos Sociales'
    if(codigoSec == '630'):
        nombreSec = 'Hotelería y Turismo'
    if(codigoSec == '640'):
        nombreSec = 'Salud y Educación'
    if(codigoSec == '710'):
        nombreSec = 'Maderero'
    if(codigoSec == '720'):
        nombreSec = 'Agropecuario'
    if(codigoSec == '810'):
        nombreSec = 'Marítimo'
    if(codigoSec == '910'):
        nombreSec = 'Artes Visuales'
    if(codigoSec == '920'):
        nombreSec = 'Artes Escénicas Teatro'
    if(codigoSec == '930'):
        nombreSec = 'Artes Escénicas Danza'
    return nombreSec    
    
def espe(codigoEsp):
    nombreEsp = 'nope'
    if(codigoEsp == '0'):
        nombreEsp = 'Ciclo General / Sin información'
    if(codigoEsp == '41001'):
        nombreEsp = 'Administración'
    if(codigoEsp == '41002'):
        nombreEsp = 'Contabilidad'
    if(codigoEsp == '41003'):
        nombreEsp = 'Secretariado'
    if(codigoEsp == '41004'):
        nombreEsp = 'Ventas'
    if(codigoEsp == '41005'):
        nombreEsp = 'Administración (con mención)'        
    if(codigoEsp =='51001' ):
            nombreEsp ='Edificación'
    if(codigoEsp =='51002' ):
            nombreEsp ='Terminaciones de Construcción'
    if(codigoEsp =='51003'):
            nombreEsp ='Montaje Industrial'
    if(codigoEsp =='51004' ):
            nombreEsp ='Obras viales y de infraestructura'
    if(codigoEsp =='51005' ):
            nombreEsp ='Instalaciones Sanitarias'
    if(codigoEsp =='51006' ):
            nombreEsp ='Refrigeración y climatización'
    if(codigoEsp =='51008' ):
            nombreEsp ='Instalaciones Sanitarias'
    if(codigoEsp =='51009' ):
            nombreEsp ='Construcción (con mención)'
    if(codigoEsp =='52008' ):
            nombreEsp ='Mecánica Industrial'
    if(codigoEsp =='52009' ):
            nombreEsp ='Construcciones Metálicas'
    if(codigoEsp =='52010' ):
            nombreEsp ='Mecánica Automotriz'
    if(codigoEsp =='52011'):
            nombreEsp = 'Matricería'
    if(codigoEsp =='52012' ):
            nombreEsp ='Mecánica de mantención de aeronaves'
    if(codigoEsp =='52013' ):
            nombreEsp ='Mecánica Industrial (con mención)'
    if(codigoEsp =='53014' ):
            nombreEsp ='Electricidad'
    if(codigoEsp =='53015' ):
            nombreEsp ='Electrónica'
    if(codigoEsp =='53016' ):
            nombreEsp ='Telecomunicaciones'
    if(codigoEsp =='54018' ):
            nombreEsp ='Explotación minera'
    if(codigoEsp =='54019' ):
            nombreEsp ='Metalurgia Extractiva'
    if(codigoEsp =='54020' ):
            nombreEsp ='Asistencia en geología'
    if(codigoEsp =='55022' ):
            nombreEsp ='Gráfica'
    if(codigoEsp =='55023'):
            nombreEsp = 'Dibujo Técnico'
    if(codigoEsp =='56025'):
            nombreEsp = 'Operación de planta química'
    if(codigoEsp =='56026'):
            nombreEsp = 'Laboratorio químico'
    if(codigoEsp =='56027' ):
            nombreEsp ='Química Industrial (con mención)'
    if(codigoEsp =='57028' ):
            nombreEsp ='Tejido'
    if(codigoEsp =='57029'):
            nombreEsp = 'Textil'
    if(codigoEsp =='57030'):
            nombreEsp = 'Vestuario y Confección Textil'
    if(codigoEsp =='57031' ):
            nombreEsp ='Productos del cuero'
    if(codigoEsp =='58033' ):
            nombreEsp ='Conectividad y Redes'
    if(codigoEsp =='58034'):
            nombreEsp = 'Programación'
    if(codigoEsp =='58035'):
            nombreEsp = 'Telecomunicaciones'
    if(codigoEsp =='61001'):
            nombreEsp = 'Elaboración Industrial de Alimentos'
    if(codigoEsp =='61002' ):
            nombreEsp ='Servicio de Alimentación Colectiva'
    if(codigoEsp =='61003' ):
            nombreEsp ='Gastronomía (con mención)'
    if(codigoEsp =='62004'):
            nombreEsp = 'Atención de párvulos'
    if(codigoEsp =='62005' ):
            nombreEsp ='Atención de adultos mayores'
    if(codigoEsp =='62006' ):
            nombreEsp ='Atención de Enfermería'
    if(codigoEsp =='62007' ):
            nombreEsp ='Atención Social y Recreativa'
    if(codigoEsp =='62008' ):
            nombreEsp ='Atención de Enfermería (con mención)'
    if(codigoEsp =='63009' ):
            nombreEsp ='Servicio de turismo'
    if(codigoEsp =='63010' ):
            nombreEsp ='Servicios Hoteleros'
    if(codigoEsp =='63011'):
            nombreEsp = 'Servicio de hotelería'
    if(codigoEsp =='64001' ):
            nombreEsp ='Atención de párvulos'
    if(codigoEsp =='64008' ):
            nombreEsp ='Atención de Enfermería (con mención)'
    if(codigoEsp =='71001' ):
            nombreEsp ='Forestal'
    if(codigoEsp =='71002' ):
            nombreEsp ='Procesamiento de la madera'
    if(codigoEsp =='71003' ):
            nombreEsp ='Productos de la madera'
    if(codigoEsp =='71004' ):
            nombreEsp ='Celulosa y Papel'
    if(codigoEsp =='71005' ):
            nombreEsp ='Muebles y Terminaciones de la Madera'
    if(codigoEsp =='72006' ):
            nombreEsp ='Agropecuaria'
    if(codigoEsp =='72007' ):
            nombreEsp ='Agropecuaria (con mención)'
    if(codigoEsp =='81001'):
            nombreEsp = 'Naves mercantes y especiales'
    if(codigoEsp =='81002'):
            nombreEsp ='Pesquería'
    if(codigoEsp =='81003'):
            nombreEsp ='Acuicultura'
    if(codigoEsp =='81004' ):
            nombreEsp ='Operación portuaria'
    if(codigoEsp =='81005' ):
            nombreEsp ='Tripulación naves mercantes y especiales'
    if(codigoEsp =='91001'):
            nombreEsp = 'Artes Visuales'
    if(codigoEsp =='91002' ):
            nombreEsp ='Artes Audiovisuales'
    if(codigoEsp =='91003'):
            nombreEsp ='Diseño'
    if(codigoEsp =='91004' ):
            nombreEsp ='Antes Musicales'
    if(codigoEsp =='91005' ):
            nombreEsp ='Artes Escenicas'
    if(codigoEsp =='92004' ):
            nombreEsp ='Interpretación Teatral'
    if(codigoEsp =='92005' ):
            nombreEsp ='Diseño Escénico'
    if(codigoEsp =='93006' ):
            nombreEsp ='Interpretación en Danza de Nivel Intermedio'
    if(codigoEsp =='93007' ):
            nombreEsp ='Monitoría de Danza'


    return nombreEsp        
    
def mens(codigoMen):
    nombreMen = 'nope'
    if(codigoMen == '0'):
        nombreMen = 'Ciclo General / Sin información'
    if(codigoMen == '41005001'):
        nombreMen = 'Plan Común'        
    if(codigoMen == '41005002'):
        nombreMen = 'Logística'
    if(codigoMen == '41005003'):
        nombreMen = 'Recursos Humanos'
    if(codigoMen == '51007001'):
        nombreMen = 'Plan Común'
    if(codigoMen == '51007002'):
        nombreMen = 'Edificación'
    if(codigoMen == '51007003'):
        nombreMen = 'Terminaciones de la Construcción'
    if(codigoMen == '51007004'):
        nombreMen = 'Obras Viales e Insfraestructura'
    if(codigoMen == '52013001'):
        nombreMen = 'Plan Común'
    if(codigoMen == '52013002'):
        nombreMen = 'Mantenimiento Electromecánico'
    if(codigoMen == '52013003'):
        nombreMen = 'Máquinas-Herramientas'
    if(codigoMen == '52013004'):
        nombreMen = 'Matricería'
    if(codigoMen == '56027001'):
        nombreMen = 'Plan Común'
    if(codigoMen == '56027002'):
        nombreMen = 'Planta Química'
    if(codigoMen == '56027003'):
        nombreMen = 'Laboratorío Químico'
    if(codigoMen == '61003001'):
        nombreMen = 'Plan Común'
    if(codigoMen == '61003002'):
        nombreMen = 'Cocina'
    if(codigoMen == '61003003'):
        nombreMen = 'Pastelería y Repostería'
    if(codigoMen == '64008001'):
        nombreMen = 'Adultos Mayores'
    if(codigoMen == '64008002'):
        nombreMen = 'Enfermería'
    if(codigoMen == '64008003'):
        nombreMen = 'Plan Común'
    if(codigoMen == '72007001'):
        nombreMen = 'Plan Común'
    if(codigoMen == '72007002'):
        nombreMen = 'Agricultura'
    if(codigoMen == '72007003'):
        nombreMen = 'Pecuaria'
    if(codigoMen == '72007004'):
        nombreMen = 'Vitivinícola'
        
    return nombreMen      
    
def sitFin(codigoSit):
    nombreSit = 'Sin información'
    if(codigoSit == '-1'):
        nombreSit = 'Sin información'
    if(codigoSit == ' '):
        nombreSit = 'Sin información'
    if(codigoSit == ''):
        nombreSit = 'Sin información'
    if(codigoSit == 'P'):
        nombreSit = 'Promovido'
    if(codigoSit == 'R'):
        nombreSit = 'Reprobado'
    if(codigoSit == 'Y'):
        nombreSit = 'Retirado'
    return nombreSit  

def sitFinR(codigoSitR):
    nombreSitR = 'Sin información'
    if(codigoSitR == '-1'):
        nombreSitR = 'Sin información'
    if(codigoSitR == ' '):
        nombreSitR = 'Sin información'
    if(codigoSitR == ''):
        nombreSitR = 'Sin información'
    if(codigoSitR == 'P'):
        nombreSitR = 'Promovido'
    if(codigoSitR == 'R'):
        nombreSitR = 'Reprobado'
    if(codigoSitR == 'Y'):
        nombreSitR = 'Retirado'
    if(codigoSitR == 'T'):
        nombreSitR = 'Trasladado'
    return nombreSitR
    
def promedio(codigoP):
    prom = codigoP
    if(codigoP == '1,0'):
        prom = '10'
    if(codigoP == '1,1'):
        prom = '11'
    if(codigoP == '1,2'):
        prom = '12'
    if(codigoP == '1,3'):
        prom = '13'
    if(codigoP == '1,4'):
        prom = '14'
    if(codigoP == '1,5'):
        prom = '15'
    if(codigoP == '1,6'):
        prom = '16'
    if(codigoP == '1,7'):
        prom = '16'
    if(codigoP == '1,8'):
        prom = '16'
    if(codigoP == '1,9'):
        prom = '16'
    if(codigoP == '2,0'):
        prom = '20'
    if(codigoP == '2,1'):
        prom = '21'
    if(codigoP == '2,2'):
        prom = '22'
    if(codigoP == '2,3'):
        prom = '23'
    if(codigoP == '2,4'):
        prom = '24'
    if(codigoP == '2,5'):
        prom = '25'
    if(codigoP == '2,6'):
        prom = '26'
    if(codigoP == '2,7'):
        prom = '27'
    if(codigoP == '2,8'):
        prom = '28'
    if(codigoP == '2,9'):
        prom = '29'
    if(codigoP == '3,0'):
        prom = '30'
    if(codigoP == '3,1'):
        prom = '31'
    if(codigoP == '3,2'):
        prom = '32'
    if(codigoP == '3,3'):
        prom = '33'
    if(codigoP == '3,4'):
        prom = '34'
    if(codigoP == '3,5'):
        prom = '35'
    if(codigoP == '3,6'):
        prom = '36'
    if(codigoP == '3,7'):
        prom = '37'
    if(codigoP == '3,8'):
        prom = '38'
    if(codigoP == '3,9'):
        prom = '39'
    if(codigoP == '4,0'):
        prom = '40'
    if(codigoP == '4,1'):
        prom = '41'
    if(codigoP == '4,2'):
        prom = '42'
    if(codigoP == '4,3'):
        prom = '43'
    if(codigoP == '4,4'):
        prom = '44'
    if(codigoP == '4,5'):
        prom = '45'
    if(codigoP == '4,6'):
        prom = '46'
    if(codigoP == '4,7'):
        prom = '47'
    if(codigoP == '4,8'):
        prom = '48'
    if(codigoP == '4,9'):
        prom = '49'
    if(codigoP == '5,0'):
        prom = '50'
    if(codigoP == '5,1'):
        prom = '51'
    if(codigoP == '5,2'):
        prom = '52'
    if(codigoP == '5,3'):
        prom = '53'
    if(codigoP == '5,4'):
        prom = '54'
    if(codigoP == '5,5'):
        prom = '55'
    if(codigoP == '5,6'):
        prom = '56'
    if(codigoP == '5,7'):
        prom = '57'
    if(codigoP == '5,8'):
        prom = '58'
    if(codigoP == '5,9'):
        prom = '59'
    if(codigoP == '6,0'):
        prom = '60'
    if(codigoP == '6,1'):
        prom = '61'
    if(codigoP == '6,2'):
        prom = '62'
    if(codigoP == '6,3'):
        prom = '63'
    if(codigoP == '6,4'):
        prom = '64'
    if(codigoP == '6,5'):
        prom = '65'
    if(codigoP == '6,6'):
        prom = '66'
    if(codigoP == '6,7'):
        prom = '67'
    if(codigoP == '6,8'):
        prom = '68'
    if(codigoP == '6,9'):
        prom = '69'
    if(codigoP == '7,0'):
        prom = '70'
    if(codigoP == '1'):
        prom = '10'
    if(codigoP == '2'):
        prom = '20'
    if(codigoP == '3'):
        prom = '30'
    if(codigoP == '4'):
        prom = '40'
    if(codigoP == '5'):
        prom = '50'
    if(codigoP == '6'):
        prom = '60'
    if(codigoP == '7'):
        prom = '70'
    return prom    
    
    