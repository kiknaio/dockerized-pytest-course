from scripts.chp2.video3.mapmaker_exceptions_start import Point
import pytest


def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long() == (14.7167, 17.4677)


# Handle invalid coordinates
def test_invalid_point_generation():
    with pytest.raises(ValueError) as exp:
        Point("Buenos Aires", 12.12331, -555.080268)
    assert str(exp.value) == 'Invalide latitude, longitude combination'


# Handle invalid data types
def test_city_name_generation():
    with pytest.raises(TypeError) as exp:
        Point(123, 41.716667, 44.783333)
    assert str(exp.value) == 'Invalid data type for city name'
