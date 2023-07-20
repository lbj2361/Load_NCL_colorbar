import numpy as np
from matplotlib.colors import LinearSegmentedColormap

def loadcolorbar(colorbarname):    #获取色标的函数
    colorbardir="./colorbar/"      #色标文件夹的位置
    colorbarpath=colorbardir+colorbarname+".txt"    #色标的路径
    colorbar=LinearSegmentedColormap.from_list(colorbarname, np.loadtxt(colorbarpath)) #获取色标
    
    return colorbar


