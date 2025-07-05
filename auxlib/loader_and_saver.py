from .common import *

class loader_and_saver:
    '''
    Some examples on how to use the loader_and_saver class.

    Initializing the class:
    loading_data = loader_and_saver(os.getcwd())

    Saving data: Given some data set, in this case 'train_images'.
    loading_data.saver(train_images)

    Loading simulated images:
    sim_images, temperature = loading_data.simulatedImages(5)

    Loading data from the loader given some os path:
    sim = loading_data.loader(os.path.join(os.getcwd(),'2024-08-10','data_2'))

    Using the checker:
    loader_and_saver.checker(train_images, sim)
    '''
    def __init__(self, path):
        self.path = path
    
    
    def saver(self, data, directory=None, name_of_file='data'):
        if directory is None:
            directory = './data'

        if not os.path.exists(directory):
            os.makedirs(directory)

        base_name = name_of_file.strip()
        existing_files = [f for f in os.listdir(directory) if f.startswith(base_name) and f.endswith('.h5')]
        name_suffix = len(existing_files) + 1
        name = f"{base_name}_{name_suffix}.h5"

        file_path = os.path.join(self.path,directory,name)
        
        with h5py.File(file_path, 'w') as f:
            for i, arr in enumerate(tqdm(data, desc="Saving images", unit="array")):
                f.create_dataset(f'array_{i}', data=arr, compression='gzip', compression_opts=9)
        print("Files saved as", file_path)


    def loader(self, file_name):
        name = file_name
        if name[:-3] !='.h5':
            name += '.h5'

        loaded_list = []
        with h5py.File(name, 'r') as f:
            for key in tqdm(sorted(f.keys(), key=lambda x: int(x.split('_')[1])), 
                            desc="Loading arrays", unit="array"):
                loaded_list.append(f[key][:])
        print("Files loaded!")
        return loaded_list


    def checker(original_list, loaded_list):
        data_is_equal = True
        for original, loaded in zip(original_list, loaded_list):
            if not np.array_equal(original, loaded):
                data_is_equal = False
                break
        if data_is_equal:
            print("The original data set and the loaded data set are identical.")
        else:
            print("The original data set and the loaded data set are NOT identical.")


    def simulatedImages(self, index: int):
        print('Loading simulated images...')

        densityIndices = ['055','06', '061', '062', '063', '064', '065', '07', '08', '09','1']

        loadingPath = os.path.join(self.path,'data',f'data_p{densityIndices[index]}')
        
        simImages = self.loader(loadingPath)
        
        temperature = np.arange(0.0, 5.02, 0.02).tolist()
        dens_format = densityIndices[index][:1]+'.'+densityIndices[index][1:]
        print(f'Data of density p = {dens_format} succesfully loaded.')
        
        return simImages, temperature
    