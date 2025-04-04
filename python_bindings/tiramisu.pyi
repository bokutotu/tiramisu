from typing import Any, ClassVar, List

from typing import overload

a_input: argument_t
a_output: argument_t
a_temporary: argument_t
arch_cpu: hardware_architecture_t
arch_flexnlp: hardware_architecture_t
arch_nvidia_gpu: hardware_architecture_t
e_none: expr_t
e_op: expr_t
e_sync: expr_t
e_val: expr_t
e_var: expr_t
o_abs: op_t
o_access: op_t
o_acos: op_t
o_acosh: op_t
o_add: op_t
o_address: op_t
o_address_of: op_t
o_allocate: op_t
o_asin: op_t
o_asinh: op_t
o_atan: op_t
o_atanh: op_t
o_buffer: op_t
o_call: op_t
o_cast: op_t
o_ceil: op_t
o_cond: op_t
o_cos: op_t
o_cosh: op_t
o_div: op_t
o_dummy: op_t
o_eq: op_t
o_expo: op_t
o_floor: op_t
o_free: op_t
o_ge: op_t
o_gt: op_t
o_le: op_t
o_left_shift: op_t
o_lerp: op_t
o_lin_index: op_t
o_log: op_t
o_logical_and: op_t
o_logical_not: op_t
o_logical_or: op_t
o_lt: op_t
o_max: op_t
o_memcpy: op_t
o_min: op_t
o_minus: op_t
o_mod: op_t
o_mul: op_t
o_ne: op_t
o_none: op_t
o_right_shift: op_t
o_round: op_t
o_select: op_t
o_sin: op_t
o_sinh: op_t
o_sqrt: op_t
o_sub: op_t
o_tan: op_t
o_tanh: op_t
o_trunc: op_t
o_type: op_t
p_async: primitive_t
p_boolean: primitive_t
p_float32: primitive_t
p_float64: primitive_t
p_int16: primitive_t
p_int32: primitive_t
p_int64: primitive_t
p_int8: primitive_t
p_none: primitive_t
p_uint16: primitive_t
p_uint32: primitive_t
p_uint64: primitive_t
p_uint8: primitive_t
p_void_ptr: primitive_t
p_wait_ptr: primitive_t
r_receiver: rank_t
r_sender: rank_t

class argument_t:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    a_input: ClassVar[argument_t] = ...
    a_output: ClassVar[argument_t] = ...
    a_temporary: ClassVar[argument_t] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class buffer:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(
        self, arg0: str, arg1: List[expr], arg2: primitive_t, arg3: argument_t
    ) -> None: ...
    def allocate_at(self, *args, **kwargs) -> Any: ...
    def dump(self, arg0: bool) -> None: ...
    def get_name(self) -> str: ...

