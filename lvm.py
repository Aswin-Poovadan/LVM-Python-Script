import os
from pyfiglet import Figlet
from termcolor import colored
out = Figlet(font = "banner3-D") 
print(colored(out.renderText("LVM"), 'red')) 
print()
def lvmcreate(device_name, vg_name, lv_name, size, direc_name):
  os.system(f'pvcreate {device_name}')
  os.system(f'vgcreate {vg_name} {device_name}')
  os.system(f'vgdisplay {vg_name}')
  os.system(f'lvcreate --size {size}G --name {lv_name} {vg_name}')
  os.system(f'mkfs.ext4 /dev/{vg_name}/{lv_name}')
  os.system('udevadm settle')
  os.system(f'mount /dev/{vg_name}/{lv_name} {direc_name}')
  os.system('lvdisplay')
  os.system('df -h')
  os.system('sleep 2')

def lvmextend(extvg_name, extsize, extlv_name):
  os.system(f'lvextend --size {extsize}G /dev/{extvg_name}/{extlv_name}') 
  os.system(f'resize2fs /dev/{extvg_name}/{extlv_name}')
  os.system('df -h')
  os.system('sleep 2')

def lvmreduce(reduce_dir, reduce_vg, reduce_lv, reduce_size):
  os.system(f'umount {reduce_dir}')
  os.system(f'e2fsck -f /dev/mapper/{reduce_vg}-{reduce_lv}')
  os.system(f'resize2fs /dev/mapper/{reduce_vg}-{reduce_lv} {reduce_size}G')
  os.system(f'lvreduce -L {reduce_size}G /dev/mapper/{reduce_vg}-{reduce_lv} -y')
  os.system(f'mount /dev/mapper/{reduce_vg}-{reduce_lv} {reduce_dir}')
  os.system('df -h')
  os.system('sleep 2')

while True:
  print("1.LV Creation \n2.LV Extend \n3.LV Reduce \n4.Exit\n")
  Choice=input("Choose your Requirement: ") 
  if Choice.strip() == "1":
    device_name = input("Enter the Device Name:  ")
    vg_name = input("Enter VG name: ")
    lv_name = input("Enter the LV name: ")
    size = input("Enter the size of LV: ")
    direc_name = input('Enter the directory name to mount the LV : ')
    lvmcreate(device_name, vg_name, lv_name, size,  direc_name)
    os.system('clear')
  elif Choice.strip() == "2":
    extvg_name = input("Enter the VG name to extend:  ")
    extlv_name = input("Enter the LV name to extend:  ")
    extsize = input("Enter the size to be extended:  ")  
    lvmextend(extvg_name, extsize, extlv_name)
    os.system('clear')
  elif Choice.strip() == "3":
    reduce_dir = input("Enter the mount directory:  ")
    reduce_vg  = input("Enter the VG name to reduce:  ")
    reduce_lv = input("Enter the LV name  to reduce:  ")
    reduce_size = input("Enter the size to be reduced:  ")
    lvmreduce(reduce_dir, reduce_vg, reduce_lv, reduce_size)
    os.system('sleep 4')
    os.system('clear')
  elif Choice.strip() == "4":
    print("Happy Partitioning :) ")
    break
  else:
    print("Wrong Input! Try Again. ")
