# cl0seted's dotfiles
This is my configuration for my Hyprland on Arch Linux. 

## Requirements
Make sure that you have git and stow on your system
```
sudo pacman -S git stow
```

I intend to add a dependency list that you can pipe into pacman, or a script that auto installs everything required for the stuff in this folder to work. 

Until then, run the following command to install all the necessary dependencies
```bash
sudo pacman -S --needed ghostty hyprland hyprpaper hyprshot waypaper waybar
``` 

## Installation
Clone this repository into your home folder
```bash
$ git clone https://github.com/cl0seted/dotfiles
$ cd dotfiles
```
Use GNU Stow to automatically generate symlinks
```bash
$ stow .
```
