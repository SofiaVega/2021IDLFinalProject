# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

def CreateDataLoader(opt):
    print("\n>>CreateDataLoader(opt)")
    from data.custom_dataset_data_loader import CustomDatasetDataLoader
    data_loader = CustomDatasetDataLoader()
    print(data_loader.name())
    data_loader.initialize(opt)
    return data_loader