class computation:
    @overload
    def __init__(self, arg0: str, arg1, arg2: expr) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1, arg2: primitive_t) -> None: ...
    @overload
    def __init__(self, arg0, arg1: primitive_t) -> None: ...
    @overload
    def after(self, arg0: computation, arg1) -> None: ...
    @overload
    def after(self, arg0: computation, arg1: int) -> None: ...
    def after_low_level(self, arg0: computation, arg1: int) -> None: ...
    def cache_shared(
        self, arg0: computation, arg1, arg2: List[int], arg3: List[expr], arg4: bool
    ) -> computation: ...
    def dump(self) -> None: ...
    def get_buffer(self) -> buffer: ...
    @overload
    def gpu_tile(self, arg0, arg1, arg2: int, arg3: int) -> None: ...
    @overload
    def gpu_tile(self, arg0, arg1, arg2: int, arg3: int, arg4, arg5, arg6, arg7) -> None: ...
    @overload
    def gpu_tile(self, arg0, arg1, arg2, arg3: int, arg4: int, arg5: int) -> None: ...
    @overload
    def gpu_tile(
        self,
        arg0,
        arg1,
        arg2,
        arg3: int,
        arg4: int,
        arg5: int,
        arg6,
        arg7,
        arg8,
        arg9,
        arg10,
        arg11,
    ) -> None: ...
    def parallelize(self, arg0) -> None: ...
    def set_expression(self, arg0: expr) -> None: ...
    @overload
    def split(self, arg0, arg1: int) -> None: ...
    @overload
    def split(self, arg0, arg1: int, arg2, arg3) -> None: ...
    @overload
    def split(self, arg0: int, arg1: int) -> None: ...
    @overload
    def store_in(self, arg0: buffer) -> None: ...
    @overload
    def store_in(self, arg0: buffer, arg1: List[expr]) -> None: ...
    @overload
    def then(self, arg0: computation, arg1) -> computation: ...
    @overload
    def then(self, arg0: computation, arg1: int) -> computation: ...
    @overload
    def tile(self, arg0, arg1, arg2: int, arg3: int) -> None: ...
    @overload
    def tile(self, arg0, arg1, arg2: int, arg3: int, arg4, arg5, arg6, arg7) -> None: ...
    @overload
    def tile(self, arg0, arg1, arg2, arg3: int, arg4: int, arg5: int) -> None: ...
    @overload
    def tile(
        self,
        arg0,
        arg1,
        arg2,
        arg3: int,
        arg4: int,
        arg5: int,
        arg6,
        arg7,
        arg8,
        arg9,
        arg10,
        arg11,
    ) -> None: ...
    @overload
    def tile(self, arg0: int, arg1: int, arg2: int, arg3: int) -> None: ...
    @overload
    def tile(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...
    def __getitem__(self, arg0: List[expr]) -> expr: ...

class constant(computation):
    @overload
    def __init__(self, arg0: str, arg1: expr) -> None: ...
    @overload
    def __init__(
        self, arg0: str, arg1: expr, arg2: primitive_t, arg3: bool, arg4: computation, arg5: int
    ) -> None: ...

class expr:
    __hash__: ClassVar[None] = ...
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: primitive_t) -> None: ...
    @overload
    def __init__(self, arg0: int) -> None: ...
    @overload
    def __init__(self, arg0: float) -> None: ...
    @overload
    def __init__(self, arg0) -> None: ...
    @overload
    def __init__(self, arg0: op_t, arg1: primitive_t, arg2: expr) -> None: ...
    @overload
    def __init__(self, arg0: op_t, arg1: expr) -> None: ...
    @overload
    def __init__(self, arg0: op_t, arg1: str) -> None: ...
    @overload
    def __init__(self, arg0: op_t, arg1: expr, arg2: expr) -> None: ...
    @overload
    def __init__(self, arg0: op_t, arg1: expr, arg2: expr, arg3: expr) -> None: ...
    @overload
    def __init__(self, arg0: op_t, arg1: str, arg2: List[expr], arg3: primitive_t) -> None: ...
    def cast(self, arg0: primitive_t) -> expr: ...
    def dump(self) -> None: ...
    def get_double_val(self) -> float: ...
    def get_float32_value(self) -> float: ...
    def get_float64_value(self) -> float: ...
    def get_int16_value(self) -> int: ...
    def get_int32_value(self) -> int: ...
    def get_int64_value(self) -> int: ...
    def get_int8_value(self) -> int: ...
    def get_int_val(self) -> int: ...
    def get_name(self) -> str: ...
    def get_uint16_value(self) -> int: ...
    def get_uint32_value(self) -> int: ...
    def get_uint64_value(self) -> int: ...
    def get_uint8_value(self) -> int: ...
    def is_equal(self, arg0: expr) -> bool: ...
    def logical_not(self) -> expr: ...
    def set_name(self, arg0: str) -> None: ...
    def __add__(self, arg0: expr) -> expr: ...
    def __div__(self, arg0: expr) -> expr: ...
    def __eq__(self, arg0: expr) -> expr: ...
    def __ge__(self, arg0: expr) -> expr: ...
    def __gt__(self, arg0: expr) -> expr: ...
    def __le__(self, arg0: expr) -> expr: ...
    def __lshift__(self, arg0: expr) -> expr: ...
    def __lt__(self, arg0: expr) -> expr: ...
    def __mod__(self, arg0: expr) -> expr: ...
    def __mul__(self, arg0: expr) -> expr: ...
    def __ne__(self, arg0: expr) -> expr: ...
    def __neg__(self) -> expr: ...
    def __radd__(self, arg0: expr) -> expr: ...
    def __rdiv__(self, arg0: expr) -> expr: ...
    def __req__(self, arg0: expr) -> expr: ...
    def __rge__(self, arg0: expr) -> expr: ...
    def __rgt__(self, arg0: expr) -> expr: ...
    def __rle__(self, arg0: expr) -> expr: ...
    def __rlshift__(self, arg0: expr) -> expr: ...
    def __rlt__(self, arg0: expr) -> expr: ...
    def __rmod__(self, arg0: expr) -> expr: ...
    def __rmul__(self, arg0: expr) -> expr: ...
    def __rne__(self, arg0: expr) -> expr: ...
    def __rrshift__(self, arg0: expr) -> expr: ...
    def __rshift__(self, arg0: expr) -> expr: ...
    def __rsub__(self, arg0: expr) -> expr: ...
    def __rtruediv__(self, arg0: expr) -> expr: ...
    def __sub__(self, arg0: expr) -> expr: ...
    def __truediv__(self, arg0: expr) -> expr: ...

