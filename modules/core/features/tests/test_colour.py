import pytest

from modules.core.features import colour


class TestHex:

    @pytest.mark.parametrize(
        "kwargs, _error",
        [
            (True, TypeError),
        ],
    )
    def test_raises(self, kwargs, _error):
        with pytest.raises(_error):
            colour.hex_to_rgb(**kwargs)


class TestRGC:

    @pytest.mark.parametrize(
        "kwargs, _error",
        [
            ((True, True, True), TypeError),
        ],
    )
    def test_raises(self, kwargs, _error):
        with pytest.raises(_error):
            colour.rgb_to_hex(**kwargs)


class TestRandom:

    @pytest.mark.parametrize(
        "kwargs, _error",
        [
            ('test', TypeError),
        ],
    )
    def test_raises(self, kwargs, _error):
        with pytest.raises(_error):
            colour.rgb_to_hex(**kwargs)