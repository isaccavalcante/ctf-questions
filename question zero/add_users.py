from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    seq = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    cpf = db.Column(db.String(120))
    password = db.Column(db.String(80))

db.create_all()

def generate_names():
    print("[", end=" ")
    with open("nomes.csv") as f:
        lines = f.readlines()[:1800]
        for line in lines:
            name = line.split(",")[0] 
            print( '"{}"'.format(name), end=",")
    print("]")

names = ["MARIA","ANA","JOAO","GABRIEL","LUCAS","PEDRO","MATEUS","JOSE","GUSTAVO","VITORIA","GUILHERME","CARLOS","JULIA","VITOR","FELIPE","LETICIA","MARCOS","RAFAEL","LUIZ","DANIEL","EDUARDO","MATHEUS","LUIS","AMANDA","BRUNO","BEATRIZ","GABRIELA","LARISSA","PAULO","LEONARDO","MARIANA","VINICIUS","DAVI","BRUNA","SAMUEL","VICTOR","CAMILA","ISABELA","FRANCISCO","CAIO","ANTONIO","TIAGO","LUANA","SARA","EDUARDA","BIANCA","RAFAELA","GEOVANA","FERNANDA","IGOR","NATALIA","LAURA","LUAN","ANDRE","NICOLAS","JULIANA","MIGUEL","NICOLE","THIAGO","GABRIELE","YASMIN","ARTHUR","HENRIQUE","CAUA","RODRIGO","RAISSA","DIEGO","SABRINA","LIVIA","ARTUR","LARA","RUAN","ALINE","MILENA","RIAN","GIOVANA","JESSICA","BRENDA","KAUAN","VANESSA","DEBORA","PABLO","DAVID","ANDERSON","CAROLINE","BRENO","RENAN","MARCELO","LEANDRO","FERNANDO","ALICE","SOFIA","LUIZA","ALAN","ANDRESSA","ISADORA","TAINA","JULIO","DIOGO","KAUA","REBECA","MURILO","ALEXANDRE","DANILO","DOUGLAS","YASMIM","ERICA","WESLEY","TAIS","EMILY","CARLA","VINICIOS","ALEX","RAIANE","ISABELE","RAQUEL","RICARDO","FABIO","EMILI","ITALO","LAIS","DANIELE","CAMILE","TAINARA","BARBARA","CLARA","TALITA","JENIFER","CAROLINA","LORENA","CAUAN","PAMELA","ENZO","JEFERSON","FABRICIO","SAMARA","ESTER","EVELIN","IAGO","INGRID","YURI","DANIELA","ERICK","TAMIRES","MARINA","JAQUELINE","ERIC","IASMIN","OTAVIO","MAICON","JEAN","FLAVIA","NATAN","MARCELA","THAIS","RENATA","IASMIM","ALANA","ESTEFANI","EVERTON","ALISSON","ADRIELE","EMERSON","RYAN","CAIQUE","EMANUEL","MANUELA","MAIARA","KAIQUE","FRANCISCA","GABRIELI","JAMILE","JOICE","ANTONIA","CRISTIAN","WILLIAN","MARIANE","ALESSANDRA","ADRIANO","VICTORIA","PAULA","DAIANE","ALISON","HUGO","JUAN","EMILLY","RENATO","FLAVIO","JONAS","BERNARDO","GISELE","PATRICIA","WESLEI","GIOVANNA","MICHELE","LUCIANO","EMILE","RICHARD","ADRIAN","ANNA","MELISSA","ELEN","MARCIO","JORGE","MARCO","EMANUELE","ERIK","FRANCIELE","VIVIANE","IAN","ELOISA","KEVIN","PAOLA","KAIO","CLEITON","KAUE","SAMIRA","MAURICIO","MAISA","EDSON","ROBERTA","LUISA","ROBSON","NAIARA","ALESSANDRO","KAILANE","ISABELLA","ELIAS","LAVINIA","MARLON","FILIPE","KAUANE","HELOISA","KAREN","ANDREI","WILIAN","PALOMA","NATANAEL","MOISES","JANAINA","SARAH","MIRELA","STEFANI","CAUE","JOANA","IARA","ARIANE","MICAEL","JONATAN","SOPHIA","KARINE","ISABEL","JUNIOR","FABIANA","ELLEN","AUGUSTO","LUCIANA","IZABELA","ESTEFANE","GRAZIELE","PIETRO","ISABELI","PRISCILA","NATALI","RAISA","JOSUE","HEITOR","MAYARA","POLIANA","ROBERTO","JONATAS","ISAQUE","RAYANE","ISRAEL","RAMON","EZEQUIEL","LAISA","KARINA","ICARO","SERGIO","EVELYN","ADRIANA","MANOEL","WANDERSON","ISAC","YAN","AGATA","MICHAEL","HELENA","ELAINE","NICOLI","YAGO","ANE","ROBERT","LAIANE","VERONICA","MONIQUE","RAYSSA","CLAUDIO","GEAN","WENDEL","ISMAEL","ADRIEL","DEIVID","LAILA","NATHALIA","MAIRA","PATRICK","IURI","DENILSON","JONATHAN","MANOELA","KAIKE","CRISTIANO","VALERIA","TALIA","SUELEN","CAUANE","KELVIN","MICHEL","ISABELLE","JONATA","MILENE","ALICIA","CECILIA","CAROLAINE","GEOVANNA","RIQUELME","BEATRIS","CAMILI","GEOVANE","MIRIAN","GUILERME","MIKAEL","HELEN","ARIEL","RONALDO","TATIANE","LUDIMILA","IRIS","KELLY","ISAAC","JHONATAN","STEFANY","ERIKA","RAUL","RAI","LARISA","CINTIA","GABRIELLE","RONALD","GIULIA","JENNIFER","MARIO","ANGELA","TALES","RAIMUNDO","VIVIAN","JULIANO","TAIANE","GABRIELLY","RITA","WELITON","JULIANE","CICERO","WILLIAM","ANGELO","MONICA","CESAR","FABIANO","TAMARA","PIETRA","MARCIA","LEVI","ELOA","ROGERIO","ANGELICA","ANDREIA","ISAIAS","KEILA","NAYARA","ANDREZA","VAGNER","NATHAN","JACKSON","ROGER","ALVARO","ALEXANDRA","JEOVANA","LORRANE","MARILIA","CRISTIANE","CARINE","WELLINGTON","MICAELE","CLARICE","JAINE","KETLIN","MAYCON","ANDRESA","GRAZIELA","ALEXANDRO","ISABELLY","IVAN","TAUANE","BRYAN","JOAQUIM","JOYCE","JOEL","GESSICA","ANTONY","LEANDRA","ESTEFANY","JOSIANE","ELISA","ANTONI","CLAUDIA","DANIELI","ANNE","WEVERTON","ADRIELI","JAIANE","HELLEN","LUDMILA","DENIS","CAILANE","CHARLES","DENISE","HIAGO","JAMILI","JHONATA","EMANUELI","TALISON","CARINA","CRISTINA","AGATHA","CAROL","TAILA","HIGOR","KESIA","ESTELA","IZADORA","VALENTINA","EMANOEL","SAULO","FABIOLA","ANDRIELE","WAGNER","ELIANE","KEVEN","NAIANE","SAVIO","CASSIO","LANA","CASSIA","KAROLINE","ERIQUE","MARTA","TAISSA","IZABELE","DIANA","THAINA","MANUEL","ALLAN","JHENIFER","ROMULO","ANDREY","KAIK","INGRIDE","BRIAN","JADSON","SANDRO","JAILSON","TAISA","CIBELE","ALEXIA","SAMANTA","JEFFERSON","LILIAN","ADRIA","CLEBER","MIRELE","WELINGTON","MARCUS","LORRAINE","NATIELE","CATARINA","EVILIN","TAILANE","LAIZA","BRAIAN","VANDERSON","ADRIANE","LAZARO","THALITA","NATALY","KAMILA","LIDIA","LUANE","WALISON","MARIELE","KETLEN","EMANUELA","KAYLANE","EVANDRO","GEOVANI","SANDRA","CAMILLY","YARA","RAPHAEL","MIQUEIAS","LUNA","ISIS","ELTON","NICOLY","ARIELE","CASSIANE","GABRIELY","RUTE","JENIFFER","LILIANE","DARLAN","WALLACE","SUZANA","LUCA","GABRIELLA","WALACE","JORDANA","CRISLAINE","STEFANE","EMANUELLE","WELINTON","RAILANE","LIDIANE","LORENZO","CAMILY","TALISSON","MAX","LAUANE","BRAYAN","GIOVANI","MICAELA","SIMONE","JHON","REINALDO","BRENA","ALBERTO","WILSON","TATIANA","MAYRA","ABRAAO","MAURO","NICOLLY","IZAQUE","KELI","MICHELI","PRICILA","RAILSON","WILIAM","DAIANA","MIKAELE","MICAELI","ALEXSANDRO","MARCELE","MAYSA","ANNY","EDILSON","JOELMA","GILBERTO","TAYNA","RAINARA","JACSON","JADE","KAUANY","ANANDA","FABRICIA","FRANCIELI","KARLA","SILAS","ELOIZA","GIOVANE","TAYNARA","CAMILLE","FABIANE","BRENDO","DANDARA","JOSIEL","ELANE","DEIVISON","THALES","NATASHA","NAIRA","RUBENS","GISLAINE","ABNER","JANDERSON","SEBASTIAO","ESTHER","ELIZA","LUARA","ELEM","JAMILY","VINICIO","KALINE","DEVID","THALIA","SANDY","GRASIELE","MIRIAM","WEMERSON","ANDRIELI","REGINALDO","WALISSON","KETELIN","THAYNA","ANDREINA","KAUANI","KAMILLY","THAMIRES","TOMAS","ENRIQUE","SAMILA","RAIANA","INGRIDI","ELIANA","PETERSON","AILTON","EVELLYN","ANALICE","REGIANE","LEIDIANE","GILSON","HUDSON","GLORIA","CLARISSE","ELIEL","SILVIA","EVERSON","RANIELE","LUMA","DAYANE","NOEMI","JARDEL","JANIELE","MAICOM","WENDERSON","RAILA","ERIKE","LUCCA", "ISAC", "MAIANE","DANIELLE","FATIMA","ESTEVAO","STHEFANY","YGOR","EMANUELLY","ANDREA","SAMILE","IURY","NUBIA","JOSEANE","GLENDA","DEISE","SUELEM","ALANE","KAYKY","GILMAR","LUZIA","ANGELINA","ANTHONY","SILVIO","JOSIAS","RAFAELLA","JOHN","LEILA","THOMAS","TAUAN","GRACIELE","VALTER","ADILSON","ROSANA","GLEICE","RUTH","HELIO","GLEICIANE","CRISLANE","RAFAELE","ISABELLI","TULIO","TAMIRIS","IZABEL","JOELSON","JAKSON","SILVANA","KAMILE","EDER","EDNA","PATRIK","ISABELY","CRISTOFER","MATIAS","CLEBERSON","GRAZIELI","KELY","MISAEL","JOSEFA","MIRELLA","HENRY","ROSANGELA","MAIZA","LAISLA","MARA","FRANCINE","KAROLAINE","SAMIA","REGINA","APARECIDA","JAIRO","ANDREW","EVA","IGO","LORRANA","NATACHA","STEPHANY","VANESA","CLARISSA","RAILAN","FREDERICO","KETLYN","SHEILA","ELISANGELA","MESSIAS","NARA","JAIR","CASSIANO","EVELIM","ELOISE","LORANE","OLIVIA","CICERA","JESICA","IURE","GEORGE","NADIA","INGRED","RENAM","CAUANI","KATIA","ALEF","WENDER","ALEXANDER","GERSON","RUAM","EMELI","ELIZABETE","WESLLEY","GABRIELLI","LAISSA","EMELY","LIGIA","RAINE","CAUAM","GEFERSON","JUSSARA","LUCIENE","JAMILLY","THEO","NELSON","MAXUEL","LAINE","WELLITON","GISELI","KEMILI","FAGNER","JOSIELE","YURE","VICENTE","KAYKE","KAWAN","CHRISTIAN","MEL","LUCIO","MACIEL","DALILA","ELIZEU","KELIANE","LUCIA","KLEBER","GENILSON","JULHA","KIARA","IZABELI","KAUAM","MIRELI","LAYSA","KEMILY","GLEISON","MIZAEL","KEZIA","KAREM","KAIKY","DIENIFER","CHAIANE","GERALDO","ROMARIO","CALEBE","RAICA","RIVALDO","ROSIANE","THAINARA","IANA","MARCIEL","DERICK","PATRIC","GEANE","RIAM","KAUANA","MARCELI","MIKAELI","HANNA","SAMOEL","ELISON","IZABELLA","NATHALY","NATIELI","RHUAN","AILA","LUCIELE","CAIKE","INACIO","STEPHANIE","KEMILLY","CAREN","THAYNARA","SILMARA","LINCON","LAISE","CELSO","ELISEU","BERNADO","ARTU","LEO","EDMILSON","LUCIANE","RAY","LUIGI","RAYSA","ADRIELLY","JEANE","SIDNEI","LORRAN","TATIELE","EVELY","GLEIDSON","RODOLFO","DEIVIDE","TAINAR","WILIANE","NICOLLE","IANE","WELISON","ROSA","PAULINA","ELIS","JOISE","CLEISON","GILVAN","LAYLA","ADSON","TALIS","RAMOM","GEISIANE","LIANDRA","MILLENA","RAIZA","VANDERLEI","ELIZANGELA","GEISA","JOABE","SUELI","ALESANDRA","ATILA","DARA","RANA","KAMILY","NILTON","HEBERT","FRANCIANE","THAISSA","JACIARA","KAILA","EDILENE","RAFAELI","SUELLEN","HUMBERTO","AIRTON","LAUREN","MAGNO","MICHELLE","EDERSON","WELLINTON","MARISA","MANUELLA","ESDRAS","KESSIA","RAQUELE","JONATHA","NADSON","AFONSO","LARYSSA","TAUANI","KAUN","DAMIAO","TARCISIO","HENRRIQUE","RONI","ADRIELY","ANITA","NINA","KIMBERLY","TANIA","ADRIELLE","LUCIMARA","FLAVIANE","VALQUIRIA","MARIELI","ILANA","TEREZA","ANY","DAVILA","UESLEI","CLAUDIANE","EDVALDO","NICHOLAS","EDGAR","GIAN","DOMINIQUE","ARIANA","MAIKON","MIKAELA","RIANA","GENIFER","VALESCA","LORAINE","EZEQUIAS","SANTIAGO","JAIME","NATA","NAELI","VALMIR","WELLIGTON","ELVIS","RUBIA","IRAN","MAITE","KAIANE","ADAILTON","TIFANI","THAISA","MONALISA","ROSEANE","ROSILENE","EVELI","SORAIA","VALDIR","WASHINGTON","DANIELLY","RAIMUNDA","VITORIO","SAFIRA","TAUANA","ALESANDRO","WANESSA","LAYANE","NIVIA","JAKELINE","JESSE","CAMILLA","LORRANY","KETELEN","RAQUELI","JACKELINE","ELDER","ALEJANDRO","CLEIDIANE","EDIVAN","KAROLINA","WENDELL","KAILAINE","EMANUELY","ELITON","WELTON","JEREMIAS","ORLANDO","ADENILSON","EDVAN","JORDAN","DAFNE","LIA","RAIAN","ESMERALDA","NILSON","MARIAH","SAMELA","ELIAN","NAILA","TAISE","THAYS","WELIGTON","EMILIA","ALANIS","NIVEA","SUZANE","JOVANA","QUESIA","KENNEDY","EMILLI","AGNES","RIKELME","ALEXSANDER","REINAN","ENRICO","LILIA","KAYQUE","KELLI","MILTON","ALLANA","HILLARY","HENRI","JAILTON","SIDNEY","EMILLE","SAIMON","EWERTON","MADSON","GIOVANNI","CLAUDINEI","VICTO","JHONATAS","NAYANE","IVO","ARTHU","ALBERT","ELENA","DERIK","LAIZ","DEISIANE","BENEDITO","MAICO","DAFINE","LIEDSON","ALERRANDRO","ADAO","TABATA","SAMILI","GILMARA","CAIC","DOGLAS","GRASIELA","LARRISA","LEONAN","DIONATAN","ELIELSON","RONILSON","NAYRA","MORGANA","TAYLA","CLEVERSON","MARCIELE","CLEBSON","KAIC","FRANCILENE","LAUANA","MAILSON","JOSILENE","WARLEY","MAIKE","ANIELE","MARILENE","JOANDERSON","KAYO","WALLISON","ANI","ELIENE","EDIVALDO","CARLIANE","SIBELE","DEBORAH","FRANK","TAUA","ELIDA","GILHERME","KENEDY","EITOR","ISLANE","INGREDI","JAMES","HERIQUE","WALTER","IZAIAS","JOSIMAR","IVANILDO","SOLANGE","DAVISON","DIONE","LAILSON","HADASSA","MARCELLA","RANIEL","OSVALDO","FABIA","EDIVANIA","EMERSOM","DOMINGOS","REBECCA","OSMAR","ARMANDO","SAMANTHA","MAXSUEL","EVELEN","ANDRIEL","THAYLA","KASSIA","JHENIFFER","SALOMAO","JONATHAS","GLAUBER","LORAN","HELOISE","ARNALDO","ALAM","ISA","SUIANE","DARLENE","RAPHAELA","INARA","EDINALDO","NALANDA","FRANKLIN","ADEMIR","SUSANA","IZABELLE","MARI","MIRIA","SHAIANE","ADRYAN","PEROLA","GREICE","ESMAEL","ABRAO","CALINE","HELEM","LUAM","ARIELI","NATALIE","JOSIVAN","MIKAELY","IZABELLY","VALDEMIR","JENEFER","ABEL","MURILLO","LAURIANE","CRISTIELE","QUEZIA","VANIA","CAUANA","GISLANE","SONIA","TACIANE","CAIK","CELIO","STEFANIE","IVANILSON","JANE","CEZAR","EDIMILSON","LOUISE","EDNALDO","JULHO","ELIEZER","JACIELE","ANDERSOM","JANINE","EDISON","MIKAELLY","LUANDERSON","ALMIR","KENIA","ELIZANDRA","RAIRA","WESLEN","TAILAN","TAYANE","INGREDE","IANDRA","EMYLI","JEOVANE","RONIEL","RAYANNE","JHENNIFER","RENE","ALEXSANDRA","UANDERSON","LORRAYNE","PIERRE","KALEBE","KEREN","EMELLY","GULHERME","JAMERSON","DARIO","SINTIA","RONALDE","HELOIZA","JAMILLE","MELISA","EDILAINE","LAIRA","SANDRIELE","ISAEL","TALINE","HERCULES","ULISSES","KATHLEEN","AGHATA","PATRIQUE","CLAITON","NICOLLAS","THAILA","OLAVO","ELISANDRA","LEILIANE","RONAN","DENER","NAILSON","LARISSE","KAIKI","ELLEM","VALDINEI","EDVANIA","GRABRIEL","LUCILENE","KAILANY","RAUAN","RILARI","CASSANDRA","JESUS","RIANE","KEMILE","ALFREDO","JULIENE","GUILHEME","ADEILSON","JULIE","GLAUCIA","LISANDRA","JULIAN","BRENNO","LAIANA","AYLA","GESICA","ELIVELTON","CARLO","RONILDO","ENDERSON","MARCELLY","ANTONIEL","JACIANE","GRAZIELLE","JHONY","WENDY","MANUELI","EVILE","AQUILES","TAINAN","MAILON","EMANOELE","KATIANE","MAILA","WELISSON","DANIELY","LINDA","AVILA","ELISSON","LARICA","EVILYN","JORDANIA","HELOA","JOILSON","JUNIO","KAROL","RAIR","KALEB","MACELO","QUEILA","TIFANY","UGO","JULI","JOANE","GIULIANA","ADRIENE","TAINE","OSEIAS","RAYNARA","IZAC","STELA","ASHLEY","FRANCIEL","GABRIL","VANUSA","LAERCIO","WILTON","LUANI","GEOVANIA","RAYLA","JEFESON","KALIANE","LEITICIA","THAIANE","VENICIOS","ELIELTON","LAYS","HENZO","MICAELY","EDILANE","ELISABETE","VIRGINIA","JOBSON","BETINA","LAURO","ARIADNE","KEVIM","IVANA","JOSIVALDO","RENILSON","RAYAN","KETILIN","JOSENILDO","ALYSSON","THIERRY","MOISEIS","ADALBERTO","TICIANE","POLIANE","ELI","ANDESON","DARLISON","STHEFANI","SULAMITA","RANIELI","STELLA","EVILI","FRANCINALDO","ERIVAN","JANICE","CLAUDEMIR","LENILSON","ADAILSON","ELIABE","WILLIANE","LORANA","MATHES","KAMILI","ADILA","OSCAR","SAMILY","AGNALDO","HECTOR","KAROLAYNE","ALLISON","DIONATA","ESTHEFANY","MARISTELA","SAMIR","THALISON","LAYZA","RENILDO","GARIEL","MARCEL","LOHANA","JOAB","MICKAEL","KAINAN","CLEVERTON","THAYANE","FRED","CLEIDSON","MARCELLE","OLIVER","ESTEVAN","EVELLY","IRES","VIVIA","KATIELE","MARLENE","GERLANE","HILARY","RILARY","LIZANDRA","BIATRIZ","GEISE","WEDSON","FILHO","EULER","KEVELIN","JAISON","VERA","LARRISSA","TADEU","NIKOLAS","LEILANE","ERNANDES","KLEBERSON","WEVERSON","CELINE","COSME","CLEICIANE","JOA","ERIVALDO","ROSELI","ELENILSON","FELIX","LIRIEL","CAETANO","ENSO","HANA","JHONATHAN","JEFERSSON","IARLEY","KELVEN","DIOVANA","RAINA","CAINA","VITO","TALLES","FELLIPE","LIZ","NATAM","MYLENA","FLAVIANA","URIEL","JHONNY","THAUANE","MARIZA","LAIRTON","DANILA","SHIRLEY","EDENILSON","MAIK","DAMARIS","CAIANE","GRASIELI","ALISSOM","THAYSSA","ITAMAR","CLEITO","CAREM","KELEN","GISLENE","RAYANA","TIFANE","DEYVID","NATANIEL","LOHAN","DIANE","WILLAN","KEYLA","CRISTIANA","ELSON","BRENDON","LUKAS","GEREMIAS","EVELLIN","KAILAN","EVERALDO","AMILTON","KAMILLA","MARJORIE","TAIANA","ROBISON","MILA","MIRELLY","ALISOM","CLEYTON","UDSON","HERICK","MARLOM","ATHUR","ISAMARA","ALIFER","JEFERSOM","ISLA","MILENI","JHONE","REGIS","RAIKA","FABIELE","LARIANE","FABIULA","KETELYN","MARCILENE","MARCONE","LUZIANE","CATIA","REBEKA","KLEITON","STEFANNY","AGDA","NATALHA","LAILTON","KAMILLE","CELIA","CRISTINE","IARLEI","ISLAINE","THAUANY","ELIZABETH","LEOMAR","RAYNE","EXPEDITO","SAYMON","EDIELSON","ODAIR","TAILON","GREGORI","IOLANDA","GEILSON","CAIRO","CINTHIA","ALEFE","KAYLA","MARLISON","ALDO","JOSUEL","LEONEL","LIS","LAUANDA","TUANE","MAIANA","GRAZIELLY","LIAN","EDINA","ADNA","JAINARA","IRLAN","IRANILDO","ITALA","LANNA","JUCILENE","ERINALDO","UELITON","VANDERLEIA","MAINARA","BENICIO","MARIANY","EDMAR","JERFESON","DAMIANA","NATHALI","MANOELE","WILKER","JASMIN","HENRICO","flag{seja_vc_sua_propria_flag}","GLEDSON","DAIVID","THALLES","KEVYN","DAMARES","SANDI","ALGUSTO","ANELISE","SALATIEL","MERCIA","MATHIAS","WARLEI","ANDRIA","GIZELE","STEPHANI","NAGILA","TAIZA","MICHELLY","KAYK","RUANA","RHYAN","AQUILA","JEANDERSON","CLAYTON","MARY","JEOVA","RAIANI","JONH","TAILSON","ABIMAEL","RICK","GISELLE","LAYSLA","RAVI","IASMI","MAYKON","TARCILA","EVILY","RAVENA","ESEQUIEL","RAIARA","KETHELYN","RAILTON","EVILIM","KIMBERLI","MAXWELL","PLINIO","ISLAN","RUTI","ALANI","INGRIDY","CALEB","RUI","ELOAH","SEVERINO","STEPHANE","CELINA","KELE","LOREN","SALETE","KERLON","RONALDI","RENA","KAROLYNE","JENNYFER","LEANDERSON","JASMIM","RICHARDE","EVERTOM","TAUANY","KEVEM","KAUANNY","XAIANE","JANILSON","IZAEL","LEIA","MAYANE","MELINA","VENICIUS","CLEDSON","KELVI","FILHA","VALDEIR","HIAN","EDIANE","DARLEI","SINARA","FREDSON","AMAURI","ABIGAIL","ERIVELTON","ALYSON","EVELINE","ELINE","ELISAMA","LUIZE","SHIRLEI","IONARA","FRANCIELLE","KALITA","ALESSA","LINDOMAR","CLEANE","MURIEL","RANGEL","DEVISON","CIBELI","CRISTOPHER","NIVALDO","SAMILLY","TAISLANE","KAINA","RAIANY","STEFFANY","EDIMAR","HERICA","ERISON","MARIANNA","LOHANE","EMANUELLI","TAIZ","JUCIELE","DANIELLA","HYAGO","TACILA","HEMILLY","ANDRIO","ROBERTE","LAVINHA","TASSIO","TAISON","ENDRIO","ESTEFANIA","EDINEI","AMABILE","AISHA","THALISSON","ALIFE","CAINAN","ELIZIANE","MARIANI","HELDER","DAVY","LIANA","CRISTHIAN","LAUANI","EVALDO","FERNADA","ELANO","ROSANE","VALESKA","EVANILSON","MIRELLE","RAYLANE","DERIC","SABRINE","PATRICIO","RICHARLISON","THALIS","ELIETE","YOHANA","THYAGO","GIRLANE","PAMELLA","DENISON","JOALISON","HANNAH","GEORGIA","RENER","QUILHERME","MARIANO","FILIPI","ROBERIO","INES","FELIPI","ANTONELA","CRISTIAM","ATOS","HARTUR","TERESA","GRABRIELA","RIQUELMI","JONES","JULLY","MICAELLY","ELIESER","KELVIM","JANETE","NAIANA","KENEDI","LUANY","TACIANA","FRANCIELY","KEVILIN","RONEI","ERICO","KELLEN","ALDAIR","BRAIN","RADIJA","MOACIR","ALERANDRO","KEROLIN","KYARA","CAMILLI","KUAN","JOAN","CLEILSON","EYSHILA","JULY","LEON","JARDIEL","DEIVIDI","APOLO","DENIZE","HERBERT","IAM","GLEICIELE","YANE","KASSIO","CINDY","ADELSON","WILHAN","GISELA","BENTO","CARMEM","NATANI","DEIVD","TAYLOR","VANILSON","HIGO","TOBIAS","CHRISTOPHER",]

for index, name in enumerate(names):
    print(f"[{index}] adding user {name}")
    user = User(name=name, cpf=random.randint(10000000000, 99999999999), password=None)
    db.session.add(user)
    db.session.commit()



