import ecospolder


def test_version_tuple():
    version_t = ecospolder.__version__
    assert isinstance(version_t, tuple)
