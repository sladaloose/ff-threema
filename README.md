# ff-threema
Script to push messages to Threema Gateway

## Local environment

- Configure the environment variables, see `.env_template`; Make them available in a `.env`-file
- Use Python3; if not available, install it (`sudo apt-get install python3 python3-pip`)
- Create virtual environment `python3 -m venv ff-threema`
- Activate virtual environment `source ff-threema/bin/activate`
- Run `pip install threema.gateway`
- Install "libsodium" as mentioned on https://download.libsodium.org/doc/ for your operating system
    - On **Mac**: `brew install libsodium`
    - On **Ubuntu**:
        - `sudo apt-get update -y`
        - `sudo apt-get install -y libsodium-dev`
    - On **Windows**:
        - Download the latest `libsodium-X.Y.Z-msvc.zip` from https://download.libsodium.org/libsodium/releases/
        - From the downloaded zip file, extract the `Win32/Release/v120/dynamic/libsodium.dll` file to somewhere
        - Copy `libsodium.dll` to ?`C:\Windows\System32\sodium.dll`. If you are using x86 version of Ruby on Win10 x64, you should copy library to `C:\Windows\SysWOW64\sodium.dll` instead.

- Run `pip install -U python-dotenv`

Note: To disable virtual environment call `deactivate`