// Lean compiler output
// Module: BdiPolytope
// Imports: public import Init public meta import Init
#include <lean/lean.h>
#if defined(__clang__)
#pragma clang diagnostic ignored "-Wunused-parameter"
#pragma clang diagnostic ignored "-Wunused-label"
#elif defined(__GNUC__) && !defined(__CLANG__)
#pragma GCC diagnostic ignored "-Wunused-parameter"
#pragma GCC diagnostic ignored "-Wunused-label"
#pragma GCC diagnostic ignored "-Wunused-but-set-variable"
#endif
#ifdef __cplusplus
extern "C" {
#endif
lean_object* lean_nat_to_int(lean_object*);
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
lean_object* lean_nat_sub(lean_object*, lean_object*);
lean_object* lean_int_sub(lean_object*, lean_object*);
lean_object* lean_int_mul(lean_object*, lean_object*);
lean_object* lean_int_add(lean_object*, lean_object*);
static lean_once_cell_t lp_bdi_x2dpolytope_BdiPolytope_P___closed__0_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_bdi_x2dpolytope_BdiPolytope_P___closed__0;
static lean_once_cell_t lp_bdi_x2dpolytope_BdiPolytope_P___closed__1_once = LEAN_ONCE_CELL_INITIALIZER;
static lean_object* lp_bdi_x2dpolytope_BdiPolytope_P___closed__1;
LEAN_EXPORT lean_object* lp_bdi_x2dpolytope_BdiPolytope_P(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_bdi_x2dpolytope_BdiPolytope_P___boxed(lean_object*, lean_object*);
static lean_object* _init_lp_bdi_x2dpolytope_BdiPolytope_P___closed__0(void){
_start:
{
lean_object* v_zero_1_; lean_object* v___x_2_; 
v_zero_1_ = lean_unsigned_to_nat(0u);
v___x_2_ = lean_nat_to_int(v_zero_1_);
return v___x_2_;
}
}
static lean_object* _init_lp_bdi_x2dpolytope_BdiPolytope_P___closed__1(void){
_start:
{
lean_object* v___x_3_; lean_object* v___x_4_; 
v___x_3_ = lean_unsigned_to_nat(2u);
v___x_4_ = lean_nat_to_int(v___x_3_);
return v___x_4_;
}
}
LEAN_EXPORT lean_object* lp_bdi_x2dpolytope_BdiPolytope_P(lean_object* v_c_5_, lean_object* v_x_6_){
_start:
{
lean_object* v_zero_7_; uint8_t v_isZero_8_; 
v_zero_7_ = lean_unsigned_to_nat(0u);
v_isZero_8_ = lean_nat_dec_eq(v_x_6_, v_zero_7_);
if (v_isZero_8_ == 1)
{
lean_object* v___x_9_; 
lean_dec_ref(v_c_5_);
v___x_9_ = lean_obj_once(&lp_bdi_x2dpolytope_BdiPolytope_P___closed__0, &lp_bdi_x2dpolytope_BdiPolytope_P___closed__0_once, _init_lp_bdi_x2dpolytope_BdiPolytope_P___closed__0);
return v___x_9_;
}
else
{
lean_object* v_B_10_; lean_object* v_T_11_; lean_object* v_one_12_; lean_object* v_n_13_; lean_object* v___x_14_; lean_object* v___x_15_; lean_object* v___x_16_; lean_object* v___x_17_; lean_object* v___x_18_; lean_object* v___x_19_; lean_object* v___x_20_; 
v_B_10_ = lean_ctor_get(v_c_5_, 1);
lean_inc_ref(v_B_10_);
v_T_11_ = lean_ctor_get(v_c_5_, 2);
lean_inc_ref(v_T_11_);
v_one_12_ = lean_unsigned_to_nat(1u);
v_n_13_ = lean_nat_sub(v_x_6_, v_one_12_);
v___x_14_ = lp_bdi_x2dpolytope_BdiPolytope_P(v_c_5_, v_n_13_);
v___x_15_ = lean_obj_once(&lp_bdi_x2dpolytope_BdiPolytope_P___closed__1, &lp_bdi_x2dpolytope_BdiPolytope_P___closed__1_once, _init_lp_bdi_x2dpolytope_BdiPolytope_P___closed__1);
lean_inc(v_n_13_);
v___x_16_ = lean_apply_1(v_B_10_, v_n_13_);
v___x_17_ = lean_apply_1(v_T_11_, v_n_13_);
v___x_18_ = lean_int_sub(v___x_16_, v___x_17_);
lean_dec(v___x_17_);
lean_dec(v___x_16_);
v___x_19_ = lean_int_mul(v___x_15_, v___x_18_);
lean_dec(v___x_18_);
v___x_20_ = lean_int_add(v___x_14_, v___x_19_);
lean_dec(v___x_19_);
lean_dec(v___x_14_);
return v___x_20_;
}
}
}
LEAN_EXPORT lean_object* lp_bdi_x2dpolytope_BdiPolytope_P___boxed(lean_object* v_c_21_, lean_object* v_x_22_){
_start:
{
lean_object* v_res_23_; 
v_res_23_ = lp_bdi_x2dpolytope_BdiPolytope_P(v_c_21_, v_x_22_);
lean_dec(v_x_22_);
return v_res_23_;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_Init(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_bdi_x2dpolytope_BdiPolytope(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
