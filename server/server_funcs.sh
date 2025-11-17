# function to set up the planner project
# Assumes the project is located at ~/planner, and dependencies are installed
#     (npm, git, venv created and loaded with requirements.txt, sqlite3)
# Usage: 
#  planner -f|--frontend          # run only the frontend
#  planner -d|--dev               # run the app in dev mode
#  planner -e|--edit              # open neovim in the project directory
#  planner -db                    # open the sqlite3 database
#  planner --update               # update the app from git, install 
#                                 # new dependencies, rebuild frontend, 
#                                 # and restart services
function planner() {
    cd ~/planner || return
    # if -f --frontend is provided, run only the frontend
    if [[ "$1" == "-f" || "$1" == "--frontend" ]]; then
        cd frontend || return
        npm run dev
        return
    fi
    # if -d --dev is provided, run it it in dev mode
    if [[ "$1" == "-d" || "$1" == "--dev" ]]; then
        source venv/bin/activate
        python dev.py
    fi
    # if -e --edit is provided, open neovim
    if [[ "$1" == "-e" || "$1" == "--edit" ]]; then
        source venv/bin/activate
        nvim
        return
    fi
    # if -db is provided, open the database
    if [[ "$1" == "-db" ]]; then
        sqlite3 data/database.db
        return
    fi
    # if --update is provided, update the app
    if [[ "$1" == "--update" ]]; then
        # pull the latest update
        git pull
        # ensure any new dependencies are pulled
        activate
        pip install -r requirements.txt
        # restart the service
        sudo systemctl restart planner
        # rebuild the frontend
        cd frontend
        npm run build
        # replace the build nginx is looking at
        sudo rm -rf /var/www/planner
        sudo cp -r dist /var/www/planner
        # restart nginx
        sudo systemctl restart nginx
    fi
}
