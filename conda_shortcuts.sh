# Deactivate current conda environment
# Usage: dac
alias dac='conda deactivate'

# Activate conda environment
# Usage: act [env_name]
act() {
   if [ $# == 1 ]; then
      conda activate "$1"
      
   elif [ $# == 0 ]; then
      conda activate
      
   else
      echo "ERROR: Invalid number of args. At most 1 env name is required."
   fi
}

# Helper function to prompt user for 'Yes' or 'No' response
ask() {
    read -p "$@ (Y/N)? " answer
    case "${answer}" in
    [yY] | [yY][eE][sS])
        true
        ;;
    *)
        false
        ;;
    esac
}

# Create conda environment(s) from .yml file(s) or CLI
#
# mkenv
# mkenv [file1.yml] ... [fileN.yml]
# mkenv [env_name] [package1] ... [packageN]
# mkenv ... [file1.yml] ... [env_name] [package1] ... [packageN] ... [fileN.yml] ...
mkenv() {
   if [ $# == 0 ]; then
      conda env create
      
   else
      cmd=()
      for arg in "$@"; do
         case "${arg}" in *.yml | *.YML | *.yaml | *.YAML)
            if [ ${#cmd[@]} != 0 ]; then
               conda create -n "${cmd[@]}"
               unset cmd
            fi
            
            [ -f "$arg" ] && conda env create -f "$arg" ||
            echo "ERROR: $arg doesn't exist."
            ;;
            
         *)
            cmd+=("${arg}")
            ;;
         esac
      done
      
      if [ ${#cmd[@]} != 0 ]; then
         conda create -n "${cmd[@]}"
      fi
   fi
}

# Delete conda environment(s)
# Usage: rmenv [env1] [env2] ... [envN]
rmenv() {
   for env in "$@"; do
      if ask "Are you sure you want to delete $env"; then
         env_path="$(conda info --base)/envs/$env"
         [ -e "$env_path" ] &&
         conda env remove -n "$env" -y &&
         rm -rf "$env_path" ||
         echo "ERROR: $env doesn't exist."
      fi
   done
}

# Rename conda environment
# Usage: rnenv [curr_env_name] [new_name]
rnenv() {
   if [ $# == 2 ]; then
      if [ "$CONDA_SHLVL" == 0 ]; then
         act
         conda rename -n "$1" "$2"
         dac
         
      else
         conda rename -n "$1" "$2"
      fi
      
   else
      echo "ERROR: Invalid number of args. Must include:"
      echo "	* Env's current name"
      echo "	* Env's new name"
   fi
}

# Copy conda environment
# Usage: cpenv [orig_env_name] [copy's_name]
cpenv() {
   if [ $# == 2 ]; then
      conda create -n "$2" --clone "$1"
      
   else
      echo "ERROR: Invalid number of args. Must include:"
      echo "	* Source env's name"
      echo "	* Env copy's name"
   fi
}

# Export [explicit] spec file for building identical conda environments
# Usage: exp [out_file]
exp() {
   if [ $# == 0 ]; then
      if ask "Export explicit specs"; then
         conda list --explicit > environment.yml
         
      else
         conda env export --from-history > environment.yml
      fi
      
   elif [ $# == 1 ]; then
      if ask "Export explicit specs"; then
         conda list --explicit > "$1"
         
      else
         conda env export --from-history > "$1"
      fi
      
   else
      echo "ERROR: Invalid number of args. At most 1 file name is required."
   fi
}

# Output [explicit] packages in conda environment
# Usage: lsenv
lsenv() {
   if ask "List explicit specs"; then
      conda list --explicit
      
   else
      conda list
   fi
}
