import requests
import random

words = ["Frodo","Sam","Gandalf","Aragorn","Legolas","Gimli","Boromir","Sauron","Gollum","Galadriel","Elrond","Arwen","Eowyn","Faramir","Denethor","Theoden","Merry","Pippin","Bilbo","Shelob","Smaug","Radagast","Saruman","Isildur","Elendil","Eomer","Grima","Treebeard","Tom","Balin","Dwalin","Kili","Fili","Bard","Beorn","Thranduil","Celeborn","Glorfindel","Beregond","Brego","Shadowfax","Nazgul","Witchking","Minas","Tirith","Gondor","Rohan","Mordor","Moria","Lorien","Rivendell","Isengard","Shire","Hobbiton","Bree","Weathertop","Anduin","Mount","Doom","Orodruin","Lothlorien","Helms","Deep","Orthanc","Barad","Durin","Beleriand","Valinor","Erebor","Gundabad","Angmar","Numenor","Dagorlad","Fangorn","Edoras","Caradhras","Khazad","Umbar","Dol","Guldur","Osgiliath","Esgaroth","Argonath","Amon","Hen","Emyn","Muil","Palantir","Silmaril","Sting","Glamdring","Orcrist","Narsil","Anduril","One","Precious","Ring","Mithril","Gollum","Elves","Dwarves","Orcs","Hobbits"]
dict = {
    "Frodo": "Hobbit que lleva el Anillo Único a Mordor.",
    "Sam": "Leal compañero de Frodo en su viaje.",
    "Gandalf": "Mago sabio que guía a la Comunidad del Anillo.",
    "Aragorn": "Heredero de Isildur y futuro rey de Gondor.",
    "Legolas": "Elfo arquero del Bosque Negro.",
    "Gimli": "Enano guerrero, amigo de Legolas.",
    "Boromir": "Hombre de Gondor, miembro de la Comunidad.",
    "Sauron": "Señor oscuro que forjó el Anillo Único.",
    "Gollum": "Criatura corrompida por el Anillo.",
    "Galadriel": "Reina élfica de Lothlórien, muy poderosa.",
    "Elrond": "Señor élfico de Rivendel.",
    "Arwen": "Hija de Elrond, enamorada de Aragorn.",
    "Eowyn": "Dama de Rohan que derrota al Rey Brujo.",
    "Faramir": "Hermano de Boromir, noble y sabio.",
    "Denethor": "Senescal de Gondor, padre de Boromir y Faramir.",
    "Theoden": "Rey de Rohan.",
    "Merry": "Hobbit amigo de Frodo, valiente y alegre.",
    "Pippin": "Hobbit travieso y curioso, amigo de Merry.",
    "Bilbo": "Tío de Frodo, antiguo portador del Anillo.",
    "Shelob": "Gigantesca araña de Mordor.",
    "Smaug": "Dragón que custodia el tesoro de Erebor.",
    "Radagast": "Mago amante de la naturaleza y los animales.",
    "Saruman": "Mago traidor aliado con Sauron.",
    "Isildur": "Antiguo rey que cortó el Anillo de Sauron.",
    "Elendil": "Padre de Isildur, fundador de Gondor y Arnor.",
    "Eomer": "Guerrero de Rohan y sobrino del rey Théoden.",
    "Grima": "Consejero traidor de Théoden, llamado Lengua de Serpiente.",
    "Treebeard": "Ent antiguo que ayuda a los hobbits.",
    "Tom": "Ser misterioso del bosque, inmune al Anillo.",
    "Balin": "Enano que lideró la expedición a Moria.",
    "Dwalin": "Hermano de Balin, compañero de Thorin.",
    "Kili": "Joven enano de la compañía de Thorin.",
    "Fili": "Hermano de Kili, valiente y leal.",
    "Bard": "Arquero que mata a Smaug.",
    "Beorn": "Hombre que puede transformarse en oso.",
    "Thranduil": "Rey élfico del Bosque Negro, padre de Legolas.",
    "Celeborn": "Señor élfico y esposo de Galadriel.",
    "Glorfindel": "Elfo poderoso que ayuda a Frodo en Rivendel.",
    "Beregond": "Soldado leal de Gondor que protege a Faramir.",
    "Brego": "Caballo noble de Rohan, montura de Aragorn.",
    "Shadowfax": "Caballo más veloz de la Tierra Media, montura de Gandalf.",
    "Nazgul": "Espectros del Anillo, sirvientes de Sauron.",
    "Witchking": "Rey Brujo de Angmar, líder de los Nazgûl.",
    "Minas": "Prefijo de ciudades fortificadas, como Minas Tirith.",
    "Tirith": "Segunda parte del nombre de la ciudad de Gondor.",
    "Gondor": "Reino de los Hombres al sur de la Tierra Media.",
    "Rohan": "Reino de jinetes valientes, aliados de Gondor.",
    "Mordor": "Tierra oscura donde reside Sauron.",
    "Moria": "Antigua mina de enanos bajo las Montañas Nubladas.",
    "Lorien": "Bosque élfico gobernado por Galadriel.",
    "Rivendell": "Refugio élfico dirigido por Elrond.",
    "Isengard": "Fortaleza de Saruman.",
    "Shire": "La Comarca, hogar de los hobbits.",
    "Hobbiton": "Aldea principal de la Comarca.",
    "Bree": "Pueblo donde se encuentran los hobbits con Aragorn.",
    "Weathertop": "Colina donde Frodo es herido por un Nazgûl.",
    "Anduin": "Gran río que cruza la Tierra Media.",
    "Mount": "Monte, parte del nombre del Monte del Destino.",
    "Doom": "Destino, parte del nombre Monte del Destino.",
    "Orodruin": "Nombre élfico del Monte del Destino.",
    "Lothlorien": "Bosque dorado de los elfos, también llamado Lórien.",
    "Helms": "Parte del nombre del Abismo de Helm, fortaleza de Rohan.",
    "Deep": "Parte del nombre Abismo de Helm.",
    "Orthanc": "Torre de Saruman en Isengard.",
    "Barad": "Parte del nombre Barad-dûr, la torre de Sauron.",
    "Durin": "Antiguo señor enano, fundador de Khazad-dûm.",
    "Beleriand": "Región del oeste perdida bajo el mar.",
    "Valinor": "Tierra de los Valar, hogar de los inmortales.",
    "Erebor": "Montaña Solitaria, reino de los enanos.",
    "Gundabad": "Montaña tomada por los orcos.",
    "Angmar": "Reino del Rey Brujo en el norte.",
    "Numenor": "Isla de hombres sabios, destruida por su orgullo.",
    "Dagorlad": "Campo de batalla frente a la Puerta Negra.",
    "Fangorn": "Bosque antiguo donde habitan los ents.",
    "Edoras": "Capital de Rohan.",
    "Caradhras": "Montaña peligrosa en las Montañas Nubladas.",
    "Khazad": "Prefijo de Khazad-dûm, el reino de los enanos.",
    "Umbar": "Puerto de corsarios enemigos de Gondor.",
    "Dol": "Prefijo de lugares oscuros, como Dol Guldur.",
    "Guldur": "Segunda parte de Dol Guldur, fortaleza de Sauron.",
    "Osgiliath": "Antigua capital de Gondor, ahora en ruinas.",
    "Esgaroth": "Ciudad del Lago, hogar de los hombres.",
    "Argonath": "Grandes estatuas que marcan la entrada a Gondor.",
    "Amon": "Prefijo de colinas o montes, como Amon Hen.",
    "Hen": "Parte del nombre Amon Hen, colina de visión.",
    "Emyn": "Prefijo de colinas, como Emyn Muil.",
    "Muil": "Parte del nombre Emyn Muil, colinas rocosas del este.",
    "Palantir": "Piedra vidente usada para comunicarse a distancia.",
    "Silmaril": "Joya sagrada creada por Fëanor.",
    "Sting": "Espada de Bilbo y luego de Frodo.",
    "Glamdring": "Espada de Gandalf.",
    "Orcrist": "Espada de Thorin Escudo de Roble.",
    "Narsil": "Espada rota de Isildur, forjada como Andúril.",
    "Anduril": "Espada reforjada de Narsil, empuñada por Aragorn.",
    "One": "El Anillo Único de Sauron.",
    "Precious": "Cómo Gollum llama al Anillo.",
    "Ring": "El Anillo Único, fuente de poder y corrupción.",
    "Mithril": "Metal élfico ligero y resistente.",
    "Elves": "Raza inmortal de la Tierra Media.",
    "Dwarves": "Raza de enanos, hábiles mineros y herreros.",
    "Orcs": "Criaturas oscuras creadas por Morgoth.",
    "Hobbits": "Pequeños habitantes pacíficos de la Comarca."}
alphabet_min = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

alphabet_max = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

def char_fromapi():

    url = "https://the-one-api.dev/v2/character"

    headers = {
        "Authorization": "Bearer emMSizTpuv-gYa81exWF"
    }

    response = requests.get(url, headers=headers)
    characters = response.json()["docs"]
    random_character = random.choice(characters)

    # return random_character["name"].lower()
    return random_character




