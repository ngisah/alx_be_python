import sys
from bank_account import BankAccount

def main():
    """
    Main function to handle command-line arguments and perform banking operations.
    """
    # Create a BankAccount instance with a starting balance of $100
    account = BankAccount(100) 
    
    # Check if a command is provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>[:<amount>]")
        print("Commands: deposit:<amount>, withdraw:<amount>, display")
        sys.exit(1)

    # Parse the command and optional amount from the command-line argument
    parts = sys.argv[1].split(':')
    command = parts[0]
    
    # Handle the 'display' command which has no amount
    if command == "display":
        account.display_balance()
        return # Exit after displaying balance

    # Check for commands that require an amount
    if len(parts) < 2:
        print(f"Error: The '{command}' command requires an amount.")
        print(f"Example: python main-0.py {command}:50")
        sys.exit(1)

    try:
        amount = float(parts[1])
    except ValueError:
        print("Error: Invalid amount. Please enter a numeric value.")
        sys.exit(1)

    # Execute the command
    if command == "deposit":
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
        account.display_balance()
    elif command == "withdraw":
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
        account.display_balance()
    else:
        print("Invalid command. Use 'deposit', 'withdraw', or 'display'.")

if __name__ == "__main__":
    main()
