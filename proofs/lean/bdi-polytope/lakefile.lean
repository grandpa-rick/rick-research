import Lake
open Lake DSL

package «bdi-polytope» where
  -- no extra options

lean_lib «BdiPolytope» where
  -- no extra options

@[default_target]
lean_exe «bdi-polytope» where
  root := `Main
