import vehicles
from Input import Input

# drone = vehicles.Drone(
#     Input('Имя дрона').str(),
#     Input('Мощность').float(),
#     Input('Грузоподъёмность').float()
#     vehicles.Vector3(0, 0, 0)
# )
# car = vehicles.Car(
#     Input('Имя машины').str(),
#     Input('Мощность').float(),
#     vehicles.Vector3(0, 0, 0)
# )
drone = vehicles.Drone("Д1", 10, 100)
car = vehicles.Car("М1", 1000)

while True:
    try:
        n = Input('Что сделать с дроном (1-6), машиной(7-8)?').natural()
        match n:
            case 1:
                print(drone)
            case 2:
                t = Input('Время').float()
                x = Input('x').float()
                y = Input('y').float()
                z = Input('z').float()
                drone.drive(t, vehicles.Vector3(x, y, z))
            case 3:
                x = Input('x').float()
                y = Input('y').float()
                z = Input('z').float()
                drone.park(vehicles.Vector3(x, y, z))
            case 4:
                drone.payload = Input("Грузоподъёмность новая").natural()
            case 5:
                drone.load(Input("Вес").natural(), Input("Название").str())
            case 6:
                drone.upload()
            case 7:
                print(car)
            case 8:
                car.refill()
    except ValueError as e:
        print(e)
