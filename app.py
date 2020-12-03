from flask import Flask, render_template, request
import numpy as np
from joblib import load
app = Flask(__name__)
model = load("zoo_model.joblib")

#zoo = Animal_predictor()
@app.route('/',methods=['POST'])
def make_prediction():
    input = np.array([])
    attributes = ['hair','feather','eggs','milk','airborne','aquatic','predator','toothed','backbone','breathes','venemous','fins','legs','tail','domestic','catsize']
    for attribute in attributes:
        if attribute == 'legs':
            if type(request.form['legs']) == "int":
                input = np.concatenate((input, np.array([(request.form['legs'])])))
            else:
                input = np.concatenate((input, np.array([0])))
        else:
            if request.form[attribute] == "yes":
                input = np.concatenate((input,np.array([1])))
            else:
                input = np.concatenate((input, np.array([0])))

    class_num = model.predict(input.reshape(1,-1))
    class_info = {1:"Mammal",2:"Bird",3:"Reptile",4:"Fish",5:"Amphibian",6:"Bug",7:"Invertebrate"}
    info = {1:"aardvark, antelope, bear, boar, buffalo, calf, cavy, cheetah, deer, dolphin, elephant, fruitbat, giraffe, girl, goat, gorilla, hamster, hare, leopard, lion, lynx, mink, mole, mongoose, opossum, oryx, platypus, polecat, pony, porpoise, puma, pussycat, raccoon, reindeer, seal, sealion, squirrel, vampire, vole, wallaby, wolf, anta, ariranha, boto-cor-de-rosa, bugio, cachorro-vinagre, chimpanze, gato-maracaja, jaguatirica, lobo-guara, macaco-aranha, macaco-barrigudo, mico-leao-dourado, mono-carvoeiro, onca-pintada, orangotango, peixe-boi, queixada, tamandua-bandeira, urso-de-oculos",
            2:"chicken, crow, dove, duck, flamingo, gull, hawk, kiwi, lark, ostrich, parakeet, penguin, pheasant, rhea, skimmer, skua, sparrow, swan, vulture, wren, aguia-cinzenta, aracari-banana, arara-azul, arara-caninde, chaua, ema, gaviao-pombo, guara, harpia, jacurutu, jacutinga, jandaia-amarela, macuco, murucututu, mutum, papagaio-de-cara-roxa, pato-de-crista, pavo, tucano-de-bico-preto, urubu-rei",
            3:"pitviper, seasnake, slowworm, tortoise, tuatara, turtle, chameleon, iguana, lizard, gecko, python, boa, adder, crocodile, alligator, gharial, skink, cobra-cipo, jabuti, jacare-coroa, jararaca-ilhoa, jiboia, sucuri, tracaja, urutu-cruzeiro",
            4:"bass, carp, catfish, chub, dogfish, haddock, herring, pike, piranha, seahorse, sole, stingray, tuna, anchovy, flounder, halibut, mackerel, barracuda, marlin, trout, baiacu, cascudinho-de-caverna, lambari, matrinxa, pirarucu, raia-chita, tambaqui, tubarao-raposa",
            5:"frog, frog, newt, toad, salamander, siren, tree frog, dart frog, firebelly, wart toad, perereca-de-alcatrazes, ra-flecha-azul, ra-pimenta, sapo-barriga-de-fogo, sapo-cururu, sapo-de-chifre",
            6:"flea, gnat, honeybee, housefly, ladybird, moth, termite, wasp, mosquito, hornet, cricket, beetle, butterfly, palmetto, cockroach, mantis, dragonfly, aphid, cicada, antlion, abelha, joaninha, mariposa, pirilampo, vespa",
            7:"clam, crab, crayfish, lobster, octopus, scorpion, seawasp, slug, starfish, worm, scallop, spider, snail, silkworm, jellyfish, squid, bicho-pau, caracol-da-mata-atlantica, caranguejeira, sauva-limao"}
    return render_template("result.html",result=class_info[class_num[0]],info=info[class_num[0]])

@app.route('/',methods=['GET'])
def load():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)