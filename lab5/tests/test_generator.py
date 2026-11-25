"""Тесты модуля num_series.generator."""

import pytest

from num_series.generator import (
    _validate_n,
    random_series,
    sine_series,
    outlier_series,
    trend_series,
)


class TestValidateN:
    """Границы и типы входного параметра n."""

    @pytest.mark.parametrize("n", [1, 5, 100, 1000])
    def test_positive_int_passes(self, n):
        _validate_n(n)

    @pytest.mark.parametrize("n", [0, -1, -100])
    def test_zero_and_negative_rejected(self, n):
        with pytest.raises(ValueError, match="положительным целым"):
            _validate_n(n)

    @pytest.mark.parametrize("n", [3.5, -0.1, 1.0000001])
    def test_non_integer_float_rejected(self, n):
        with pytest.raises(ValueError, match="положительным целым"):
            _validate_n(n)

    @pytest.mark.parametrize("n", ["5", "abc", None, [5], {"n": 5}])
    def test_bad_types_rejected(self, n):
        with pytest.raises(ValueError, match="положительным целым"):
            _validate_n(n)

    def test_error_message_contains_repr_and_cause(self):
        with pytest.raises(ValueError) as exc_info:
            _validate_n("abc")
        msg = str(exc_info.value)
        assert "'abc'" in msg
        assert "причина" in msg

    def test_float_integral_passes(self):
        _validate_n(3.0)


class TestRandomSeries:
    def test_length(self):
        assert len(random_series(10, seed=1)) == 10

    def test_reproducible_with_seed(self):
        assert random_series(20, seed=42) == random_series(20, seed=42)

    def test_different_seeds_differ(self):
        assert random_series(20, seed=1) != random_series(20, seed=2)

    def test_within_bounds(self):
        data = random_series(100, low=-5, high=5, seed=0)
        assert all(-5 <= x <= 5 for x in data)

    def test_low_ge_high_raises(self):
        with pytest.raises(ValueError, match="low должно быть меньше high"):
            random_series(5, low=10, high=5)

    def test_invalid_n_raises(self):
        with pytest.raises(ValueError):
            random_series(0)


class TestSineSeries:
    def test_length(self):
        assert len(sine_series(30, seed=0)) == 30

    def test_reproducible(self):
        assert sine_series(30, noise=0.5, seed=7) == sine_series(30, noise=0.5, seed=7)

    def test_zero_noise_is_deterministic_without_seed(self):
        a = sine_series(20, noise=0.0, seed=1)
        b = sine_series(20, noise=0.0, seed=999)
        assert a == b

    def test_amplitude_bounds_without_noise(self):
        data = sine_series(100, amplitude=2.0, noise=0.0)
        assert all(-2.0 - 1e-9 <= x <= 2.0 + 1e-9 for x in data)


class TestTrendSeries:
    def test_linear_without_noise(self):
        data = trend_series(5, start=0, step=2.0, noise=0.0)
        assert data == [0.0, 2.0, 4.0, 6.0, 8.0]

    def test_length(self):
        assert len(trend_series(15, seed=0)) == 15

    def test_reproducible(self):
        assert trend_series(10, noise=0.5, seed=3) == trend_series(10, noise=0.5, seed=3)


class TestOutlierSeries:
    def test_default_length_and_reproducibility(self):
        s1 = outlier_series(seed=42)
        s2 = outlier_series(seed=42)
        assert len(s1) == 1500
        assert s1 == s2
        assert all(isinstance(x, float) for x in s1)

    def test_contains_large_outliers(self):
        data = outlier_series(n=1500, noise_low=-10.0, noise_high=10.0, outlier_scale=10.0, seed=7)
        assert max(data) >= 100.0
        assert min(data) <= -100.0
