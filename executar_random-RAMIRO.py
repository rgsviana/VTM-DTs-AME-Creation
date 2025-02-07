'''
	PARA EXECUTAR ESTE PROGRAMA, UTILIZE O SEGUINTE COMANDO:
		python3 executar_random.py
	EXEMPLO:
		python3 executar_random-RAMIRO.py
'''
import os
root = "/home/rgsviana/DATASETS_AME/"
datasets_train = ["dataset_ame_16x16_train.csv", "dataset_ame_16x32_train.csv", "dataset_ame_16x64_train.csv", "dataset_ame_32x16_train.csv", "dataset_ame_32x32_train.csv", "dataset_ame_32x64_train.csv", "dataset_ame_64x16_train.csv", "dataset_ame_64x32_train.csv", "dataset_ame_64x64_train.csv", "dataset_ame_64x128_train.csv", "dataset_ame_128x64_train.csv", "dataset_ame_128x128_train.csv"]
datasets_test = ["dataset_ame_16x16_test.csv", "dataset_ame_16x32_test.csv", "dataset_ame_16x64_test.csv", "dataset_ame_32x16_test.csv", "dataset_ame_32x32_test.csv", "dataset_ame_32x64_test.csv", "dataset_ame_64x16_test.csv", "dataset_ame_64x32_test.csv", "dataset_ame_64x64_test.csv", "dataset_ame_64x128_test.csv", "dataset_ame_128x64_test.csv", "dataset_ame_128x128_test.csv"]
models = ["dataset_ame_16x16", "dataset_ame_16x32", "dataset_ame_16x64", "dataset_ame_32x16", "dataset_ame_32x32", "dataset_ame_32x64", "dataset_ame_64x16", "dataset_ame_64x32", "dataset_ame_64x64", "dataset_ame_64x128", "dataset_ame_128x64", "dataset_ame_128x128"]

for dataset_train, dataset_test, model in zip(datasets_train, datasets_test, models):
    os.system("python3 random_search-RAMIRO.py "+root+dataset_train+" "+root+dataset_test+" 3000 "+model)

