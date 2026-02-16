# from flask import Flask,request,jsonify 
# import mlflow.pyfunc 
# import pandas as pd  

# app=Flask(__name__) 
# run_id = '3a6f785cd536466d931010c82ca86f22'
# model= mlflow.pyfunc.load_model('runs:/3a6f785cd536466d931010c82ca86f22/iris_model')
# # print(model)

# @app.route('/')
# def home():
#     return {'message':'Welcome Mlflow'}

# @app.route('/predict',methods=['GET','POST'])
# def predict():
#     data=request.json  
#     df=pd.DataFrame([data])
#     predictions = model.predict(df)     
#     return jsonify({'predictions':int(predictions[0])})

# if __name__=='__main__':
#     app.run(port=5001)