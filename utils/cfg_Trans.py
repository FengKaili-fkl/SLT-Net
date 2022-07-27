DROP_PATH_RATE = 0.4
FINAL_UPSAMPLE: "expand_first"
EMBED_DIM = 96
DEPTHS = [2, 2, 2, 2]
depths_decoder = [1, 2, 2, 2]
NUM_HEADS = [3, 6, 12, 24]
WINDOW_SIZE = 32
IMG_SIZE = 512
PATCH_SIZE = 4
IN_CHANS = 3
num_classes = 2
MLP_RATIO = 4
QKV_BIAS = True
QK_SCALE = None
DROP_RATE = 0

APE = False
PATCH_NORM = True
USE_CHECKPOINT =False

print('='*10+'cfg'+'='*10)
print('WINDOW_SIZE',WINDOW_SIZE)
print('PATCH_SIZE',PATCH_SIZE)
print('IMG_SIZE',IMG_SIZE)
print('MLP_RATIO',MLP_RATIO)
print('DROP_PATH_RATE',DROP_PATH_RATE)
print('DROP_RATE',DROP_RATE)
print('='*10+'=='+'='*10)