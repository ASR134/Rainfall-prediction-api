from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
from pydantic import BaseModel,Field,computed_field
from typing import Annotated
import pickle

# loaded model
with open("rainfall_model.pkl","rb") as f:
    loaded_model = pickle.load(f)

app = FastAPI()

# pydantic model

class user_input(BaseModel):
    
    pressure : Annotated[float, Field(...,description="Pressure of the location",gt=0)]
    temparature : Annotated[float, Field(...,description="Temperature in celcius")]
    humidity : Annotated[float, Field(...,description="relative Humidity in percentage",ge=0,le=100)]
    cloud : Annotated[float, Field(...,description="cloud cover percentage")]
    sunshine : Annotated[float, Field(...,description="number of hours sunshine during the day",ge=0)]
    winddirection : Annotated[float, Field(...,description="wind direction in degress (0 degree = North )")]
    windspeed : Annotated[float, Field(...,description="wind speed in km/h")]
    max_temp : Annotated[float,Field(...)]
    min_temp : Annotated[float,Field(...)]
    
    @computed_field
    @property
    def temp_range(self) -> float:
        range = self.max_temp - self.min_temp
        return range
    

# api endpoint

@app.post("/predict")
def rainfall_prediction(input_data : user_input):
    
    input_df = pd.DataFrame({
        "pressure" : [input_data.pressure],
        "temparature" : [input_data.temparature],
        "humidity" : [input_data.humidity],
        "cloud" : [input_data.cloud],
        "sunshine" : [input_data.sunshine],
        "winddirection" : [input_data.winddirection],
        "windspeed" : [input_data.windspeed],
        "temp_range" : [input_data.temp_range]
        })
    
    trained_model = loaded_model["model"]
    prediction = trained_model.predict(input_df)
    
    if (prediction[0] == 1):
        result = "Rain"
    else:
        result = "No Rain"
        
    return JSONResponse(status_code=200, content={"prediction" : result})
    
    
    
    
    
    