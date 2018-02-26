# commandline
An imporved version *unx command Use Python and C  

##1. what [python]
what is an improved version of the *w* tool. It finds all processes associated with a TTY(not just those registered in wtmp), and reports all users that are running anything. In particular, unlike w, what will also shows things running in detached screen/tmuxen. 
    
Example output:

```console
$./what
 up 3d06h 16 users  load 0.40 0.39 0.42 procs 1/698
USER     TTY      LOGIN  INPUT OUTPUT WHAT
root     tty1     3d06h  3d06h  3d06h /sbin/agetty --noclear tty1 linux
root     tty7     3d06h  3d06h  3d06h /usr/lib/xorg/Xorg -core :0 -seat seat0 -auth /var/run/lightdm/root/:0 -nolisten tcp vt7 -novtswitch
goku     pts/19   3d06h  2h51m  2h50m ssh -o ServerAliveInterval=30 -p 26861 vps@104.194.77.31
goku     pts/20   5h53m  2h48m  2h48m zsh
goku     pts/21  36m13m 36m08m 34m08m -zsh
goku     pts/2    3d06h     0s     0s python ./what.py
root     none    174 more process
goku     none    82 more process

```