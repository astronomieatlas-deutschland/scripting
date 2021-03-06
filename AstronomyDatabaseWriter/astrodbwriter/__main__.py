import database
from crawler import gdp
from database.planetarium import *


def generate_test_data():
    return [Planetarium(institution="Sternwarte mit Planetarium Dieterskirchen",
                        location="Dieterskirchen",
                        address="Neunburger Straße 24, 92542 Dieterskirchen",
                        country_code="DE",
                        latitude=49.411389,
                        longitude=12.404722,
                        website="www.sternwarte-dieterskirchen.de",
                        dome_diameter=6,
                        dome_tilt=0,
                        mobility=MobilityType.STATIONARY,
                        seats=25,
                        seat_arrangement=SeatArrangement.CONCENTRIC,
                        optomechanical_projector="Polaris MK1",
                        optomechanical_projector_manufacturer=OptomechanicalProjectorManufacturer.BERGER,
                        fulldome_software="DigitalSky 2",
                        fulldome_software_manufacturer=FulldomeSoftwareManufacturer.SKY_SKAN,
                        opening_year=2014,
                        visitors_per_year=3000),
            Planetarium(institution="Nicolaus-Copernicus Planetarium Nürnberg",
                        location="Nürnberg",
                        address="Am Plärrer 41, 90429 Nürnberg",
                        country_code="DE",
                        latitude=49.447778,
                        longitude=11.062778,
                        website="www.planetarium-nuernberg.de",
                        dome_diameter=18,
                        dome_tilt=0,
                        mobility=MobilityType.STATIONARY,
                        seats=200,
                        seat_arrangement=SeatArrangement.CONCENTRIC,
                        optomechanical_projector="Zeiss Modell V",
                        optomechanical_projector_manufacturer=OptomechanicalProjectorManufacturer.ZEISS,
                        fulldome_software="DigitalSky 2",
                        fulldome_software_manufacturer=FulldomeSoftwareManufacturer.SKY_SKAN,
                        opening_year=1961,
                        visitors_per_year=80000
                        ),
            Planetarium(institution="Planetarium Ursensollen",
                        location="Ursensollen",
                        address="Allmannsberger Weg 20, 92289 Ursensollen",
                        country_code="DE",
                        latitude=49.398056,
                        longitude=11.74,
                        website="www.planetarium-ursensollen.de",
                        dome_diameter=6.6,
                        dome_tilt=15,
                        mobility=MobilityType.STATIONARY,
                        seats=30,
                        seat_arrangement=SeatArrangement.UNIDIRECTIONAL,
                        optomechanical_projector=None,
                        optomechanical_projector_manufacturer=None,
                        fulldome_software="DigitalSky Dark Matter",
                        fulldome_software_manufacturer=FulldomeSoftwareManufacturer.SKY_SKAN,
                        opening_year=2019,
                        visitors_per_year=database.UNKNOWN
                        )]


if __name__ == '__main__':
    print("Hello World! This is the astronomy database writer.")
    database.publish_database(gdp.retrieve_data())
