# Deactivate current conda environment
# Usage: dac
alias dac='conda deactivate'

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

# Create conda environment(s) from .yml / .yaml file(s) or CLI
# Usage (with file(s)): mkenv [file1] [file2] ... [fileN]
# Usage (without file(s)): mkenv [env_name] [package1] [package2] ... [packageN]
mkenv() {
   if ask "Create environment(s) from file(s)"; then
      if [ $# == 0 ]; then
         conda env create
      
      else
         for file in "$@"; do
            [ -f "$file" ] && conda env create -f "$file" ||
            echo "ERROR: $file doesn't exist."
         done
      fi
      
   else
      if [ $# == 0 ]; then
         echo "ERROR: Invalid number of args. Must include:"
         echo "	* New env's name"
         echo "	* [OPTIONAL] New env's package(s)"
         
      else
         conda create -n "$@"
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

# Export [explicit] spec file for building identical conda environments
# Usage: exp [file]
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