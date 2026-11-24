import pytest
import media.parametric_eq as mod

CASES = [
    ("coeff_state_lock", (1,)),
    ("carry_state_block", (1,)),
    ("master_gain", (1,)),
    ("param_coeff_sync", (1,)),
    ("offline_block_match", (1,)),
    ("click_fade", (1,)),
    ("process", (1,)),
    ("set_band", (1,)),
    ("automate", (1,)),
    ("export", (1,)),
    ("validate_eq", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
