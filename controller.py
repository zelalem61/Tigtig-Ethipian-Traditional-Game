import pygame


class PygameDriver:
    def __init__(self):
        pygame.init()
        self.controller = None

    def connect_controller(self):
        # Initialize the joystick module
        pygame.joystick.init()

        # Check for available controllers
        if pygame.joystick.get_count() == 0:
            print("No controller connected.")
            return False

        # Connect to the first available controller
        self.controller = pygame.joystick.Joystick(0)
        self.controller.init()

        print("Connected to controller:")
        print("Name:", self.controller.get_name())
        print("Axes:", self.controller.get_numaxes())
        print("Buttons:", self.controller.get_numbuttons())

        return True

    def listen_controller(self):
        if self.controller is None:
            print("No controller connected.")
            return

        while True:
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    # Handle axis motion events
                    axis = event.axis
                    value = event.value
                    print("Axis {}: {}".format(axis, value))
                elif event.type == pygame.JOYBUTTONDOWN:
                    # Handle button press events
                    button = event.button
                    print("Button {} pressed".format(button))
                elif event.type == pygame.JOYBUTTONUP:
                    # Handle button release events
                    button = event.button
                    print("Button {} released".format(button))
                elif event.type == pygame.JOYHATMOTION:
                    # Handle hat motion events (e.g., D-pad)
                    hat = event.hat
                    value = event.value
                    print("Hat {}: {}".format(hat, value))


if __name__ == "__main__":
    driver = PygameDriver()
    connected = driver.connect_controller()

    if connected:
        driver.listen_controller()
