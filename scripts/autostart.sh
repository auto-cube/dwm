xrandr --output eDP-1 --mode 1920x1080
# xsettingsd &
fcitx5 -d
nm-applet &
xfce4-power-manager &
nitrogen --restore -d
python ~/.dwm/dwm-bar.py &
picom --experimental-backends
