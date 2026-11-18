import pytest
from game import crowd_steering as mod

CASES = [
    ("radius_grow", "m.dynamic_radius(0.5, 10.0) == approx(0.55)"),
    ("radius_zero", "m.dynamic_radius(0.5, 0.0) == approx(0.5)"),
    ("neighbors_two", "m.neighbor_count([(0.0, 0.0), (1.0, 0.0), (3.0, 0.0)], 0.0, 0.0, 1.5) == 2"),
    ("neighbors_zero", "m.neighbor_count([], 0.0, 0.0, 1.0) == 0"),
    ("speed_half", "m.density_speed(2.0, 10.0) == approx(1.0)"),
    ("replan_true", "m.should_replan(5.0, 3.0) is True"),
    ("replan_false", "m.should_replan(2.0, 3.0) is False"),
    ("local_add", "m.combine_local((1.0, 0.0), (0.0, 1.0)) == (1.0, 1.0)"),
    ("team_value", "m.team_layer(2) == 2"),
    ("terrain_add", "m.terrain_radius(0.5, 0.2) == approx(0.7)"),
    ("turn_clamp", "m.turn_limit(2.0, 1.0) == approx(1.0)"),
    ("turn_inside", "m.turn_limit(0.5, 1.0) == approx(0.5)"),
    ("recovery_remain", "m.recovery(5.0, 3.0) == approx(2.0)"),
    ("steps_three", "m.fixed_steps(0.033, 0.016) == 3"),
    ("speed_zero", "m.density_speed(0.0, 10.0) == approx(0.0)")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
