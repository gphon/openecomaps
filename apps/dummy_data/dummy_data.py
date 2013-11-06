#!/usr/bin/python
# -*- coding: latin-1 -*-

def convert2html( text ):
    return text.replace('ä', '&auml;').replace('Ä', '&Auml;'). \
                replace('ö', '&ouml;').replace('Ö', '&Ouml;'). \
                replace('ü', '&uuml;').replace('Ü', '&Uuml;'). \
                replace('%', '%%').replace('ß', '&szlig;')


PAGE_FISH_P_TITLE = 'Fischliste Potsdam'
PAGE_FISH_P_TEXT = 'von Stuttgart kopiert :-).'
PAGE_FISH_P_IMAGE = 'blank.gif'
PAGE_FISH_P_FLYER = 'fischliste_stuttgart.pdf'

PAGE_FISH_S_TITLE = 'Fischliste Stuttgart'
PAGE_FISH_S_TEXT = 'Seit mehreren Jahrzehnten werden die Weltmeere industriell ausgebeutet. Das hat dazu gefÃ¼hrt, dass 87 Prozent der FischbestÃ¤nde zu den Ãœberfischten oder erschÃ¶pften BestÃ¤nden gezÃ¤hlt werden. Die maritimen Ã–kosysteme sind auÃŸerdem noch von anderen, menschengemachten Gefahren bedroht: VermÃ¼llung der Meere mit PlastikabfÃƒÂƒÃ‚Â¤llen, Verschmutzung mit ÃƒÂƒÃ‚Â–l durch zunehmende Tiefseebohrungen, ÃƒÂƒÃ‚ÂœberdÃƒÂƒÃ‚Â¼ngung der Meere durch industrielle Landwirtschaft, Klimawandel. Die Organisation Greenpeace kÃƒÂƒÃ‚Â¤mpft seit ihrer GrÃƒÂƒÃ‚Â¼ndung fÃƒÂƒÃ‚Â¼r den Erhalt der MeeresÃƒÂƒÃ‚Â¶kosysteme. Greenpeace Stuttgart setzt die Themen lokal und verbrauchernah um. So ist unsere Stuttgarter Fischliste bereits in der neunten Auflage.'
PAGE_FISH_S_IMAGE = 'blank.gif'
PAGE_FISH_S_FLYER = 'fischliste_stuttgart.pdf'

PAGE_PAPER_B_TITLE = 'Papierratgeber Berlin'
PAGE_PAPER_B_TEXT = '2008 haben wir einen Papierratgeber fÃƒÂƒÃ‚Â¼r Berlin entwickelt, der jedes Jahr aktualisiert wird und auf diesen Internetseiten zum Download bereit steht. Besonders mÃƒÂƒÃ‚Â¶chten wir auch die Verwendung von Recyclingpapier in der Schule fÃƒÂƒÃ‚Â¶rdern, dafÃƒÂƒÃ‚Â¼r sind wir auf Schul- und Kinderfesten oft prÃƒÂƒÃ‚Â¤sent.'
PAGE_PAPER_B_IMAGE = 'blank.gif'
PAGE_PAPER_B_FLYER = 'papierratgeber_berlin.pdf'

PAGE_PAPER_Halle_TITLE = 'Papierratgeber Halle'
PAGE_PAPER_Halle_TEXT = 'Im Juni 2010 haben wir unseren Flyer zum Thema Recyclingpapier fertig gestellt.<br><br>Er ist fuer Kinder und deren Eltern gedacht. Auf der Vorderseite befindet sich ein Comic des Grafikers Bern Zierfuss, das den Kindern an Hand zweier Hefte und ihrer Geschichte die Bedeutung von Recyclingpapier fuer den Waldschutz und die Umwelt klar macht.'
PAGE_PAPER_Halle_IMAGE = 'blank.gif'
PAGE_PAPER_Halle_FLYER = 'papierratgeber_potsdam.pdf'

PAGE_PAPER_HH_TITLE = 'Papierratgeber Hamburg'
PAGE_PAPER_HH_TEXT = 'keine Beschreibung hinterlegt'
PAGE_PAPER_HH_IMAGE = 'blank.gif'
PAGE_PAPER_HH_FLYER = 'papierratgeber_hamburg.pdf'

