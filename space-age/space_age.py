class SpaceAge(object):
    EARTH_SECONDS = 31557600
    EARTH_YEAR = 1
    MERCURY_YEAR = 0.2408467
    VENUS_YEAR = 0.61519726
    MARS_YEAR = 1.8808158
    JUPITER_YEAR = 11.862615
    SATURN_YEAR = 29.447498
    URANUS_YEAR = 84.016846
    NEPTUNE_YEAR = 164.79132

    def __init__(self, seconds: int):
        self.seconds: int = seconds

    def on_earth(self):
        return round(self.seconds / (self.EARTH_SECONDS * self.EARTH_YEAR), 2)

    def on_mercury(self):
        return round(self.seconds / (self.EARTH_SECONDS * self.MERCURY_YEAR), 2)

    def on_venus(self):
        return round(self.seconds / (self.EARTH_SECONDS * self.VENUS_YEAR), 2)

    def on_mars(self):
        return round(self.seconds / (self.EARTH_SECONDS * self.MARS_YEAR), 2)

    def on_jupiter(self):
        return round(self.seconds / (self.EARTH_SECONDS * self.JUPITER_YEAR), 2)

    def on_saturn(self):
        return round(self.seconds / (self.EARTH_SECONDS * self.SATURN_YEAR), 2)

    def on_uranus(self):
        return round(self.seconds / (self.EARTH_SECONDS * self.URANUS_YEAR), 2)

    def on_neptune(self):
        return round(self.seconds / (self.EARTH_SECONDS * self.NEPTUNE_YEAR), 2)
