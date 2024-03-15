a=1
if a == 1:
    module_path = 'nets.unet'
else:
    module_path = 'mynets.unet'

module = __import__(module_path, fromlist=['Unet'])
Unet = getattr(module, 'Unet')

# 现在你可以像使用普通导入那样使用Unet
unet_instance = Unet()