## Disclaimer
This is a hobby project so I can learn some Python.  It doesn't work yet.
I'll remove this disclaimer when this project is functional and maybe a little stable.

## Purpose
Maps linode api entities to a fuse filesystem.

## Install

```
./setup.py install --user
 mkdir mnt
 read LINODE_API_KEY
 export LINODE_API_KEY

 # I rerun this line after each change to linodefs.py
 # .. and hoping each time that this leap will be the leap home.
 (sudo umount mnt; ./linodefs.py -o api_key=$LINODE_API_KEY mnt; cd mnt; ls)

```

## Debugging
```
tail -f linodefs.log
```



## Design
Maybe it will look like this?
```
/mnt/lnfs/linodes/
                  linode1234
		  happy -> linode1234
		           /
			    disks
			    configs/
			            config123
				             disks
			    bin/
			        reboot
				shutdown
				start
				destroy
```
It does not look that yet so far.. Very subject to change.