PAGE_PAPER_P_TITLE = 'Papierratgeber Potsdam'
PAGE_PAPER_P_TEXT = '2008 haben wir einen Papierratgeber fÃƒÂ¼r Potsdam entwickelt, der jedes Jahr aktualisiert wird und auf diesen Internetseiten zum Download bereit steht. Besonders mÃƒÂ¶chten wir auch die Verwendung von Recyclingpapier in der Schule fÃƒÂ¶rdern, dafÃƒÂ¼r sind wir auf Schul- und Kinderfesten oft prÃƒÂ¤sent.'
PAGE_PAPER_P_IMAGE = 'blank.gif'
PAGE_PAPER_P_FLYER = 'papierratgeber_potsdam.pdf'

###############################################################################

SEAL_EU_BIO_NAME = 'EU-Bio'
SEAL_EU_BIO_DESCRIPTION = convert2html( '''
Zum Jahresbeginn 2009 trat in der EU eine neue Basisverordnung (VO Nr. 834/2007) über den ökologischen Landbau in Kraft. Darin wird die Herstellung ökologischer Produkte und ihre Kennzeichnung mit Hilfe des EU-Bio-Siegels und der Öko-Kontrollstelle geregelt. Auf verpackten Lebensmitteln ist das Siegel Pflicht, auf unverpackten Erzeugnissen kann es freiwillig benutzt werden. Neben dem EU-Bio-Siegel können zusätzlich auch andere, wie nationale Logos oder Logos von Anbauverbänden verwendet werden.<br>
Die neue Basisverordnung als rechtliche Grundlage für die ökologische Landwirtschaft, soll die Rechtslage vereinfacht, klarer aber weniger im Detail regeln. Es wurden Ziele und Grundsätze hinzugefügt.<br>
Ergänzt wird die Basisverordnung durch konkretere Durchführungsbestimmungen (VO Nr. 889/2008) sowie eine Importregelung (VO Nr. 1235/2008) für Produkte von außerhalb der EU. Nationale Gesetze, wie das deutsche Ökolandbaugesetz, können weitere Regelungen beinhalten.<br>
<br>
<h3>Kriterien:</h3>
Die Betriebe sollen wenn möglich in einem hofeigenen Kreislauf wirtschaften, also eigene Futtermittel anbauen oder Dünger aus eigenem Kompost verwenden. Zukäufe müssen aus ökologischem Landbau kommen und müssen dokumentiert werden. In Ausnahmefällen kann aber auch konventionelles Saatgut, Pflanzensetzlinge, Futtermittel und Tiere zugekauft werden. Der Pflanzenschutz sollte durch vorbeugende Maßnahmen, z.B. Nützlinge, Fruchtwechsel oder robustere Arten geschehen. Als letzte Lösung dürfen aber bestimmte Pflanzenschutzmittel oder chemisch-synthetische Dünger eingesetzt werden.<br>
Mindestens 95% der Futtermittel sowie der Zutaten verarbeiteter Produkte müssen aus ökologischer Landwirtschaft stammen. Dagegen dürfen keine gentechnisch veränderten Organismen (GVO) im Landbau oder der Verarbeitung verwendet werden. Zusatzstoffe, die mit Hilfe von GVO hergestellt wurden dürfen allerdings verwendet werden, wenn sie anders nicht verfügbar sind.<br>
Die Verwendung von Zusatzstoffen ist beschränkt und entspricht etwa einem Zehntel derer konventioneller Produkte.<br>
<br>
<h3>Kontrolle:</h3>
Um die Einhaltung der Standards zu gewährleisten, werden die Erzeuger- und Verarbeitungsbetriebe einmal im Jahr kontrolliert. Zusätzlich können stichprobenartig unangemeldete Kontrollen stattfinden. Dabei werden von unabhängigen, anerkannten Kontrollstellen die Tiere und Pflanzen, Betriebsunterlagen, Produktionsstätten und Erzeugnisse überprüft und ein Bericht angefertigt. Da diese Kontrollen über den ganzen Prozess von der Herstellung über die Verarbeitung bis teilweise zu den Verkaufsstellen erfolgen, wird die durchgängige Überprüfung der Produktherstellung sichergestellt.<br>
Die Kontrollstelle muss auf allen Produkt mit einer Codenummer angegeben werden, wodurch eine Rückverfolgbarkeit gewährleistet ist.<br>
<br>
Bei Verstößen gegen die Richtlinien drohen den Betrieben Auflagen, Geldstrafen oder sogar die Aberkennung des Siegels.
''' )
SEAL_EU_BIO_IMAGE = 'eu_bio.svg'

