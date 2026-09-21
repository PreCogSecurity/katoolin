"""CLI module for Katoolin."""
import sys
import traceback
from katoolin import repo_manager, installer

def main():
    try:
        print("""
  $$\   $$\             $$\                         $$\ $$\           
  $$ | $$  |            $$ |                        $$ |\__|          
  $$ |$$  /  $$$$$$\  $$$$$$\    $$$$$$\   $$$$$$\  $$ |$$\ $$$$$$$\  
  $$$$$  /   \____$$\ \_$$  _|  $$  __$$\ $$  __$$\ $$ |$$ |$$  __$$\ 
  $$  $$<    $$$$$$$ |  \033[1;36mKali linux tools installer\033[1;m |$$ |$$ |$$ |  $$ |
  \033[1;36m$$ |\$$\  $$  __$$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |
  $$ | \$$\ \$$$$$$$ |  \$$$$  |\$$$$$$  |\$$$$$$  |$$ |$$ |$$ |  $$ |
  \__|  \__| \_______|   \____/  \______/  \______/ \__|\__|\__|  \__| V1.1 \033[1;m


  \033[1;32m+ -- -- +=[ Author: LionSec | Maintainer: PreCog Security\033[1;m
  \033[1;32m+ -- -- +=[ 331 Tools \033[1;m
        """)
        
        def inicio1():
            while True:
                print("""
1) Add Kali repositories & Update 
2) View Categories
3) Install classicmenu indicator
4) Install Kali menu
5) Help
                """)
                opcion0 = input("\033[1;36mkat > \033[1;m")
                
                if opcion0 == "1":
                    while True:
                        print("""
1) Add kali linux repositories
2) Update
3) Remove all kali linux repositories
4) View the contents of sources.list file
                        """)
                        repo = input("\033[1;32mWhat do you want to do ?> \033[1;m")
                        if repo == "1":
                            installer.run_command("apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6")
                            repo_manager.add_repositories()
                        elif repo == "2":
                            installer.run_command("apt-get update -m")
                        elif repo == "3":
                            repo_manager.remove_repositories()
                            print(" ")
                            print("\033[1;31mAll kali linux repositories have been deleted !\033[1;m")
                            print(" ")
                        elif repo == "4":
                            print(repo_manager.view_repositories())
                        elif repo in ("back", "gohome"):
                            break
                        else:
                            print("\033[1;31mSorry, that was an invalid command!\033[1;m")
                elif opcion0 == "3":
                    print(""" 
ClassicMenu Indicator is a notification area applet for Ubuntu.
                    """)
                    repo = input("\033[1;32mDo you want to install classicmenu indicator ? [y/n]> \033[1;m")
                    if repo == "y":
                        installer.run_command("add-apt-repository ppa:diesch/testing && apt-get update")
                        installer.run_command("sudo apt-get install classicmenu-indicator")
                elif opcion0 == "4":
                    repo = input("\033[1;32mDo you want to install Kali menu ? [y/n]> \033[1;m")
                    if repo == "y":
                        installer.run_command("apt-get install kali-menu")
                elif opcion0 == "5":
                    print(""" 
****************** +Commands+ ******************

\033[1;32mback\033[1;m 	\033[1;33mGo back\033[1;m
\033[1;32mgohome\033[1;m	\033[1;33mGo to the main menu\033[1;m
                    """)
                elif opcion0 == "2":
                    print("Categories view. Use interactive CLI mode in Ubuntu/Kali environment.")
                elif opcion0 in ("exit", "quit"):
                    sys.exit(0)
                else:
                    print("\033[1;31mSorry, that was an invalid command!\033[1;m")
                    
        inicio1()
    except KeyboardInterrupt:
        print("Shutdown requested...Goodbye...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
    main()
