from .common import *

class SyntheticImagesGen:
    '''
    Some examples on how to use SyntheticImagesGen class.

    Initializing the class:
    data = SyntheticImagesGen(10, training=['ferro','neel','stripe'], L=40)

    Generating synthetic data:
    train_images, train_labels = data.dataGenerator()

    Info:    
    data.Info()
    '''

    def __init__(self, training: list[str]=['all'], L=40):
        if training == ['all']:
            training = ['para', 'ferro', 'neel', 'stripe']
        else:
            training = [element.lower() for element in training]

        self.training = training
        self.L = L

    def spin_gen(self, conf: str):
        '''
        Generates a spin configuration for the given configuration. 
        The resulting data is a tuple of the different configurations each one can have.
        For example, ferromagnetic configurations can be spin up ferromagnetic or spin down ferromagnetic.
        In this case, the tuple will contain two LxL matrices, one per each type.
        '''
        spin_conf = []
        if conf == 'ferro':
            spin_conf = [np.ones((self.L, self.L)).astype(int), 
                        -np.ones((self.L, self.L)).astype(int)]
        elif conf == 'neel':
            spin = np.fromfunction(lambda i, j: (-1)**(i + j + (conf == 4)), 
                                (self.L, self.L)).astype(int)
            spin_conf = [spin, -spin]
        elif conf == 'stripe':
            spin = np.fromfunction(lambda i, j: (-1)**j, (self.L, self.L)).astype(int)
            spin_conf = [spin, -spin, spin.T, -spin.T]
        elif conf == 'para':
            spin_conf = np.random.choice([-1, 1], size=(self.L, self.L)).astype(int)
            spin_conf = [spin_conf]
        return spin_conf
    
    def Info(self, number_configs: int):
        return print(f'Number of configurations: {number_configs}\nTraining: {self.training} \nL: {self.L}\n')

    def dataGenerator(self, number_configs: int):
        ''' 
        Generates synthetic data given a number of configurations and the type of training we want to do.
        If 'all', then it will generate all possible configurations evenly distributed. There are 4 types of configurations.
        If the number of configurations is not divisible by 4, the remaining configurations will be generated in a paramagnetic manner.
        '''
        start_time = time.time()
        print("Generating synthetic data...")
        config_dict = {
            'para': 1,
            'ferro': 2,
            'neel': 2,
            'stripe': 4
        }

        labels_dict = {
            'para': 0,
            'ferro': 1,
            'neel': 2,
            'stripe': 3
        }

        selected_dict = {k: v for k, v in config_dict.items() if k in self.training}

        len_selected = 0

        for conf in selected_dict:
            len_selected += selected_dict[conf]
                                                                    
        total_configs_per_selected = number_configs // len_selected
        remaining_configs = number_configs % len_selected

        train_images = []
        train_labels = []
        
        for conf in selected_dict:
            total_conf = total_configs_per_selected 

            for _ in range(total_conf):
                train_images.extend(self.spin_gen(conf))
                for _ in range(config_dict[conf]):
                    train_labels.append(labels_dict[conf])

        for i in range(remaining_configs):
            index = i % len(self.training)
            train_images.append(self.spin_gen(self.training[index])[0])
            train_labels.append(labels_dict[self.training[index]])

        temp = list(zip(train_images, train_labels))
        random.shuffle(temp)
        train_images, train_labels = zip(*temp)

        print("Done!")

        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Elapsed time:", elapsed_time, "seconds")
        return np.array(train_images), np.array(train_labels)