SEAL_DEMETER_NAME = 'Demeter'
SEAL_DEMETER_DESCRIPTION = convert2html( '''
Demeter ist ein Anbauverband, dessen Produkte nach biologisch-dynamischen Richtlinien hergestellt werden. Die Anbauweise basiert auf der anthroposophischen Lehre, in der ein Hof als Organismus - also ein in sich geschlossenes System - verstanden wird. Deshalb sollte ein Demeter-Hof die nötigen Zutaten für seine Produkte selbst herstellen. Eine Leitlinie ist das Ressourcen- und Energiesparen und der Einsatz erneuerbarer Energiequellen. Zudem wird auf den Schutz des Bodens und der Erhaltung des Bodenlebens wertgelegt.<br>
Das 1997 gegründete internationale Netzwerk umfasst mittlerweile fast 50 Länder.<br>
<br>
<h3>Kriterien:</h3>
Der Verband schreibt einzuhaltende Mindestanforderungen für Erzeugung und Verarbeitung vor, welche über dem Standard des EU-Bio-Siegels liegen. Der gesamte Betrieb muss auf biologisch-dynamische Landwirtschaft umgestellt werden.<br> 
Die Zutaten von Produkten müssen zu mindestens 90% aus Demeter-zertifizierten Bestandteilen bestehen. Nur wenn bestimmte Zutaten nicht verfügbar sind, können diese nach Genehmigung von Demeter e.V. von anderen Anbauverbänden oder von EU-Bio-zertifizierten Betrieben zugekauft werden. Die Zusatzstoffe sind auf 13 "absolut notwendige" beschränkt und für jedes Lebensmittel geregelt.<br>
Saatgut sollte auf dem eigenen Hof oder in der Region vermehrt werden. Über eine Negativliste ist bestimmtes Saatgut ausgeschlossen.<br>
Um die biologisch-dynamische Landwirtschaft zu gewähren, muss jeder Hof Tierhaltung einschließen. Dabei sind die Demeter-Richtlinien der Tierhaltung stärker Reglementiert als beim EU-Bio-Siegel. So soll die Haltung den Bedürfnissen der Tiere angepasst werden. Die Tiere dürfen zur Schlachtung nicht weiter als 200 Kilometer transportiert werden. Futtermittel müssen zu mindestens 50% vom eigenen Hof oder einer Hofkooperation stammen, zugekauftes Futter sollte biologisch-dynamisch produziert worden sein. Es darf keine konventionellen Bestandteile enthalten.<br>
<br>
<h3>Kontrolle:</h3>
Neben der Kontrolle im Zuge des Bio-Siegels wird jährlich die Einhaltung der Kriterien von Demeter e.V. durch den Verband überprüft sowie ein Gespräch zur Betriebsentwicklung geführt.
''')
SEAL_DEMETER_IMAGE = 'demeter.svg'

SEAL_FAIRTRADE_NAME = 'Fair Trade'
SEAL_FAIRTRADE_DESCRIPTION = 'Siegel fuer fairen Handel'
SEAL_FAIRTRADE_IMAGE = 'fair_trade.svg'

SEAL_FSC_NAME = 'FSC'
SEAL_FSC_DESCRIPTION = 'forest stewardship council'
SEAL_FSC_IMAGE = 'fsc.svg'

SEAL_MSC_NAME = 'MSC'
SEAL_MSC_DESCRIPTION = 'marine stewardship council'
SEAL_MSC_IMAGE = 'msc.svg'