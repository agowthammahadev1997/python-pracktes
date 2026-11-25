class Car:
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.is_engine_started = False
        self.current_speed = 0

    # Start engine
    def start_engine(self):
        self.is_engine_started = True

    # Stop engine
    def stop_engine(self):
        if self.current_speed == 0:
            self.is_engine_started = False
        else:
            print("Cannot stop the engine while moving")

    # Increase speed
    def accelerate(self):
        if not self.is_engine_started:
            print("Car has not started yet")
        else:
            self.current_speed += self.acceleration

            if self.current_speed > self.max_speed:
                self.current_speed = self.max_speed

    # Apply brakes
    def apply_brakes(self):
        self.current_speed -= self.tyre_friction

        if self.current_speed < 0:
            self.current_speed = 0

    # Car horn
    def sound_horn(self):
        if self.is_engine_started:
            print("Beep Beep")
        else:
            print("Car has not started yet")


class Truck(Car):

    def __init__(self, color, max_speed, acceleration,
                 tyre_friction, max_cargo_weight):

        # Calling parent class constructor
        super().__init__(color, max_speed, acceleration, tyre_friction)

        self.max_cargo_weight = max_cargo_weight
        self.load = 0

    # Load cargo
    def load_cargo(self, cargo_weight):

        if self.is_engine_started:
            print("Cannot load cargo during motion")

        elif self.load + cargo_weight > self.max_cargo_weight:
            print(f"Cannot load cargo more than max limit: {self.max_cargo_weight}")

        else:
            self.load += cargo_weight

    # Unload cargo
    def unload_cargo(self, cargo_weight):

        if self.is_engine_started:
            print("Cannot unload cargo during motion")

        else:
            self.load -= cargo_weight

            if self.load < 0:
                self.load = 0

    # Override parent class method
    def sound_horn(self):

        if self.is_engine_started:
            print("Honk Honk")
        else:
            print("Car has not started yet")


# Creating Truck object
truck = Truck("Red", 100, 10, 5, 500)

# Testing truck features
print("Truck Color:", truck.color)
print("Maximum Speed:", truck.max_speed)
print("Maximum Cargo Weight:", truck.max_cargo_weight)
print("Initial Load:", truck.load)
print("Initial Speed:", truck.current_speed)

truck.load_cargo(200)
print("Current Load:", truck.load)

truck.load_cargo(400)

truck.start_engine()
truck.load_cargo(50)

truck.sound_horn()

truck.stop_engine()

truck.unload_cargo(100)
print("Current Load:", truck.load)

truck.start_engine()
truck.accelerate()
print("Current Speed:", truck.cuhasrrent_speed)

truck.sound_horn()
