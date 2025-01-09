import subprocess

# Function to create a user
def create_user(username, password):
    try:
        # Create the user
        command = f"sudo useradd {username}"
        subprocess.run(command, check=True, shell=True)

        # Set the password
        command = f"echo '{username}:{password}' | sudo chpasswd"
        subprocess.run(command, check=True, shell=True)

        print(f"User {username} created successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error creating user: {e}")

# Function to list all users
def list_users():
    try:
        command = "cut -d: -f1 /etc/passwd"
        result = subprocess.run(command, check=True, shell=True, capture_output=True, text=True)
        users = result.stdout.splitlines()
        print("List of users:")
        for user in users:
            print(user)
    except subprocess.CalledProcessError as e:
        print(f"Error listing users: {e}")

# Function to delete a user
def delete_user(username):
    try:
        # The command to delete the user and remove their home directory
        command = f"sudo userdel -r {username}"

        # The `subprocess.run()` will prompt for the sudo password, unless passwordless sudo is configured
        subprocess.run(command, shell=True, check=True)

        print(f"User {username} deleted successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting user: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Function to create a user
def create_user(username, password):
    try:
        # Create the user
        command = f"sudo useradd {username}"
        subprocess.run(command, check=True, shell=True)

        # Set the password
        command = f"echo '{username}:{password}' | sudo chpasswd"
        subprocess.run(command, check=True, shell=True)

        print(f"User {username} created successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error creating user: {e}")

# Function to list all users
def list_users():
    try:
        command = "cut -d: -f1 /etc/passwd"
        result = subprocess.run(command, check=True, shell=True, capture_output=True, text=True)
        users = result.stdout.splitlines()
        print("List of users:")
        for user in users:
            print(user)
    except subprocess.CalledProcessError as e:
        print(f"Error listing users: {e}")

# Function to delete a user
def delete_user(username):
    try:
        # The command to delete the user and remove their home directory
        command = f"sudo userdel -r {username}"
        
        # The `subprocess.run()` will prompt for the sudo password, unless passwordless sudo is configured
        subprocess.run(command, shell=True, check=True)

        print(f"User {username} deleted successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting user: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Function to create a user
def create_user(username, password):
    try:
        # Create the user
        command = f"sudo useradd {username}"
        subprocess.run(command, check=True, shell=True)

        # Set the password
        command = f"echo '{username}:{password}' | sudo chpasswd"
        subprocess.run(command, check=True, shell=True)

        print(f"User {username} created successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error creating user: {e}")

# Function to list all users
def list_users():
    try:
        command = "cut -d: -f1 /etc/passwd"
        result = subprocess.run(command, check=True, shell=True, capture_output=True, text=True)
        users = result.stdout.splitlines()
        print("List of users:")
        for user in users:
            print(user)
    except subprocess.CalledProcessError as e:
        print(f"Error listing users: {e}")

# Function to delete a user
def delete_user(username):
    try:
        # The command to delete the user and remove their home directory
        command = f"sudo userdel -r {username}"
        
        # The `subprocess.run()` will prompt for the sudo password, unless passwordless sudo is configured
        subprocess.run(command, shell=True, check=True)

        print(f"User {username} deleted successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting user: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Function to create a user
def create_user(username, password):
    try:
        # Create the user
        command = f"sudo useradd {username}"
        subprocess.run(command, check=True, shell=True)

        # Set the password
        command = f"echo '{username}:{password}' | sudo chpasswd"
        subprocess.run(command, check=True, shell=True)

        print(f"User {username} created successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error creating user: {e}")

# Function to list all users
def list_users():
    try:
        command = "cut -d: -f1 /etc/passwd"
        result = subprocess.run(command, check=True, shell=True, capture_output=True, text=True)
        users = result.stdout.splitlines()
        print("List of users:")
        for user in users:
            print(user)
    except subprocess.CalledProcessError as e:
        print(f"Error listing users: {e}")

# Function to delete a user
def delete_user(username):
    try:
        command = f"sudo userdel -r {username}"  # -r flag removes the user'
        # Use 'echo' to pass the password automatically
        subprocess.run(f"echo YOUR_SUDO_PASSWORD | {command}", shell=True, check=True)
        print(f"User {username} deleted successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting user: {e}")
        print("Exit status:", e.returncode)
        print("Error message:", e.stderr)

# Function to change user password
def change_password(username, new_password):
    try:
        command = f"echo '{username}:{new_password}' | sudo chpasswd"
        subprocess.run(command, check=True, shell=True)
        print(f"Password for {username} changed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error changing password for {username}: {e}")

# Main menu for the script
def main():
    while True:
        print("\nUser Management Script")
        print("1. Create User")
        print("2. List Users")
        print("3. Delete User")
        print("4. Change Password")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            create_user(username, password)
        elif choice == "2":
            list_users()
        elif choice == "3":
           username = input("Enter the username to delete: ")
           delete_user(username)
        elif choice == "4":
           username = input("Enter the username to change password: ")
           new_password = input("Enter the new password: ")
           change_password(username, new_password)
        elif choice == "5": 
           print("Exting...")
           break
        else:
           print("Invalid choice. Try again.")

if __name__== "__main__":
    main()


