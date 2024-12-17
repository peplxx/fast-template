echo "Installing dependencies..."
./deploy/dependencies.sh
clear

# Check for --force argument
FORCE=false
for arg in "$@"; do
    if [ "$arg" == "--force" ]; then
        FORCE=true
    fi
done

# Check if .env file exists
if [ ! -f ".env" ] || [ "$FORCE" == true ]; then
    echo "Creating environment..."
    # Command to create environment
    make env
    echo "Please, fill env file and run make run-prod command"

else
    clear
    echo "All is done! Running production..."
    make run-prod
fi


