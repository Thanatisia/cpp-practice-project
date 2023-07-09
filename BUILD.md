# Build/Setup Instructions

## Setup
### Dependencies
- build essential packages
    - Packages
        - make
        - g++
    - In Windows
        + Install 'MinGW-w64' for 64-bit GNU development utilities (i.e. make, gcc, g++ etc)
    - In Linux 
        - Using package manager
            + apt-based
                ```console
                sudo apt install build-essential
                ```
            + pacman-based
                ```console
                sudo pacman -S base-devel
                ```

### Pre-Requisites


### Manual Build/Compile from Source
- Using g++
    ```console
    g++ src/main.cpp -o out/yt-dlp-mass-dl
    ```
- Using Makefile
    ```console
    make build
    ```

### Installing
- Manually
    - In Linux
        ```console
        sudo install 0655 out/yt-dlp-mass-dl /usr/local/bin/yt-dlp-mass-dl
        ```
- Using Makefile
    ```console
    sudo make install
    ```

### Uninstalling
- Manually
    - In Linux
        ```console
        sudo rm /usr/local/bin/yt-dlp-mass-dl
        ```
- Using Makefile
    ```console
    sudo make uninstall
    ```