class expr_t:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    e_none: ClassVar[expr_t] = ...
    e_op: ClassVar[expr_t] = ...
    e_sync: ClassVar[expr_t] = ...
    e_val: ClassVar[expr_t] = ...
    e_var: ClassVar[expr_t] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class function:
    def __init__(self, arg0: str) -> None: ...
    def codegen(self, arg0: List[buffer], arg1: str, arg2: bool, arg3: bool) -> None: ...
    def dump(self, arg0: bool) -> None: ...
    def dump_halide_stmt(self) -> None: ...
    def gen_c_code(self) -> None: ...
    def pycodegen(self, arg0: List[buffer], arg1: str, arg2: bool) -> None: ...

class hardware_architecture_t:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    arch_cpu: ClassVar[hardware_architecture_t] = ...
    arch_flexnlp: ClassVar[hardware_architecture_t] = ...
    arch_nvidia_gpu: ClassVar[hardware_architecture_t] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class input(computation):
    @overload
    def __init__(self, arg0: str, arg1: List[var], arg2: primitive_t) -> None: ...
    @overload
    def __init__(self, arg0: List[var], arg1: primitive_t) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: List[str], arg2: List[expr], arg3: primitive_t) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: List[expr], arg2: primitive_t) -> None: ...
    def get_buffer(self) -> buffer: ...
    def get_name(self) -> str: ...
    @overload
    def store_in(self, arg0: buffer) -> None: ...
    @overload
    def store_in(self, arg0: buffer, arg1: List[expr]) -> None: ...

