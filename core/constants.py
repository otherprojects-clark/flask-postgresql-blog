from arrow import utcnow
from colorama import Fore, Style

DATE = utcnow().format('MMMM DD, YYYY')

success = Fore.GREEN + Style.BRIGHT
critical = Fore.RED + Style.BRIGHT

reset = Fore.RESET
reset_all = Style.RESET_ALL