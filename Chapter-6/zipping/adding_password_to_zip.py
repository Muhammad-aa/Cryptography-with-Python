import pyzipper
import os

def add_password_to_existing_zip(existing_zip_path, new_zip_path, password):
    """Add a password to an existing ZIP file by creating a new password-protected ZIP file.

    Args:
    existing_zip_path: Path to the existing ZIP file.
    new_zip_path: Path for the new password-protected ZIP file.
    password: Password for the new ZIP file."""
    with pyzipper.AESZipFile(new_zip_path, 'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as new_zf:
        # set password for the new zip file
        new_zf.setpassword(password.encode('utf-8'))
        # open the existing zip file
        with pyzipper.ZipFile(existing_zip_path, 'r') as existing_zf:
            # iterate over the files in the existing zip file
            for file_name in existing_zf.namelist():
                # read the file from the existing zip file and write it to the new zip file
                with existing_zf.open(file_name) as source_file:
                    new_zf.writestr(file_name, source_file.read())
    print(f"Password-protected ZIP file created at {new_zip_path}")

if __name__ == "__main__":
    import sys
    import getpass
    # Example usage
    existing_zip_path = sys.argv[1]
    # some basic checks
    assert os.path.exists(existing_zip_path), "The provided ZIP file does not exist."
    assert existing_zip_path.endswith('.zip'), "The provided file is not a ZIP file."
    # new zip path is existing zip path with '-protected' appended to it
    new_zip_path = existing_zip_path.split('.')[0] + '-protected.zip'
    # password for the new zip file
    password = getpass.getpass("Enter the password for the new ZIP file: ")
    # add password to the existing zip file
    add_password_to_existing_zip(existing_zip_path, new_zip_path, password)