class op_t:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    o_abs: ClassVar[op_t] = ...
    o_access: ClassVar[op_t] = ...
    o_acos: ClassVar[op_t] = ...
    o_acosh: ClassVar[op_t] = ...
    o_add: ClassVar[op_t] = ...
    o_address: ClassVar[op_t] = ...
    o_address_of: ClassVar[op_t] = ...
    o_allocate: ClassVar[op_t] = ...
    o_asin: ClassVar[op_t] = ...
    o_asinh: ClassVar[op_t] = ...
    o_atan: ClassVar[op_t] = ...
    o_atanh: ClassVar[op_t] = ...
    o_buffer: ClassVar[op_t] = ...
    o_call: ClassVar[op_t] = ...
    o_cast: ClassVar[op_t] = ...
    o_ceil: ClassVar[op_t] = ...
    o_cond: ClassVar[op_t] = ...
    o_cos: ClassVar[op_t] = ...
    o_cosh: ClassVar[op_t] = ...
    o_div: ClassVar[op_t] = ...
    o_dummy: ClassVar[op_t] = ...
    o_eq: ClassVar[op_t] = ...
    o_expo: ClassVar[op_t] = ...
    o_floor: ClassVar[op_t] = ...
    o_free: ClassVar[op_t] = ...
    o_ge: ClassVar[op_t] = ...
    o_gt: ClassVar[op_t] = ...
    o_le: ClassVar[op_t] = ...
    o_left_shift: ClassVar[op_t] = ...
    o_lerp: ClassVar[op_t] = ...
    o_lin_index: ClassVar[op_t] = ...
    o_log: ClassVar[op_t] = ...
    o_logical_and: ClassVar[op_t] = ...
    o_logical_not: ClassVar[op_t] = ...
    o_logical_or: ClassVar[op_t] = ...
    o_lt: ClassVar[op_t] = ...
    o_max: ClassVar[op_t] = ...
    o_memcpy: ClassVar[op_t] = ...
    o_min: ClassVar[op_t] = ...
    o_minus: ClassVar[op_t] = ...
    o_mod: ClassVar[op_t] = ...
    o_mul: ClassVar[op_t] = ...
    o_ne: ClassVar[op_t] = ...
    o_none: ClassVar[op_t] = ...
    o_right_shift: ClassVar[op_t] = ...
    o_round: ClassVar[op_t] = ...
    o_select: ClassVar[op_t] = ...
    o_sin: ClassVar[op_t] = ...
    o_sinh: ClassVar[op_t] = ...
    o_sqrt: ClassVar[op_t] = ...
    o_sub: ClassVar[op_t] = ...
    o_tan: ClassVar[op_t] = ...
    o_tanh: ClassVar[op_t] = ...
    o_trunc: ClassVar[op_t] = ...
    o_type: ClassVar[op_t] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class primitive_t:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    p_async: ClassVar[primitive_t] = ...
    p_boolean: ClassVar[primitive_t] = ...
    p_float32: ClassVar[primitive_t] = ...
    p_float64: ClassVar[primitive_t] = ...
    p_int16: ClassVar[primitive_t] = ...
    p_int32: ClassVar[primitive_t] = ...
    p_int64: ClassVar[primitive_t] = ...
    p_int8: ClassVar[primitive_t] = ...
    p_none: ClassVar[primitive_t] = ...
    p_uint16: ClassVar[primitive_t] = ...
    p_uint32: ClassVar[primitive_t] = ...
    p_uint64: ClassVar[primitive_t] = ...
    p_uint8: ClassVar[primitive_t] = ...
    p_void_ptr: ClassVar[primitive_t] = ...
    p_wait_ptr: ClassVar[primitive_t] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class rank_t:
    __members__: ClassVar[dict] = ...  # read-only
    __entries: ClassVar[dict] = ...
    r_receiver: ClassVar[rank_t] = ...
    r_sender: ClassVar[rank_t] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class sync(expr):
    def __init__(self) -> None: ...

class var(expr):
    @overload
    def __init__(self, arg0: primitive_t, arg1: str) -> None: ...
    @overload
    def __init__(self, arg0: str) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: expr, arg2: expr) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def dump(self) -> None: ...
    def get_lower(self) -> expr: ...
    def get_name(self) -> str: ...
    def get_upper(self) -> expr: ...

def allocate(arg0) -> expr: ...
@overload
def codegen(
    arguments: List[buffer], obj_filename: str, gen_cuda_stmt: bool = ..., gen_python: bool = ...
) -> None: ...
@overload
def codegen(
    arguments: List[buffer],
    obj_filename: str,
    gen_architecture_flag: hardware_architecture_t,
    gen_python: bool = ...,
) -> None: ...
def cuda_stream_synchronize() -> expr: ...
def get_implicit_function(*args, **kwargs) -> Any: ...
def init(arg0: str) -> None: ...
def memcpy(arg0, arg1) -> expr: ...
@overload
def pycodegen(arg0: List[buffer], arg1: str, arg2: bool) -> None: ...
@overload
def pycodegen(arg0: List[buffer], arg1: str, arg2: hardware_architecture_t, arg3: bool) -> None: ...
