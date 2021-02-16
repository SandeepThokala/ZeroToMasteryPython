from imageai.Prediction import ImagePrediction
import os

execution_path = os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsMobileNetV2()
prediction.setModelPath(os.path.join(execution_path, r"C:\Users\sande\Desktop\Deepu\ZTM\MachineLearning\mobilenet_v2.h5"))
prediction.loadModel()

predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "Santa.png"), result_count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)