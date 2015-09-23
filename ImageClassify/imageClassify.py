#encoding: utf-8
__author__ = 'Victor'
import numpy as np
import caffe
from parseClassName import parseClassName
'''
Program Description:
given an image, result is the class and correspond probobility it belongs to.
'''

class ImageClassifier():
       def classifyOneImage(self,imagePath):
            MODEL_FILE = '/home/victor/code/caffe/models/tmall/tmall_train_val.prototxt'
            PRETRAINED = '/home/victor/code/caffe/models/tmall/caffe_tmall_train_iter_450000.caffemodel'
            IMAGE_FILE = '/home/victor/code/caffe/examples/images/shirt.jpg'
            IMAGE_MEAN_FILE= '/home/victor/code/caffe/models/tmall/image_mean.npy'
            classNamePath='/home/victor/code/caffe/models/tmall/tml'
            caffe.set_mode_cpu()
            net = caffe.Classifier(MODEL_FILE,PRETRAINED,mean=np.load(IMAGE_MEAN_FILE).mean(1).mean(1),
                                   channel_swap=(2,1,0),raw_scale=255,image_dims=(256, 256))
            input_image = caffe.io.load_image(IMAGE_FILE)
            prediction = net.predict([input_image])#it seems that we have more good handel,but just take this for this moment.
            #from the fc_8 get the prob and get the correspond class
            [classNameMap,className_dict]=parseClassName.getClass(classNamePath)
            for key in classNameMap.keyset():
                #iterate the keyset
                print classNameMap[key],":",
                data = np.sum(net.blobs[key+'_fc8'].data,axis=0)
                rankList=data.flatten().argsort()
                for i in range(len(rankList)):
                    index=rankList[i]
                    print "%s %.3f"%(className_dict[key][index],data[index]),
                print
            #end

if __name__=="__main__":
    Classifier=ImageClassifier()
    Classifier.classifyOneImage("")



