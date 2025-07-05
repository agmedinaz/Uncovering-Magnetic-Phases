from .common import *

def name_of_folder(training=['para', 'ferro', 'neel', 'stripe']):

    if training == ['all']:
        training = ['para', 'ferro', 'neel', 'stripe']
        
    training_names = {'para': 'Para', 'ferro': 'Ferro', 'neel': 'Neel', 'stripe': 'Stripe'}

    name_of_folder = ''

    for name in training:
        if name_of_folder != '':
            name_of_folder += '_'
        name_of_folder += training_names[name]

    if name_of_folder=='Para_Ferro_Neel_Stripe':
        name_of_folder = 'All'

    return name_of_folder

def folders(type = 'DNN', training=['para', 'ferro', 'neel', 'stripe']):

    type = type.upper()

    type = type + '_outputs'

    name_folder = name_of_folder(training)

    folder = os.path.join(os.getcwd(), type, name_folder)

    os.makedirs(folder, exist_ok = True)
    return folder

def folders_figs(type = 'DNN', training=['para', 'ferro', 'neel', 'stripe']):

    type = type.upper()

    type = type + '_outputs'

    name_folder = name_of_folder(training)

    folder = os.path.join(os.getcwd(), type, name_folder, 'figs')

    os.makedirs(folder, exist_ok = True)
    return folder