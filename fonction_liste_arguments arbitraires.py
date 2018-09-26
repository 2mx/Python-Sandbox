# **args permet de recevoir une liste d'aguments
# @see https://docs.python.org/fr/3.7/tutorial/controlflow.html#keyword-arguments
def custom_digit(**config_args):
    config = {
        'color' : '#000000',
        'width' : 8,
        'heigt' : 8
        }
    #config = {**config, **config_args}# Avec Phyton 3.5 et +
    config.update(config_args)
    print(config)
    print("La couleur = " + config['color'])


custom_digit(color='#DEFF45', width=10, font=())
