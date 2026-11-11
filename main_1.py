from fastapi import FastAPI
app = FastAPI()

@app.get("/jam")
def jam(num1 : int, num2 : int):
    return(f"{num1} + {num2} = {num1 + num2}")

@app.get("/menha")
def menha(num_1 : int, num_2 : int):
    return(f"{num_1} - {num_2} = {num_1 - num_2}")

@app.get("/zarb")
def zarb(num_1 : int, num_2 : int):
    return(f"{num_1} * {num_2} = {num_1 * num_2}")

@app.get("/taghsim")
def taghsim(num_1 : int, num_2 : int):
    if num_2 != 0:
        return(f"{num_1} / {num_2} = {num_1 / num_2}")