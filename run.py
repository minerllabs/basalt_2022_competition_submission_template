import train
import test_BuildVillageHouse
import test_CreateVillageAnimalPen
import test_FindCave
import test_MakeWaterfall

import os
EVALUATION_STAGE = os.getenv('EVALUATION_STAGE', 'all')

# Training Phase
if EVALUATION_STAGE in ['all', 'training']:
    train.main()

# Testing Phase
if EVALUATION_STAGE in ['all', 'testing']:
    test_BuildVillageHouse.main()
    test_CreateVillageAnimalPen.main()
    test_FindCave.main()
    test_MakeWaterfall.main()
